# import os
import argparse
import hashlib
import sys
from datetime import datetime, date, time

text = []

def get_md5_hash(text):
    hasher = hashlib.md5()
    for line in text:
        line = line.encode('utf-8')
        hasher.update(line)
    md5_hash = hasher.hexdigest()
    return md5_hash


def make_timestamp():
    dt = datetime.now()
    return dt.strftime('%Y/%m/%d @ %H:%M:%S')


def write_to_file(data, timestamp, md5_hash, filename='ruthbook.txt'):
    with open(filename, "a") as out:
        out.write('\n')
        out.write(md5_hash)
        out.write(' || ')
        out.write(timestamp)
        for line in text:
            out.write('\n')
            out.write(line)


def save_text(text):
    timestamp = make_timestamp()
    md5_hash = get_md5_hash(text)[0:7]
    write_to_file(text, timestamp, md5_hash)


def main():
    parser = argparse.ArgumentParser(description="Program to write some random notes.")
    parser.add_argument("-f", "--file", help="Filename to write")
    args = parser.parse_args()
    print('Welcome to Ruthbook! Press ctrl+c to save and exit.')
    while True:
        try:
            text.append(input('>>> '))
        except KeyboardInterrupt:
            save_text(text)
            print('Bye!')
            sys.exit()


if __name__ == '__main__':
    main()

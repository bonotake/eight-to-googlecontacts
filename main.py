from __future__ import annotations
import csv
import sys
from typing import List, Union
from common import eightheader, gcheader


def main(eightpath: str, gcpath: str) -> None:
    with open(eightpath, newline='') as eightfile:
        with open(gcpath, 'w', newline='') as gcfile:
            reader = csv.DictReader(eightfile)
            writer = csv.DictWriter(gcfile, fieldnames=gcheader)

            writer.writeheader()
            for row in reader:
                writer.writerow({'E-mail 1 - Value': row['e-mail']})


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

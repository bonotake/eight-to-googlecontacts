"""
Converter from email address list to Google Contacts CSV.

An email address is a bare address like 'takeo.bono@gmail.com'
  or like 'Takeo Imai <takeo.bono@gmail.com>'
"""
import csv
import re
import sys
from typing import List, Optional, Tuple
from common import gcheader

Email = Tuple[Optional[str], str]


def listup(listfile) -> List[Email]:
    pattern = "(.*?)<([\w\.@]+)>,?\n"
    emails: Email = []
    for line in listfile:
        result = re.match(pattern, line)
        email: Email = ('', '')

        if result:
            group = result.groups()
            if len(group) < 2:
                email = ('', result[0])
            else:
                email = (group[0], group[1])

        emails.append(email)

    return emails


def convert(listpath: str, gcpath: str) -> None:
    with open(listpath, newline='') as listfile:
        with open(gcpath, 'w', newline='') as gcfile:
            emails = listup(listfile)
            writer = csv.DictWriter(gcfile, fieldnames=gcheader)

            writer.writeheader()
            for email in emails:
                writer.writerow({'Name': email[0], 'E-mail 1 - Value': email[1]})


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2])

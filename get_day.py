import argparse
import datetime
import subprocess

from pathlib import Path
from zoneinfo import ZoneInfo


current_day = datetime.datetime.now(tz=ZoneInfo('America/New_York')).day

parser = argparse.ArgumentParser(description='Specify AOC day')
parser.add_argument('-d', '--day', default=current_day)
args = parser.parse_args()

path = Path(f'./day{args.day:0>2}/')
path.mkdir(exist_ok=False)

(path / f'day{args.day:0>2}.ipynb').touch()
with open(path / f'day{args.day:0>2}.ipynb', 'w', newline='\n') as file:
    file.write("""{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "259732c8-0c01-42aa-89be-92cb9b66db33",
   "metadata": {},
   "outputs": [],
   "source": [
    "from aocd import get_data, submit\\n",
    "\\n",
    "DAY = %s\\n",
    "YEAR = 2023"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77f10d99-939e-4d7f-bafb-1489d33529bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('input.txt', 'w') as file:\\n",
    "    file.writelines(get_data(day=DAY, year=YEAR))\\n",
    "    \\n",
    "data = get_data(day=DAY, year=YEAR).splitlines()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3d1bb4b-8045-49c2-bfd6-9dd865333c7c",
   "metadata": {},
   "source": [
    "## PART 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "120cf190-601e-4383-967b-38acad54deeb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf6ca7a9-ca01-41fa-8922-b0a7c885c607",
   "metadata": {},
   "outputs": [],
   "source": [
    "submit(answer1, part='a', day=DAY, year=YEAR)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df560372-995f-4692-b8e8-1984a103534c",
   "metadata": {},
   "source": [
    "## PART 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d185dd9f-cd54-4776-a5ab-e2ad6b41bca9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ef058ef-d777-42ed-98da-5110fab4c8a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "submit(answer2, part='b', day=DAY, year=YEAR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff812024-1681-4e03-8edf-7b72e443b6a2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
""" % args.day)

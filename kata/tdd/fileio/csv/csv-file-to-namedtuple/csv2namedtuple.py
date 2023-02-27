from collections import namedtuple
import csv

def csv2namedtuple(file):
    data = csv.reader(file, delimiter=',')
    columns = next(data)
    Row = namedtuple("Row", columns)
    for row in data:
        yield Row(*row)


import os
import pytest

from csv2namedtuple import csv2namedtuple


@pytest.fixture
def given_csvfilename():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_dir, 'departments.csv')

@pytest.fixture
def given_csvfile(given_csvfilename):
    with open(given_csvfilename, "r", encoding="utf-8") as file:
        yield file

def test_reads_entire_file(given_csvfile):
    all_rows = list(csv2namedtuple(given_csvfile))
    assert len(all_rows) == 27
    first_row = all_rows[0]
    assert first_row._asdict() == {
        'department_id': '10',
        'department_name': 'Administration',
        'manager_id': '200',
        'location_id': '1700',
    }
    
import xlrd
from xlrd import xldate as xdate
from .models import WorkbookEntry
from .models import get_col_for_attr

ENTRY_FIELDS = WorkbookEntry._meta.get_fields()[1:]
ALPHABET_MAX = 26

def extract_entries(workbook):
    entries = []
    with xlrd.open_workbook(workbook.file.path) as book:
        sh = book.sheet_by_index(0)
        for rx in range(13, sh.nrows):
            row = sh.row(rx)
            entry = create_entry(row)
            if not entry.is_empty():
                entries.append(entry)
    return entries

def create_entry(row):
    entry = WorkbookEntry()
    for field in ENTRY_FIELDS:
        col = get_col_for_attr(field.name)
        idx = workbook_index(col)
        cell = row[idx]
        if is_date_cell(cell):
            date = xdate.xldate_as_datetime(cell.value, 0)
            value = date
        else:
            value = cell.value
        setattr(entry, field.name, value)
    return entry

def is_date_cell(cell):
    if cell.ctype == 3:
        return True
    return False

def workbook_index(idx):
    base = ord('A')
    sidx = 0
    for i in range(len(idx)):
        delta = i * ALPHABET_MAX
        sidx = ord(idx[i]) - base + delta
    return sidx

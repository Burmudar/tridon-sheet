import xlrd
from xlrd import xldate as xdate
from .models import WorkbookEntry
from .models import WORKBOOK_COL_COUNT
from .models import get_col_for_attr
import datetime

ENTRY_FIELDS = tuple(x for x in WorkbookEntry._meta.get_fields() if x.name not in ('workbook_file', 'id'))
ALPHABET_MAX = 26
ZA_TIMEZONE = datetime.timezone(datetime.timedelta(hours=2), 'ZA')


class WorkbookProcessor(object):

    def __init__(self, start_row=0):
        self.start_row_idx = start_row

    def extract_entries(self, workbook, row_start=-1):
        entries = []
        if row_start == -1:
            row_start = self.start_row_idx
        with xlrd.open_workbook(workbook.file.path) as book:
            sh = book.sheet_by_index(0)
            for rx in range(self.start_row_idx, sh.nrows):
                row = sh.row(rx)
                entry = self.create_entry(workbook, row)
                if not entry.is_empty():
                    entries.append(entry)
        return entries

    def create_entry(self, workbook, row):
        if len(row) < WORKBOOK_COL_COUNT:
            raise WorkbookProcessingError("Workbook has incorrect number of colums")
        entry = WorkbookEntry(workbook_file = workbook)
        for field in ENTRY_FIELDS:
            col = get_col_for_attr(field.name)
            idx = self.col_idx(col) - 1 #zero indexed
            cell = row[idx]
            if self.is_date_cell(cell):
                date = xdate.xldate_as_datetime(cell.value, 0)
                value = date.replace(tzinfo=ZA_TIMEZONE)
            else:
                value = cell.value
            setattr(entry, field.name, value)
        return entry

    def is_date_cell(self, cell):
        if cell.ctype == 3:
            return True
        return False

    def col_idx(self, v):
        sidx = 0
        for i in range(len(v)):
            vIdx = len(v) - (i + 1)
            #Get index of letter in the alphabet
            num = self.__alpha_idx(v[vIdx])
            #'BA' -> B pos is the 'teens' meaning, 26 twice since the base of the number 'BA' is 26
            if i > 0:
                num = num * (ALPHABET_MAX * i)
            sidx += num
        return sidx

    def __alpha_idx(self, v):
        if v.upper() == 'A':
            return 1
        return (ord(v.upper()) - ord('A')) + 1


class WorkbookProcessingError(Exception):
    pass

import xlrd

COLS = ['B', 'D', 'E', 'F', 'G', 'I', 'O', 'T', 'U', 'W', 'AB', 'AG', 'AI', 'AJ', 'BJ'
        'BM']
ALPHABET_MAX = 26

def extract_entries(sheet_path):
    entries = []
    with xlrd.open_workbook(sheet_path) as book:
        sh = book.sheet_by_index(0)
        for rx in range(11, 12): #sh.nrows):
            row = sh.row(rx)
            for cx in COLS:
                idx = sheet_index(cx)
                print(row[idx])


def sheet_index(idx):
    base = ord('A')
    sidx = 0
    for i in range(len(idx)):
        delta = i * ALPHABET_MAX
        sidx = ord(idx[i]) - base + delta
    return sidx

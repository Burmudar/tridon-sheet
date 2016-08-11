import xlrd
import argparse


def dump_file_info(filename):
    with xlrd.open_workbook(filename) as book:
        print("Dumping info from: {0}".format(filename))
        print("The number of worksheets is {0}".format(book.nsheets))
        print("Worksheet name(s): {0}".format(book.sheet_names()))
        sh = book.sheet_by_index(0)
        print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
        #for rx in range(sh.nrows):
            #print(sh.row(rx))


def main(files):
    for f in files:
        dump_file_info(f)


def parse_file_names():
    parser = argparse.ArgumentParser(description="XLS Files to dump info on")
    parser.add_argument('files', metavar='files', type=str, nargs='+',
                        help='a file to dump info on')
    args = parser.parse_args()
    return args.files

if __name__ == "__main__":
    files = parse_file_names()
    main(files)

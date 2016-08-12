from django.shortcuts import render
from django.http import HttpResponse
from .forms import SheetFileForm
import xlrd
# Create your views here.


def sheet_upload(request):
    if request.method == 'POST':
        form = SheetFileForm(request.POST, request.FILES)
        form.add_sheet_hash()
        if form.is_valid():
            form.save()
            entries = extract_entries(form.instance)
            save_entries(entries)
    else:
        form = SheetFileForm()
    return render(request, 'sheet/sheet_file_form.html', {'form': form})


def extract_entries(model):
    entries = []
    cols = ['A', 'C', 'H', 'J', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'V', 'X', 'Y', 'Z',
            'AA', 'AC', 'AD', 'AE', 'AF', 'AH', 'AK', 'AL', 'AM', 'AO', 'AP', 'AQ', 'AR',
            'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE',
            'BF', 'BG', 'BH', 'BL']
    with xlrd.open_workbook(model.sheet_file.path) as book:
        sh = book.sheet_by_index(0)
        for rx in range(15, sh.nrows):
            row = sh.row(rx)
            for cx in cols:
                idx = sheet_index(cx)
                print(row[idx])

def sheet_index(idx):
    base = ord('A')
    sidx = 0
    for i in range(len(idx)):
        delta = i * 24
        sidx = ord(idx[i]) - base + delta
    return sidx


def save_entries(entries):
    pass


def index(request):
    return HttpResponse("Hello, world. YOu're at the sheet index.")

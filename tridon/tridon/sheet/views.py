from django.shortcuts import render
from django.http import HttpResponse
from .forms import WorkbookFileForm
from .sheets import extract_entries
# Create your views here.


def sheet_upload(request):
    if request.method == 'POST':
        form = WorkbookFileForm(request.POST, request.FILES)
        form.add_sheet_hash()
        if form.is_valid():
            form.save()
            entries = extract_entries(form.instance)
            save_entries(entries)
    else:
        form = WorkbookFileForm()
    return render(request, 'sheet/workbook_file_form.html', {'form': form})




def save_entries(entries):
    pass


def index(request):
    return HttpResponse("Hello, world. YOu're at the sheet index.")

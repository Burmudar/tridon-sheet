from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import WorkbookFileForm
from .processors import WorkbookProcessor
from .models import WorkbookEntry
from .models import WorkbookFile
# Create your views here.


def sheet_upload(request):
    if request.method == 'POST':
        form = WorkbookFileForm(request.POST, request.FILES)
        form.add_sheet_hash()
        if form.is_valid():
            form.save()
            processor = WorkbookProcessor(start_row=14)
            entries = processor.extract_entries(form.instance)
            WorkbookEntry.objects.bulk_create(entries)
            return render(request, 'sheet/workbookentry_list.html', {'workbook', form.instance})
    else:
        form = WorkbookFileForm()
        return render(request, 'sheet/workbook_file_form.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world. YOu're at the sheet index.")


class SheetEntryView(ListView):
    template_name = "sheet/entries_by_workbook_file.html"
    context_object_name = "workbook_entries"

    def get_queryset(self):
        self.workbook = get_object_or_404(WorkbookFile, id=self.kwargs['workbook_pk'])
        return WorkbookEntry.objects.filter(workbook_file=self.workbook)

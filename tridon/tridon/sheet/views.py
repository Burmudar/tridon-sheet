from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from .forms import WorkbookFileForm
from .processors import WorkbookProcessor
from .models import WorkbookEntry
from .models import WorkbookFile
# Create your views here.


def sheet_upload(request):
    if request.method == 'POST':
        form = WorkbookFileForm(request.POST, request.FILES)
        form.update_instance()
        if form.is_valid():
            form.save()
            processor = WorkbookProcessor(start_row=14)
            entries = processor.extract_entries(form.instance)
            WorkbookEntry.objects.bulk_create(entries)
            return redirect('sheet:invoice-detail', pk=form.instance.id)
    else:
        form = WorkbookFileForm()
        return render(request, 'sheet/workbook_file_form.html', {'form': form})


def index(request):
    return render(request, 'sheet/index.html')


def documents(request):
    return render(request, 'sheet/documents.html')


def about(request):
    return render(request, 'sheet/about.html')


def contact(request):
    return render(request, 'sheet/contact.html')


def invoice(request):
    context = {
        'workbooks': WorkbookFile.objects.all(),
        'selected_wb': None,
        'entries': []
    }
    return render(request, 'sheet/invoice.html', context)


class SheetEntryView(ListView):
    template_name = "sheet/entries_by_workbook_file.html"
    context_object_name = "workbook_entries"

    def get_queryset(self):
        if 'workbook_pk' in self.kwargs and self.kwargs['workbook']:
            pass
        self.workbook = get_object_or_404(WorkbookFile, id=self.kwargs['workbook_pk'])
        return WorkbookEntry.objects.filter(workbook_file=self.workbook)


class SheetDetailView(ListView, SingleObjectMixin):
    template_name = "sheet/invoice.html"
    context_object_name = "entries"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=WorkbookFile.objects.all())
        return super(SheetDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SheetDetailView, self).get_context_data(**kwargs)
        context['workbooks'] = WorkbookFile.objects.all()
        context['selected_wb'] = self.object
        return context

    def get_queryset(self):
        if self.object is None:
            return []
        return self.object.workbookentry_set.all()

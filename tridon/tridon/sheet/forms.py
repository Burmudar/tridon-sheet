from django import forms
from .models import WorkbookFile
from .utils import hash_file


class WorkbookFileForm(forms.ModelForm):
    class Meta:
        model = WorkbookFile
        fields = ['file']

    def add_sheet_hash(self):
        formFile = self.files['file']
        self.instance.file_hash = hash_file(formFile)

    def clean(self):
        cleaned_data = super(WorkbookFileForm, self).clean()
        if self.file_has_valid_ext():
            raise forms.ValidationError("Only Excel files with ('xls' extension) can be uploaded")
        if self.instance.file_hash == '' or self.instance.file_hash is None:
            raise forms.ValidationError("Spreadsheet has an invalid hash")
        if self.is_duplicate():
            raise forms.ValidationError("Spreadsheet has already been uploaded")
        return cleaned_data

    def file_has_valid_ext(self):
        wb = self.files['file']
        return not wb.name.endswith('xls')

    def is_duplicate(self):
        sheets = WorkbookFile.objects.filter(file_hash__exact=self.instance.file_hash)
        return len(sheets) > 0

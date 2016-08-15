from django import forms
from .models import WorkbookFile
import hashlib


class WorkbookFileForm(forms.ModelForm):
    class Meta:
        model = WorkbookFile
        fields = ['path']

    def add_sheet_hash(self):
        hasher = hashlib.sha256()
        hasher.update(self.files['sheet_file'].read())
        sheet_hash = hasher.hexdigest()
        self.instance.sheet_hash = sheet_hash

    def clean(self):
        cleaned_data = super(WorkbookFileForm, self).clean()
        if self.file_has_valid_ext():
            raise forms.ValidationError("Only Excel files with ('xls' extension) can be uploaded")
        if self.instance.sheet_hash == '' or self.instance.sheet_hash == None:
            raise forms.ValidationError("Spreadsheet has an invalid hash")
        if self.is_duplicate():
            raise forms.ValidationError("Spreadsheet has already been uploaded")
        return cleaned_data

    def file_has_valid_ext(self):
        sheet = self.files['sheet_file']
        return not sheet.name.endswith('xls')

    def is_duplicate(self):
        sheets = WorkbookFile.objects.filter(sheet_hash__exact=self.instance.sheet_hash)
        return len(sheets) > 0

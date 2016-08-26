import unittest
import datetime
from .processors import WorkbookProcessor
from .processors import WorkbookProcessingError
from .processors import ZA_TIMEZONE
from .models import WorkbookEntry
from .models import WorkbookFile
from .utils import hash_file

# Create your tests here.
class WorkbookProcessorTest(unittest.TestCase):

    def setUp(self):
        self.processor = WorkbookProcessor()
        self.expected_entries = [
            WorkbookEntry(date_received=datetime.datetime(2016, 5, 3, 22, 15, 6, tzinfo=ZA_TIMEZONE),
                          consignment_id=169579892,
                          consignment_no="CTKIN117420",
                          reference="4) CTKIN117420 9) 28) 169579892",
                          return_no='',
                          service_level=406,
                          sender="C-TEK",
                          consignee="SS AGENCIES",
                          consignee_suburb="PORT ELIZABETH",
                          packets=1,
                          kgs_used=2.00,
                          rate_per_kg=1.94,
                          min_charge=86.14,
                          doc_fee=10.11,
                          fuel_surcharge=14.92,
                          amount=126.825
                          ),
            WorkbookEntry(date_received=datetime.datetime(2016, 5, 4, 22, 10, 6, tzinfo=ZA_TIMEZONE),
                          consignment_id=169643990,
                          consignment_no="TRE1891ZWARTKOP",
                          reference="4) TRE1891ZWARTKOP 9) 28) 169643990",
                          return_no='',
                          service_level=406,
                          sender="TRIDON LOGISTICS (PTY) LTD.",
                          consignee="OUTDOOR WAREHOUSE CENTURION GATE",
                          consignee_suburb="CENTURION",
                          packets=20,
                          kgs_used=80.00,
                          rate_per_kg=1.31,
                          min_charge=75.37,
                          doc_fee=10.11,
                          fuel_surcharge=27.46,
                          amount=241.8624
                          ),
            WorkbookEntry(date_received=datetime.datetime(2016, 5, 16, 22, 14, 15, tzinfo=ZA_TIMEZONE),
                          consignment_id=170240404,
                          consignment_no="CTKIN117573",
                          reference="4) CTKIN117573 9) 28) 170240404",
                          return_no='',
                          service_level=406,
                          sender="C-TEK",
                          consignee="SHAUN NEL",
                          consignee_suburb="LADYSMITH",
                          packets=1,
                          kgs_used=3.00,
                          rate_per_kg=5.38,
                          min_charge=96.90,
                          doc_fee=10.11,
                          fuel_surcharge=16.59,
                          amount=141.0408
                          )
        ]
        self.WORKBOOK_3_ENTRIES_START_ROW_1 = WorkbookFile(file="test_resources/3_entries_start_row_1.xls")
        self.WORKBOOK_3_ENTRIES_START_ROW_1.file_hash = hash_file(self.WORKBOOK_3_ENTRIES_START_ROW_1.file)
        self.WORKBOOK_3_ENTRIES_START_ROW_5 = WorkbookFile(file="test_resources/3_entries_start_row_5.xls")
        self.WORKBOOK_3_ENTRIES_START_ROW_5.file_hash = hash_file(self.WORKBOOK_3_ENTRIES_START_ROW_5.file)
        self.WORKBOOK_3_ENTRIES_START_ROW_1_WITH_GAP = WorkbookFile(file="test_resources/3_entries_start_row_1_with_gap.xls")
        self.WORKBOOK_3_ENTRIES_START_ROW_1_WITH_GAP.file_hash = hash_file(self.WORKBOOK_3_ENTRIES_START_ROW_1_WITH_GAP.file)
        self.WORKBOOK_WRONG_COL_COUNT = WorkbookFile(file="test_resources/wrong_cols_count.xls")

    def test_extract_entries_can_be_saved(self):
        self.WORKBOOK_3_ENTRIES_START_ROW_1.save()
        entries = self.processor.extract_entries(self.WORKBOOK_3_ENTRIES_START_ROW_1)
        WorkbookEntry.objects.bulk_create(entries)
        self.assertEquals(len(entries), len(WorkbookEntry.objects.all()))

    def test_col_idx(self):
        idx = self.processor.col_idx("A")
        exp_idx = 1
        self.assertEquals(idx, exp_idx)
        idx = self.processor.col_idx("Z")
        exp_idx = 26
        self.assertEquals(idx, exp_idx)
        idx = self.processor.col_idx("M")
        exp_idx = 13
        self.assertEquals(idx, exp_idx)
        idx = self.processor.col_idx("AB")
        exp_idx = 28
        self.assertEquals(idx, exp_idx)
        idx = self.processor.col_idx("AZ")
        exp_idx = 52
        self.assertEquals(idx, exp_idx)
        idx = self.processor.col_idx("BA")
        exp_idx = 53
        self.assertEquals(idx, exp_idx)
        idx = self.processor.col_idx("BZ")
        exp_idx = 78
        self.assertEquals(idx, exp_idx)

    def test_extract_entries(self):
        entries = self.processor.extract_entries(self.WORKBOOK_3_ENTRIES_START_ROW_1)
        self._assert_equal_list(entries, self.expected_entries)
        entries = self.processor.extract_entries(self.WORKBOOK_3_ENTRIES_START_ROW_5, row_start=5)
        self._assert_equal_list(entries, self.expected_entries)
        entries = self.processor.extract_entries(self.WORKBOOK_3_ENTRIES_START_ROW_1_WITH_GAP)
        self._assert_equal_list(entries, self.expected_entries)

    def test_exception_is_thrown_when_sheet_has_incorrect_col_count(self):
        with self.assertRaises(WorkbookProcessingError):
            self.processor.extract_entries(self.WORKBOOK_WRONG_COL_COUNT)

    '''
    Only used for comparing unsaved list of WorkbookEntry instances
    '''
    def _assert_equal_list(self, actual, expected):
        self.assertEquals(len(actual), len(expected))
        for i in range(len(actual)):
            self._assert_equal_entry(actual[i], expected[i])

    '''
    Only used for comparing unsaved WorkbookEntry instances
    '''
    def _assert_equal_entry(self, actual, expected):
        for k in actual.__dict__:
            if k.startswith('_'):
                continue
            self.assertEqual(actual.__dict__[k], expected.__dict__[k])

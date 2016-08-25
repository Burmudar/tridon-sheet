import unittest
import datetime
from .processors import WorkbookProcessor
from .models import WorkbookEntry
from .models import WorkbookFile

# Create your tests here.
class WorkbookProcessorTest(unittest.TestCase):

    def setUp(self):
        self.processor = WorkbookProcessor()
        self.WORKBOOK_3_ENTRIES_START_ROW_1 = WorkbookFile(file="test_resources/3_entries_start_row_1.xls")

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

    def test_equals(self):
            first = WorkbookEntry(date_received=datetime.datetime( 2016, 5, 3, 22, 15, 00),
                                    consignment_id="169579892",
                                    consignment_no="CTKIN117420",
                                    reference="4) CTKIN117420 9) 28) 169579892",
                                    return_no=-1,
                                    service_level=406,
                                    sender="C-TEK",
                                    consignee="SS AGENCIES",
                                    consignee_suburb="PORT ELIZABETH",
                                    packets="1",
                                    kgs_used=2.00,
                                    rate_per_kg=1.94,
                                    min_charge=86.14,
                                    doc_fee=10.11,
                                    fuel_surcharge=14.92,
                                    amount=126.83
                                )
            second = WorkbookEntry(date_received=datetime.datetime(2016, 5, 4, 22, 10, 00),
                                    consignment_id="169643990",
                                    consignment_no="TRE1891ZWARTKOP",
                                    reference="4) TRE1891ZWARTKOP 9) 28) 169643990",
                                    return_no=-1,
                                    service_level=406,
                                    sender="TRIDON LOGISTICS (PTY) LTD.",
                                    consignee="OUTDOOR WAREHOUSE CENTURION GATE",
                                    consignee_suburb="ZWARTKOP",
                                    packets="20",
                                    kgs_used=80.00,
                                    rate_per_kg=1.31,
                                    min_charge=75.37,
                                    doc_fee=10.11,
                                    fuel_surcharge=27.46,
                                    amount=241.8624,
                                )
            self.assertNotEqual(first, second)
            firstv2 = WorkbookEntry(date_received=datetime.datetime(2016, 5, 3, 22, 15, 00),
                                    consignment_id="169579892",
                                    consignment_no="CTKIN117420",
                                    reference="4) CTKIN117420 9) 28) 169579892",
                                    return_no=-1,
                                    service_level=406,
                                    sender="C-TEK",
                                    consignee="SS AGENCIES",
                                    consignee_suburb="PORT ELIZABETH",
                                    packets="1",
                                    kgs_used=2.00,
                                    rate_per_kg=1.94,
                                    min_charge=86.14,
                                    doc_fee=10.11,
                                    fuel_surcharge=14.92,
                                    amount=126.83
                                )
            self.assertEqual(first, firstv2)

    def test_extract_entries(self):
        expected_entries = [
            WorkbookEntry(date_received=datetime.datetime(2016, 5, 3, 22, 15, 6),
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
            WorkbookEntry(date_received=datetime.datetime(2016, 5, 4, 22, 10, 6),
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
            WorkbookEntry(date_received=datetime.datetime(2016, 5, 16, 22, 14, 15),
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
        entries = self.processor.extract_entries(self.WORKBOOK_3_ENTRIES_START_ROW_1)
        self.assertEquals(len(entries), len(expected_entries))
        for i in range(len(entries)):
            actual = entries[i]
            expected = expected_entries[i]
            for k in actual.__dict__:
                if k == '_state':
                    continue
                self.assertEqual(actual.__dict__[k], expected.__dict__[k])

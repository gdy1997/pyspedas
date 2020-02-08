
import os
import unittest

from pyspedas.utilities.dailynames import dailynames
from pyspedas import tcopy, time_string, time_double
from pytplot import get_data, store_data

class UtilTestCases(unittest.TestCase):
    def test_dailynames(self):
        self.assertTrue(dailynames(trange=['2015-12-1', '2015-12-1/2:00'], hour_res=True) == ['2015120100', '2015120101'])

    def test_time_string(self):
        self.assertTrue(time_string(1450181243.767) == '2015-12-15 12:07:23.767000')
        self.assertTrue(time_string([1450181243.767, 1450181263.767]) == ['2015-12-15 12:07:23.767000', '2015-12-15 12:07:43.767000'])

    def test_tcopy(self):
        store_data('test', data={'x': [1, 2, 3], 'y': [5, 5, 5]})
        tcopy('test')
        t, d = get_data('test-copy')
        self.assertTrue(t.tolist() == [1, 2, 3])
        self.assertTrue(d.tolist() == [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
import unittest
from fastq_filter import fastq_f
from argparse import Namespace
import os

args_d = Namespace(filename='SP1.fq', gc_bounds=[55, 60], keep_filtered=True, min_length=15,
                   output_base_name='out_test')


class TestFastq_f(unittest.TestCase):
    def test_is_working(self):
        fastq_f(args_d)
        self.assertTrue(os.path.exists('./out_test__passed.fastq'))
        if os.path.exists('./out_test__passed.fastq'):
            os.remove('./out_test__passed.fastq')
        self.assertTrue(os.path.exists('./out_test__failed.fastq'))
        if os.path.exists('./out_test__failed.fastq'):
            print('hm')
            os.remove('./out_test__failed.fastq')


if __name__ == "__main__":
    unittest.main()

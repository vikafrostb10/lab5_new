import unittest
import main_program


class TestCalc(unittest.TestCase):

    def test_calculate_whole_week(self):
        self.assertEqual(main_program.calculate_whole_week(2014, 'April', 'May', 'Wednesday'), 5)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()

import unittest as ut
import formula as sf

class unit_tests(ut.TestCase):

    def test_class_limit(self):
       self.assertEqual(sf.class_limit(10,5,2), 2)

    def test_percent(self):
        self.assertEqual(sf.percent(10, 20), 50)
    
    def test_relative_frequency(self):
        self.assertEqual(sf.relative_frequncy(5, 20), 0.25)
    
    def test_mid_point(self):
        self.assertEqual(sf.mid_point(10, 5), 7.5)
    
    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        n = len(data)
        self.assertEqual(sf.mean(data, n), 3.0)

    def test_median(self):
        data_odd_len = [1, 2, 3, 4, 5]
        data_even_len = [1, 2, 3, 4, 5, 6]

        self.assertEqual(sf.medine(data_even_len), 3.5)
        self.assertEqual(sf.medine(data_odd_len), 3)

    def test_mid_range(self):
        self.assertEqual(sf.mid_range(10, 5), 7.5)

    def test_mean_for_grouped_data(self):
        data = [1.5,5.5,9.5,13.5,17.5]
        frequncy = [2,3,8,3,2]
        n = sum(frequncy)

        self.assertEqual(sf.mean_for_grouped_data(data,frequncy,n), 9.5)

    def test_medine_for_grouped_data(self): 
        # class intervals, frequency, cumulative frequency
        f = [[40, 49, 6,  6], 
             [50, 59, 8, 14],
             [60, 69, 12,26],
             [70, 79, 14,40],
             [80, 89, 7, 47],
             [90, 99, 3, 50]]
             
        self.assertEqual(sf.medine_for_grouped_data(f,14), 68.25)

    def test_mod(self):
        data = [1,1,2,2,2]

        self.assertEqual(sf.mode(data), [2])


if __name__ == "__main__":
    ut.main()
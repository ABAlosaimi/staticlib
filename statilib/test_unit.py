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

    def test_pop_variance(self):
        x = [["a", 1],
             ["b", 2],
             ["c", 5],
             ["d", 7],
             ["e", 10]]
        
        self.assertEqual(sf.pop_variance(x), 10.8)

    def test_variance_grouped(self):
        x = [[50, 59, 6 , 54.5],
             [60, 69, 10, 64.5],
             [70, 79, 7 , 74.5],
             [80, 89, 12, 84.5],
             [90, 99, 5 , 94.5]]
        
        self.assertAlmostEqual(sf.variance_grouped(x), 169.23, places=4)


    def test_coff_of_variation_sample(self):
        x = [[1, 3],
             [2, 5],
             [3, 6],
             [4, 4],
             [5, 3],
             [6, 5],
             [7, 4]]
        
        self.assertAlmostEqual(sf.coff_of_variation_sample(x), 25.96, delta=1.00)

    def test_coumulative_frequncy_percentile(self):
        x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        desired_rank = 45

        self.assertEqual(sf.coumulative_frequncy_percentile(x, desired_rank), 40.0)
    
    def test_percentile(self):
        x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        desired_rank = 45

        self.assertEqual(sf.percentile(x, desired_rank), 45.0)

    def test_percentile_to_value(self):
        x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        percentile = 45

        self.assertEqual(sf.percentile_to_value(x, percentile), 50)

    def test_z_scores_pop(self):
        x = [["a", 1],
             ["b", 2],
             ["c", 5],
             ["d", 7],
             ["e", 10]]
        value = 7

        self.assertAlmostEqual(sf.z_scores_pop(value, x), 0.73, delta=1.00)
    
    def test_z_scores_sample(self):
        x = [["a", 1],
             ["b", 2],
             ["c", 5],
             ["d", 7],
             ["e", 10]]
        value = 7

        self.assertAlmostEqual(sf.z_scores_sample(value, x), 0.82, delta=1.00)

    def test_quar_of(self):
        x = [32, 44, 50, 53, 58, 62, 68, 70, 75, 76, 82, 89, 94, 95]
        
        self.assertEqual(sf.quar_of(x), [51.5, 69.0, 85.5])

    def test_outlier(self):
        x = [10, 12, 14, 15, 18, 19, 20, 22, 24, 30, 100]
        
        self.assertEqual(sf.outlier(x), [100])

    def test_correlation_coefficient(self):
        data = [[1, 2],
                [2, 3],
                [3, 5],
                [4, 4],
                [5, 6]]
        n = len(data)

        self.assertAlmostEqual(sf.correlation_coefficient(data, n), 0.9, delta=0.1)

    def test_regression_line(self):
        data = [[3, 8],
                [9, 6],
                [5, 4],
                [3, 2]]
        
        result = sf.regression_line(data)
        
        self.assertAlmostEqual(result[0], 4.166, delta=1.0)
        self.assertAlmostEqual(result[1], 0.166, delta=1.0)
    
    def test_prob(self):
        event = 5 
        total_events = 10

        self.assertEqual(sf.prob(event,total_events), 0.5)
        self.assertEqual(sf.event_comp(event,total_events), 0.5)
        self.assertEqual(sf.emprical_prob(event,total_events), 0.5)

    
if __name__ == "__main__":
    ut.main()
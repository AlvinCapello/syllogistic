from syllogistic_validity import is_distributed, is_undistributed, is_negative, is_positive, arg_structure, common_term, is_copula, term_counter, distributed_term_finder, undistributed_term_finder, both_premises_undistributed, either_premises_undistributed, is_valid, converse
import unittest

class TestSyllogisticValidity(unittest.TestCase):
    
        def test_is_distributed(self):
            self.assertEqual(is_distributed("a"),None)
            self.assertEqual(is_distributed("e"),"a")
            self.assertEqual(is_distributed("i"),["a","b"])
            self.assertEqual(is_distributed("o"),"b")
    
        def test_is_undistributed(self):
            self.assertEqual(is_undistributed("a"),["a","b"])
            self.assertEqual(is_undistributed("e"),"b")
            self.assertEqual(is_undistributed("i"),None)
            self.assertEqual(is_undistributed("o"),["a","b"])
    
        def test_is_negative(self):
            self.assertEqual(is_negative("a"),False)
            self.assertEqual(is_negative("e"),True)
            self.assertEqual(is_negative("i"),False)
            self.assertEqual(is_negative("o"),True)
    
        def test_is_positive(self):
            self.assertEqual(is_positive("a"),True)
            self.assertEqual(is_positive("e"),False)
            self.assertEqual(is_positive("i"),True)
            self.assertEqual(is_positive("o"),False)
    
        def test_arg_structure(self):
            self.assertEqual(arg_structure("a","b","c"),["a","b","c"])
            self.assertEqual(arg_structure("a","b","c"),["a","b","c"])
            self.assertEqual(arg_structure("a","b","c"),["a","b","c"])
            self.assertEqual(arg_structure("a","b","c"),["a","b","c"])
    
        def test_common_term(self):
            self.assertEqual(common_term("a","b"),"")
            self.assertEqual(common_term("a","b"),"")
            self.assertEqual(common_term("a","b"),"")
            self.assertEqual(common_term("a","b"),"")
    
        def test_is_copula(self):
            self.assertEqual(is_copula("a"),True)
            self.assertEqual(is_copula("e"),True)
            self.assertEqual(is_copula("i"),True)
            self.assertEqual(is_copula("o"),True)
    
        def test_term_counter(self):
            self.assertEqual(term_counter("a","b","c"),{"a","b","c"})
            self.assertEqual(term_counter("a","b","c"),{"a","b","c"})
            self.assertEqual(term_counter("a","b","c"),{"a","b","c"})
            self.assertEqual(term_counter("a","b","c"),{"a","b","c"})
    
        def test_distributed_term_finder(self):
            self.assertEqual(distributed_term_finder("a","b","c"),{"Premise_1":[],"Premise_2":[],"Conclusion":[]})

        def test_undistributed_term_finder(self):
            self.assertEqual(undistributed_term_finder("a","b","c"),{"Premise_1":[],"Premise_2":[],"Conclusion":[]})
        
        def test_both_premises_undistributed(self):
            self.assertEqual(both_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
            self.assertEqual(both_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
            self.assertEqual(both_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
            self.assertEqual(both_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
        
        def test_either_premises_undistributed(self):
            self.assertEqual(either_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
            self.assertEqual(either_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
            self.assertEqual(either_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
            self.assertEqual(either_premises_undistributed({"Premise_1":[],"Premise_2":[],"Conclusion":[]},""))
        
        def test_is_valid(self):
            self.assertEqual(is_valid("a","b","c"),True)
            self.assertEqual(is_valid("a","b","c"),True)
            self.assertEqual(is_valid("a","b","c"),True)
            self.assertEqual(is_valid("a","b","c"),True)

        def test_converse(self):
            self.assertEqual(converse("a"),"b")
            self.assertEqual(converse("e"),"b")
            self.assertEqual(converse("i"),"b")
            self.assertEqual(converse("o"),None)
        
if __name__ == '__main__':
    unittest.main()


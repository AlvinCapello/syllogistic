def is_distributed(p):
    if p[1] == "i":
        return None
    elif p[1] == "a":
        return p[0]
    elif p[1] == "e":
        return [p[0],p[2]]
    elif p[1] == "o":
        return p[2]

def is_undistributed(p):
    if p[1] == "i":
        return [p[0],p[2]]
    elif p[1] == "a":
        return p[2]
    elif p[1] == "e":
        return None
    elif p[1] == "o":
        return p[0]

def is_negative(p):
    if p[1] == "e" or p[1] == "o":
        return True
    else:
        return False

def is_positive(p):
    if p[1] == "a" or p[1] == "i":
        return True
    else:
        return False

def arg_structure(p,q,r):
    prop_list = []
    for prop in (p,q,r):
        prop_list.append(prop)
    return prop_list

def common_term(p,q):
    middle = ""
    for i in p:
        if is_copula(i):
            pass
        elif i in q:
            middle = i
            break
    return middle

def is_copula(p):
    if p == "a" or p == "e" or p == "i" or p == "o":
        return True
    else:
        return False

def term_counter(p,q,r):
    standard_form = arg_structure(p,q,r)
    terms = set()
    for prop in standard_form:
        for letter in prop:
            if is_copula(letter):
                prop.replace(letter,"")
            else:
                terms.add(letter)
    return set(terms)

def distributed_term_finder(p,q,r):
    terms = {"Premise_1":[],"Premise_2":[],"Conclusion":[]}
    for prop in (p,q,r):
        if is_distributed(prop) is not None:
            if prop == p:
                terms["Premise_1"] = is_distributed(p)
            elif prop == q:
                terms["Premise_2"] = is_distributed(q)
            else:
                terms["Conclusion"] = is_distributed(r)
    return terms

def undistributed_term_finder(p,q,r):
    terms = {"Premise_1":[],"Premise_2":[],"Conclusion":[]}
    for prop in (p,q,r):
        if is_undistributed(prop) is not None:
            if prop == p:
                terms["Premise_1"] = is_undistributed(p)
            elif prop == q:
                terms["Premise_2"] = is_undistributed(q)
            else:
                terms["Conclusion"] = is_undistributed(r)
    return terms

def both_premises_undistributed(dictionary,search_string):
    if search_string in dictionary["Premise_1"] and search_string in dictionary["Premise_2"]:
        return True
    return False

def either_premises_undistributed(dictionary,search_string):
    if search_string in dictionary["Premise_1"] or search_string in dictionary["Premise_2"]:
        return True
    return False

def is_valid(p,q,r):
    total_terms = term_counter(p,q,r)
    distributed_terms = distributed_term_finder(p,q,r)
    undistributed_terms = undistributed_term_finder(p,q,r)
    major_term = r[2]
    minor_term = r[0]
    middle_term = common_term(p,q)
  
    if both_premises_undistributed(undistributed_terms,middle_term):
        print("Invalid: Fallacy of Undistributed Middle")
        return False
    elif is_negative(p) and is_negative(q):
        print("Invalid: Fallacy of Two Negative Premises")
        return False
    elif len(total_terms) > 3:
        print("Invalid: Fallacy of Four Terms")
        return False
    elif is_distributed(r) is not None and major_term in is_distributed(r):
        if either_premises_undistributed(undistributed_terms,major_term):
            print("Invalid: Fallacy of Illicit Major")
            return False
    elif is_distributed(r) is not None and minor_term in is_distributed(r):
        if either_premises_undistributed(undistributed_terms,minor_term):
            print("Invalid: Fallacy of Illicit Minor")
            return False
    elif is_negative(p) or is_negative(q):
        if is_positive(r):
            print("Invalid: Negative Premise with Positive Conclusion")
            return False
    elif is_negative(r):
        if is_positive(p) and is_positive(q):
            print("Invalid: Positive Premises with Negative Conclusion")
            return False
    else:
        print("Valid")
        return True

def converse(p):
    if p[0] == "a":
        print(p[2] + "i" + p[1])
        return p[2] + "i" + p[1]
    elif p[0] == "e":
        print(p[2] + p[0] + p[1])
        return p[2] + p[0] + p[1]
    elif p[0] == "i":
        print(p[2] + p[0] + p[1])
        return p[2] + p[0] + p[1]
    elif p[0] == "o":
        print("None")
        return None
    return None


def main():
    p = input("Enter the first premise: ")
    q = input("Enter the second premise: ")
    r = input("Enter the conclusion: ")
    print(is_valid(p,q,r))

while True:
    main()


"Please write unit tests for all the above functions."

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


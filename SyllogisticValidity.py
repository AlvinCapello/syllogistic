"""
First: find some what to structure the argument input so that the data in it is iterable (I could just force this by
fiat, but I think this application will be more robust if I have a way to fine-tune this process).

Second: find some way to determine the number of terms in the argument. This will require finding the unique schematic
characters and filtering out duplicates.

Third: find some way to assert that a term is distributed. Not sure yet how I will do this without declarative constructs
but I might be able to get the same effect through some conditional logic in a function.

Fourth: we will also need to count the  number of negative sentences. If the conclusion is negative, this will cause
some further conditional logic to fire.

Fifth: we will need to determine the major, minor, and middle terms of the argument. For reference: the major term is the
predicate of the conclusion, whilst the minor term is the subject of the conclusion.
"""

def is_distributed(p):
    if p[1] == "i":
        return None
    elif p[1] == "a":
        return p[0]
    elif p[1] == "e":
        return p[0],p[2]
    elif p[1] == "o":
        return p[2]

def is_undistributed(p):
    if p[1] == "i":
        return p[0],p[2]
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
    terms = set()
    for prop in (p,q,r):
        if is_distributed(prop) == None:
            pass
        if len(is_distributed(prop)) > 1:
            for letter in is_distributed(prop):
                terms.add(letter)
        else:
            terms.add(is_distributed(prop))
    return terms.remove(None)

def is_valid(p,q,r):
    total_terms = term_counter(p,q,r)
    distributed_terms = distributed_term_finder(p,q,r)
    major_term = r[2]
    minor_term = r[0]
    middle_term = common_term(p,q)
    print(middle_term)
    print(distributed_terms)

    if middle_term not in distributed_terms:
        print("Invalid: Fallacy of Undistributed Middle")
        return False
    elif is_negative(p) and is_negative(q):
        print("Invalid: Fallacy of Two Negative Premises")
        return False
    elif len(total_terms) > 3:
        print("Invalid: Fallacy of Four Terms")
        return False
    elif major_term in is_distributed(r):
        if major_term in is_undistributed(p) and major_term in is_undistributed(q):
            print("Invalid: Fallacy of Illicit Major")
            return False
    elif minor_term in is_distributed(r):
        if minor_term in is_undistributed(p) and minor_term in is_undistributed(q):
            print("Invalid: Fallacy of Illicit Minor")
            return False
        else:
            pass
    elif is_negative(p) or is_negative(q):
        if is_positive(r):
            print("Invalid: Negative Premise with Positive Conclusion")
            return False
        else:
            pass
    elif is_negative(r):
        if is_positive(p) and is_positive(q):
            print("Invalid: Positive Premises with Negative Conclusion")
            return False
    else:
        print("Valid")
        return True


is_valid("QiR", "PiQ", "PaR")

distributed_term_finder("QiR", "PiQ", "PaR")



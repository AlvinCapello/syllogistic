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
        arg_list.append(prop)
    return prop_list

def is_valid(p,q,r):
    syllogism = arg_structure[p,q,r]
    premises = [p,q]
    total_terms = {p,q,r}
    distributed_terms = {is_distributed(p), is_distributed(q), is_distributed(r)}
    undistributed_terms = {is_undistributed(p), is_undistributed(q), is_undistributed(r)}
    major_term = r[2]
    minor_term = r[0]
    middle_term = p.intersection(q)

    if middle_term in undistributed_terms:
        print("Invalid: Your argument commits the Fallacy of Undistributed Middle")
    elif is_negative(p) and is_negative(q):
        print("Invalid: Your argument commits the Fallacy of Two Negative Premises")
    elif len(total_terms) > 3:
        print("Invalid: Your argument commits the Fallacy of Four Terms")
    elif major_term in [undistributed_terms,]


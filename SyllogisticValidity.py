"""
First: find some what to structure the argument input so that the data in it is iterable (I could just force this by
fiat, but I think this application will be more robust if I have a way to fine-tune this process).

Second: find some way to determine the number of terms in the argument. This will require finding the unique schematic
characters and filtering out duplicates.

Third: find some way to assert that a term is distributed. Not sure yet how I will do this without declarative constructs
but I might be able to get the same effect through some conditional logic in a function.
"""

def distribution_check(p):
    if p[1] == "i":
        return None
    elif p[1] == "a":
        return p[0]
    elif p[1] == "e":
        return p[0],p[2]
    elif p[1] == "o":
        return p[2]


def is_valid(p,q,r):
    arg_list = []
    arg_list.append(p,q,r)

    for arg in arg_list:


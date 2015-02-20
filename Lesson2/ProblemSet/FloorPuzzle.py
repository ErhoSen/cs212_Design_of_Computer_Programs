#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def higher_floor(h1, h2):
    # h1 lives on a higher flor then h2
    return h1>h2

def adjecent(h1, h2):
    return abs(h1-h2) == 1

def floor_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    humans = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(humans)) # 1
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if not Hopper is top
                if not Kay is bottom
                if not Liskov in (top, bottom)
                if higher_floor(Perlis, Kay)
                if not adjecent(Ritchie, Liskov)
                if not adjecent(Liskov, Kay)
    )

print floor_puzzle()

# def floor_puzzle():
#     # Your code here
#     return [Hopper, Kay, Liskov, Perlis, Ritchie]
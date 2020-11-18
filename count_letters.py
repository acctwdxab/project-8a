# Dan Wu
# 11/17/2020
# Write a function that takes as a parameter a string and returns a dictionary that tabulates how many of each letter is in that string.


def count_letters ( string ):
    """takes string as parameter and returns a dictionary that tabulates each letter and its count"""
    letter = dict ()
    for x in string.upper () :
            if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z') :
                if not letter.get ( x ) :
                    letter[x] = 1
                else :
                    letter[x] += 1
                    return letter


# Dan Wu
# 11/17/2020
# Write a function that takes as a parameter a string and returns a dictionary that tabulates how many of each letter is in that string.



def count_letters (string):
 """takes string as parameter and returns a dictionary that tabulates each letter and its count"""
 letter_dic = {}
 for character in string.upper () :
    if character in ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if character in letter_dic :
                letter_dic[character] += 1
        else :
                    letter_dic[character] = 1
 return letter_dic


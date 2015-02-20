# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def is_palindrome(text):
    if len(text) == 1:
        return True
    text_length = len(text)
    middle = text_length / 2
    if text_length % 2: # if odd(3,5,7)
        return text[0:middle] == text[middle+1:][::-1]
    else:
        return text[0:middle] == text[middle:][::-1]

# print is_palindrome("racecar")
# print is_palindrome("radar")
# print is_palindrome("muuuum")
# print is_palindrome("ra")

def easy(text):
    if text == '':
        return (0, 0)
    text = text.upper()
    c = 0
    i = 0
    palindroms = set([])
    visited = set([])
    while i < len(text):
        current = text[i:i+c]
        if current not in visited:
            # print "i:", i, "c:", c, "current:", current
            if is_palindrome(current):
                palindroms.add((i, i+c))
                # print palindroms, current
            visited.add(current)
        # else:
        #     print "vis"
        c+=1
        if c > len(text):
            i+=1
            c = 0
            if i > len(text):
                break
    return max(palindroms, key=lambda val: val[1]-val[0])

# print easy('')

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if len(text) == 0:
        return (0,0)
    text = text.upper()
    # print text
    result = (0,0)
    result_dist = 0
    start = 0
    end = 1
    i = 0
    visited = set([])
    # while i < len(text):
    while i+1 < len(text):
        current = text[start:end]
        # print "i:", i, "start:", start, "end:", end, "current:", current
        if current not in visited:
            if is_palindrome(current):
                # print "PALINDROM!!!", current
                if (end - start) > result_dist:
                    result_dist = end - start
                    result = (start, end)

                if end + 1 > len(text):
                    i+=1
                    start = i
                    end = i+1
                    continue

                if is_palindrome(text[start:end+1]):
                    if (end+1 - start) > result_dist:
                        result = (start, end+1)
                        result_dist = end + 1 - start

                if start - 1 < 0: start = 0
                else: start-=1
                end+=1
            else:
                visited.add(current)
        elif len(current) % 2 == 0:
            i+=1
            start = i
            end = i+1
        else:
            if end+1 > len(text):
                i+=1
                start = i
                end = i+1
            else:
                end+=1
    return result

#print longest_subpalindrome_slice('Race carr')

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        result = ''
        for i, ch in enumerate(reversed(word)):
            result += str(10**i) + '*' + ch
            if i+1 != len(word):
                result+="+"
        return '(' + result + ')'
    else:
        return word

print compile_word("YOUlower")
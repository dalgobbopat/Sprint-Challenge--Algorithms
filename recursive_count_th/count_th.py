'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if length of word is less than th or 0 return 0
    if len(word) == 0 or len(word) < len("th"):
        return 0
    #if first 2 letters are not "th" recurse removing the first two indicies from the word
    if word[:2] != "th":
        return count_th(word[1:])
    else:
        return count_th(word[1:]) + 1
    
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    n1 = len(word)
    if(n1 == 0 or n1 < 2):
        return 0

    def recurses(word, value):
        if len(word) < 2:
            return value
        if(word[0:2] == "th"):
            value += 1
        return recurses(word[1:], value)
    
    value = recurses(word, 0)
    return value
    """
    for real thou why cant i just do this lmao
    return word.count("th")
    """

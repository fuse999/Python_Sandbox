

def abbreviation(a, b):
    from collections import Counter
    if len(a) >= len(b):
        string_diff = Counter(a) - Counter(b)
        upper_diff = Counter(a.upper()) - Counter(b)
        for letter in string_diff.keys():
            if letter.isupper():
                return "NO"
            if letter.upper() in upper_diff: 
                a=a.replace(letter,"")
        if a.upper() != b:
            return "NO"
    return "YES"
    #13/16
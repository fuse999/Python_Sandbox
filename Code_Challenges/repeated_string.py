def repeatedString(s, n):
    L = len(s)
    return (s.count('a') * (n//L) + s[:n % L].count('a'))


x = "abc"
n = 8

print(repeatedString("abc", 89))
## https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

def rotLeft(a, d):
    # print(a)
    # print(d)
    lst = a
    while d != 0:
        lst.append(lst[0])
        lst.pop(0)
        d -= 1
    return(lst)
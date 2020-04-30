def checkMagazine(magazine, note):
    answer = "Yes"
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            answer = "No"
            break
    print(answer)

# But this was to slow with O(N^2)

# so I desited T use the hash table method

def checkMagazine(magazine, note):
    answer = "Yes"
    magazine_hash = {}
    for word in magazine:
        if word in magazine_hash:
            magazine_hash[word] += 1
        else:
            magazine_hash[word] = 1
           
    for word in note:
        if word in magazine_hash and magazine_hash[word] > 0:
            magazine_hash[word] -= 1
        else:
            answer = "No"
            break
    print(answer)
def findMergeNode(headA, headB):
    len_a = 0
    walker = headA

    while walker.next != None:
        len_a += 1
        walker = walker.next

    len_b = 0
    walker = headB

    while walker.next != None:
        len_b += 1
        walker = walker.next 

    while len_a > len_b:
        headA = headA.next
        len_a -= 1

    while len_b > len_a:
        headB = headB.next
        len_b -= 1

    while True:
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next
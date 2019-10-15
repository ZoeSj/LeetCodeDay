class ListNode():  # init construct func
    def __init__(self, value):
        self.value = value
        self.next = None


def Creatlist(n):
    if n <= 0:
        return False
    if n == 1:
        return ListNode(1)  # only one node
    else:
        root = ListNode(1)
        tmp = root
        for i in range(2, n + 1):  # add node one by one
            tmp.next = ListNode(i)
            tmp = tmp.next
    return root  # return root node


def printlist(head):  # print chain table by traversal
    p = head
    while p != None:
        print p.value
        p = p.next


def listlen(head):  # length for chain table
    c = 0
    p = head
    while p != None:
        c = c + 1
        p = p.next
    return c


def insert(head, n):  # insert param before n
    if n < 1 or n > listlen(head):
        return

    p = head
    for i in range(1, n - 1):  # traversal 4 to 5 .only remove one by one .range not include n-1
        p = p.next
    a = raw_input("Enter a value:")
    t = ListNode(value=a)
    t.next = p.next
    p.next = t
    return head


def dellist(head, n):  # delete chain
    if n < 1 or n > listlen(head):
        return head
    elif n is 1:
        head = head.next  # delete header
    else:
        p = head
        for i in range(1, n - 1):
            p = p.next  # traversal 2
        q = p.next
        p.next = q.next  # put 5 behind 3
    return head


def main():
    print "Create a linklist"
    head = Creatlist(7)
    printlist(head)
    print
    print "___________________________"

    n1 = raw_input("Enter the index to insert")
    n1 = int(n1)
    insert(head, n1)
    printlist(head)
    print
    print "___________________________"

    n2 = raw_input("Enter the index to delete")
    n2 = int(n2)
    dellist(head, n2)
    printlist(head)


if __name__ == '__main__':  main()  # main func use

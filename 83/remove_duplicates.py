def remove_duplicates_from_list(head):
    for i in head:
        count_i = head.count(i)
        if count_i > 1:
            head.remove(i)
    print(head)


def remove(head: ListNode) -> ListNode:
    p = head
    while p and p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next

    return head


# remove_duplicates_from_list([1, 1, 2, 3, 4, 4, 4, 5])
remove([1, 1, 2, 3, 4, 4, 4, 5])

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Create a dummy node to handle edge cases like removing head
    dummy = ListNode(0)
    dummy.next = head
    
    slow = fast = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both fast and slow until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next
# time complexity: O(L) where L is the length of the linked list
# space complexity: O(1) since we are using a constant amount of space
# Test the function
if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2  # Remove the 2nd node from the end (should remove node with value 4)

    new_head = removeNthFromEnd(head, n)

    # Print the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
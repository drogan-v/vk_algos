from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def linked_list_from_array(arr: list[int]) -> Optional["ListNode"]:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def linked_list_to_array(head: Optional[ListNode]) -> list[int]:
    result = []
    cur = head
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    return result


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    
    head = prev
    return head


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    # Быстрый указатель позволяет определить середину за один проход,
    # потому что когда медленный пройдет половину пути, быстрый пройдет
    # 2 * половину пути. Т. е. 2 * 1/2 = 1. То есть когда быстрый пройдет 
    # весь путь, медленный как раз будет в середине
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def remove_element(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # Внутренний элемент мы удаляем просто соединяя предыдущую ноду со
    # следующей. В случае головы мы как раз сделали фейковую ноду, чтобы
    # случай свелся к удалению внутренней ноды.
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head

    while cur is not None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    
    return dummy.next

def is_subsequence(a: str, b: str) -> bool:
    # Мы ставим указатели на обе строки, и сдвигаем первый только
    # когда второй оказался на букве из изначального слова.
    # Если после прохода слова `b` указатель на слове `a` не выйдет за конец,
    # то мы не можем получить слово b обычным добавлением букв.
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)


def find_target_as_sum(arr: list[int], target: int) -> bool:
    # Алгос работает за O(n) потому что в худшем случае мы пройдем
    # по всем элементам массива, которых n штук
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            return True
    return False


def is_palindrome(s: str) -> bool:
    # Делаем два указателя на начало и конец. Символы сравниваются так же, как 
    # написано их сравнение в спецификации питона. O(n) потому что в худшем 
    # случае (палиндром) мы пройдем все n символов
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def remove_duplicates(arr: list[int]) -> int:
    # Мы просто меняем следующий символ тогда, когда найдем НЕ дубликат.
    if not arr:
        return 0
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


def merge_linked_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    # работает за O(n + m), потому что в худшем случае мы пройдем по всем элементам списков
    # не требует доп памяти, потому что мы из двух списков делаем один, изменяя соединения
    dummy = ListNode()
    curr = dummy
    
    while a and b:
        if a.val < b.val:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    
    curr.next = a or b
    return dummy.next



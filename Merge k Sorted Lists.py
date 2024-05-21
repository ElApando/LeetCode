def mergeKLists(lists):

    Lista_Nueva = [] 

    for i in lists:
        for j in i:
            Lista_Nueva.append(j)
    
    Lista_Nueva.sort()

    return Lista_Nueva

# class Solution:
#     def mergeKLists(self, lists):
#         if not lists:
#             return None
#         if len(lists) == 1:
#             return lists[0]
        
#         mid = len(lists) // 2
#         left = self.mergeKLists(lists[:mid])
#         right = self.mergeKLists(lists[mid:])
        
#         return self.merge(left, right)
    
#     def merge(self, l1, l2):
#         dummy = ListNode(0)
#         curr = dummy
        
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
        
#         curr.next = l1 or l2
        
#         return dummy.next

Lista = [[1,4,5],[1,3,4],[2,6]]
# Lista = [ListNode(val) for val in Lista]


Activo = mergeKLists(Lista)
print("WWW",Activo)
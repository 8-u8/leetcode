# %% ListNodeクラス
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode{val=" + str(self.val) + ", next={" + str(self.next) + "}}"

# %%
list1 = ListNode(1, ListNode(2, 4))
list2 = ListNode(1, ListNode(3, 4))

# %% 再帰するような関数を考える

def list_to_ListNode(l: list):
    if len(l) < 1:
        return None
    elif len(l) == 1:
        return ListNode(l[0])
    return ListNode(val=l[0], next=list_to_ListNode(l[1:]))
# %%
def ListNode_to_list(listnode: ListNode) -> list:
    # print(listnode)
    val = listnode.val # int
    out = [] 
    out.append(val)
    del val
    if listnode.next != None:
        out += ListNode_to_list(listnode.next)
    else:
        return out
    return out

# %%
l1 = [1,2,4]
print(list_to_ListNode(l1))

listnode_test = list_to_ListNode([1,2,4])
ListNode_to_list(listnode_test)
# %%
list1 = ListNode(1, ListNode(val=2, next=ListNode(val=4, next=None)))
list1_ = ListNode_to_list(list1)


# %%
list2 = ListNode(1, ListNode(val=3, next=ListNode(val=4, next=None)))
list2_ = ListNode_to_list(list2)
# %%
list_out = list1_ + list2_
list_out = sorted(list_out)
list_to_ListNode(list_out)
# %% より速いコード
# https://leetcode.com/problems/merge-two-sorted-lists/solutions/5531659/beats-above-75-of-the-users
node = ListNode()
instance = node

while list1 and list2: # list1とlist2が空でない場合
    if list1.val < list2.val:
        instance.next = list1
        list1 = list1.next
    else:
        instance.next = list2
        list2 = list2.next
    instance = instance.next

if list1: # list1のみ空でない場合
    instance.next = list1
if list2: # list2のみ空でない場合
    instance.next = list2
# Returning the node next because the init value is set to zero.
return node.next

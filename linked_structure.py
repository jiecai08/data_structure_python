# @author: Cai Jie
# @Date:   2018/5/9 15:41


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def main():
    # create a simple link structure
    # simple_single_link()

    # loop generate single linked structure
    head = loop_linked()

    # 遍历
    # traverse_the_linked(head)

    # 搜索
    # search_linked(head, "G")

    # access ith element
    # _ = access_ith_linked(head, 2)

    # replace the element
    # replace(head, "C", "G")

    # 插入头部O(1)
    head = insert(head, "G")




def simple_single_link():
    node_2 = Node("A")
    node_3 = Node("B", node_2)
    node_1 = Node("C", node_3)


def loop_linked():
    head = None
    data = ["A", "B", "C", "D", "E", "F"]
    for item in data:
        head = Node(item, head)
    return head

    # use the head will delete the node
    # while head is not None:
    #     print(head.data)
    #     head = head.next


def traverse_the_linked(head):
    prob = head
    while prob is not None:
        print(prob.data)
        prob = prob.next

def search_linked(head, target):
    prob = head
    while prob is not None:
        if prob.data == target:
            print("find the target in linked")
            return True
        else:
            prob = prob.next
    print("the target is not in linked")
    return False


def access_ith_linked(head, index):
    prob = head
    while index > 0:
        prob = prob.next
        index -= 1
    print("ith element of the linked is %s" % prob.data)
    return prob.data


def replace(head, origin, substution):
    prob = head
    while prob is not None:
        if prob.data == origin:
            prob.data = substution
            traverse_the_linked(head)
            return True
        else:
            prob = prob.next
    print("cannot find the origin data")
    return False

def insert(head, item):
    head = Node(item, head)
    traverse_the_linked(head)
    return head




if __name__ == '__main__':
    main()
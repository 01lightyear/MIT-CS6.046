'''
Solution given by chatgpt
using 4 stacks 
思路：in_stack进栈存储，同时维护这部分各个尾子列的最小值在in_min_stack中
out_stack储存待输出的项，和in_stack不会有重叠，同时维护这部分各个尾子列的最小值在out_min_stack中
当dequeue时，out_stack更新，若out_stack为空，倒序存储in_stack同时清空两个in栈
'''
class FIFO:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]
        self.in_min_stack=[]
        self.out_min_stack=[]
    def enqueue(self,x):
        self.in_stack.append(x)
        if not self.in_min_stack or x<=self.in_min_stack[-1]:
            self.in_min_stack.append(x)
        else:
            self.in_min_stack.append(self.in_min_stack[-1])
    def dequeue(self):
        if self.out_stack:
            self.out_min_stack.pop()
            return self.out_stack.pop()
        while self.in_stack:
            target=self.in_stack.pop()
            self.in_min_stack.pop()
            self.out_stack.append(target)
            if not self.out_min_stack or target<=self.out_min_stack[-1]:
                self.out_min_stack.append(target)
            else:
                self.out_min_stack.append(self.out_min_stack[-1])
        if self.out_stack:
            self.out_min_stack.pop()
            return self.out_stack.pop()
        return "No element remains"
    def find_min(self):
        if(not self.in_stack and not self.out_stack):
            return "No element remains"
        if not self.in_min_stack:
            return self.out_min_stack[-1]
        if not self.out_min_stack:
            return self.in_min_stack[-1]
        return min(self.in_min_stack[-1],self.out_min_stack[-1])
test = FIFO()
# 一系列入队操作
test.enqueue(10)
test.enqueue(20)
test.enqueue(5)
test.enqueue(15)
test.enqueue(3)
test.enqueue(8)

print("最小值:", test.find_min())  # 应输出 3

# 出队操作
print("出队:", test.dequeue())    # 应输出 10
print("最小值:", test.find_min())  # 应输出 3

print("出队:", test.dequeue())    # 应输出 20
print("最小值:", test.find_min())  # 应输出 3

# 更多入队操作
test.enqueue(2)
test.enqueue(12)

print("最小值:", test.find_min())  # 应输出 2

# 出队操作
print("出队:", test.dequeue())    # 应输出 5
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 15
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 3
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 8
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 2
print("最小值:", test.find_min())  # 应输出 12

print("出队:", test.dequeue())    # 应输出 12
print("最小值:", test.find_min())

'''
官方解答
思路很简单，使用双向队列，main即全部元素，min维护从当前项到尾端的最小值（数量不一定和main相同）
如果main被删除的首项和min首项相同，此时已经到了某个尾子列的最小值（即其头部），因而删除之
'''
from collections import deque
class Solution:
    def __init__(self):
        self.main=deque()
        self.min=deque()
    def enqueue(self,x):
        self.main.append(x)
        while self.min and self.min[-1]>x:
            self.min.pop()
        self.min.append(x)
    def dequeue(self):
        target=self.main.popleft()
        if target==self.min[0]:
            self.min.popleft()
        return target
    def find_min(self):
        if self.min:
            return self.min[0]
        return "No element remains"
test = Solution()
# 一系列入队操作
test.enqueue(10)
test.enqueue(20)
test.enqueue(5)
test.enqueue(15)
test.enqueue(3)
test.enqueue(8)

print("最小值:", test.find_min())  # 应输出 3

# 出队操作
print("出队:", test.dequeue())    # 应输出 10
print("最小值:", test.find_min())  # 应输出 3

print("出队:", test.dequeue())    # 应输出 20
print("最小值:", test.find_min())  # 应输出 3

# 更多入队操作
test.enqueue(2)
test.enqueue(12)

print("最小值:", test.find_min())  # 应输出 2

# 出队操作
print("出队:", test.dequeue())    # 应输出 5
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 15
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 3
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 8
print("最小值:", test.find_min())  # 应输出 2

print("出队:", test.dequeue())    # 应输出 2
print("最小值:", test.find_min())  # 应输出 12

print("出队:", test.dequeue())    # 应输出 12
print("最小值:", test.find_min())
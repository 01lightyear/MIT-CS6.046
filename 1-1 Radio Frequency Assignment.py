'''
主要思想：分治
按x排序，分成至多只有2个的子集，判断子集中是否存在不符合条件的点对
合并：秩序考虑两个集合边界上的点，也就是距离x0左右1以内的点，放入strip中（x0为左右两侧集合横坐标最接近的点的平均数）
strip中按y排序，考虑到与当前点距离小于1的点必定在以该点为底部中点的2*1矩形内，而该矩形内可分为8个0.5*0.5的区域，显然每个区域至多1个点
因此只需要检测该点之后的7个点即可（使时间复杂度为O（nlogn）的关键一步）
'''
import math
class FoundSolution(Exception):
    def __init__(self, value):
        self.value=value
class Node:
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
def distance_larger_than_one(node1,node2):
    return math.sqrt((node1.x-node2.x)**2+(node1.y-node2.y)**2)>=1
def divide(Nodes):
    try:
        if(len(Nodes)>2):
            left=divide(Nodes[:len(Nodes)//2])
            right=divide(Nodes[len(Nodes)//2:])
            return merge(left,right)
        elif(len(Nodes)==2):
            if not distance_larger_than_one(Nodes[0],Nodes[1]):
                raise FoundSolution((Nodes[0],Nodes[1]))    
            return Nodes
        else:
            return Nodes
    except FoundSolution as e:
        raise e
def merge(Nodes1,Nodes2):
    try:
        x0=(Nodes1[len(Nodes1)-1].x+Nodes2[0].x)/2
        strip=[]
        for i in Nodes1:
            if abs(i.x-x0)<=1:
                strip.append(i)
        for i in Nodes2:
            if abs(i.x-x0)<=1:
                strip.append(i)
        strip=sorted(strip,key=lambda Node:Node.y)
        for i in range(0,len(strip)-1):
            count=0
            for j in strip[i+1:]:
                count+=1
                if not distance_larger_than_one(strip[i],j):
                    raise FoundSolution((strip[i],j))
                if count>=7:
                    break
        return Nodes1+Nodes2
    except FoundSolution as e:
        raise e
test_cases = [
    # 测试集1：包含距离接近1的点对
    [
        Node(1.0, 2.0),
        Node(2.0, 3.0),
        Node(3.0, 1.0),
        Node(4.0, 5.0),
        Node(5.0, 4.0),
        Node(3.5, 1.8),  # 与 (3.0, 1.0) 距离小于1
    ],
    
    # 测试集2：较密集的点分布
    [
        Node(1.0, 1.0),
        Node(1.5, 2.5),
        Node(2.0, 3.0),
        Node(2.5, 4.5),
        Node(3.0, 2.0),
        Node(3.5, 1.5),
        Node(4.0, 3.5),
        Node(4.5, 5.0),
    ],
    
    # 测试集3：对角线分布
    [
        Node(1.0, 1.0),
        Node(2.0, 2.1),
        Node(3.0, 3.2),
        Node(4.0, 4.3),
        Node(5.0, 5.4),
        Node(2.8, 3.0),  # 与 (3.0, 3.2) 距离小于1
    ],
    
    # 测试集4：较分散的点
    [
        Node(1.0, 5.0),
        Node(2.5, 1.0),
        Node(4.0, 3.0),
        Node(5.5, 2.0),
        Node(7.0, 4.0),
        Node(8.5, 1.0),
    ]
]

# 测试每组数据
test_nodes=test_cases[2]
Nodes = sorted(test_nodes, key=lambda node: node.x)
try:
    result = divide(Nodes)
    print("没有找到距离小于1的点对")
except FoundSolution as e:
    point1, point2 = e.value
    print(f"找到距离小于1的点对：")
    print(f"点1: ({point1.x}, {point1.y})")
    print(f"点2: ({point2.x}, {point2.y})")
    dist = math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    print(f"两点间距离: {dist:.3f}")
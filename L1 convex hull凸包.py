from collections import deque
class node:
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
def intercept(a,b,x):
    return a.y+(b.y-a.y)*(x-a.x)/(b.x-a.x)
def merge(left,right):
    nodeleft=max(left,key=lambda node:node.x)
    noderight=min(right,key=lambda node:node.x)
    x0=(nodeleft.x+noderight.x)/2
    while True:
        maxintercept=intercept(nodeleft,noderight,x0)
        prev_left=left[left.index(nodeleft)-1]
        if(intercept(prev_left,noderight,x0)>maxintercept):#左部凸包逆时针更新
            nodeleft=prev_left
            continue
        next_right=right[(right.index(noderight)+1)%len(right)]
        if(intercept(nodeleft,next_right,x0)>maxintercept):
            noderight=next_right
            continue
        break
    upper_node_left=nodeleft
    upper_node_right=noderight
    nodeleft=max(left,key=lambda node:node.x)
    noderight=min(right,key=lambda node:node.x)
    while True:
        minintercept=intercept(nodeleft,noderight,x0)
        prev_left=left[left.index(nodeleft)-1]
        if(intercept(prev_left,noderight,x0)<minintercept):#左部凸包逆时针更新
            nodeleft=prev_left
            continue
        next_right=right[(right.index(noderight)+1)%len(right)]
        if(intercept(nodeleft,next_right,x0)<minintercept):#右部凸包顺时针更新
            noderight=next_right
            continue
        break
    lower_node_left=nodeleft
    lower_node_right=noderight
    result=deque()
    i=right.index(upper_node_right)
    while True:
        result.append(right[i])
        if(right[i]==lower_node_right):
            break;
        i=(i+1)%len(right)
    i=left.index(lower_node_left)
    while True:
        result.append(left[i])
        if(left[i]==upper_node_left):
            break;
        i=(i+1)%len(left)
    return result
def cross_product(a,b,c):#计算叉积判断三点的顺时针方向
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)
def convex_hull(nodes):
    if all(nodes[0].x==i.x for i in nodes):#处理所有点横坐标相同的情况
        return deque(sorted(nodes,key=lambda node:node.y))
    elif(len(nodes)<=2):
        result=deque(nodes)
        return result
    elif(len(nodes)==3):
        result=deque()
        if(cross_product(nodes[0],nodes[1],nodes[2])<0):
            result.append(nodes[0])
            result.append(nodes[1])
            result.append(nodes[2])
        else:
            result.append(nodes[0])
            result.append(nodes[2])
            result.append(nodes[1])
        return result
    else:
        Nodes=sorted(nodes,key=lambda node:(node.x,node.y))
        mid_x=Nodes[len(Nodes)//2].x
        left=deque(p for p in Nodes if p.x<mid_x)
        right=deque(p for p in Nodes if p.x>mid_x)
        middle=deque(p for p in Nodes if p.x==mid_x)
        right=middle+right#把横坐标相等的点放在同一组以规避斜率无穷大的情况
        return merge(convex_hull(left),convex_hull(right))
node1=node(0, 2)    # 内部点
node0=node(0, 0)   # 凸包顶点
node6=node(6, 3)    # 凸包顶点
node2=node(2, 7)     # 凸包顶点
node8=node(8, 4)     # 凸包顶点
node4=node(4, 1)     # 内部点
node3=node(3, 5)     # 内部点
node5=node(5, 6)     # 凸包顶点
points=[node1,node2,node3,node4,node6,node0,node5,node8]
for i in convex_hull(points):
    print(f"({i.x},{i.y})")

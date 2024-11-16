'''思路：
1.任选一个点为根，DFS搜索所有其他节点
2.利用DFS中子节点在父节点前面的性质，依次计算A，B
其中A为选取该节点时，该节点及其子树的利润和
B为不选该节点时，该节点及其子树的利润和
递归计算A，B
3.最后比较根节点的A，B，选择利润较大的一个
4.从根节点开始，若A>B,则选择该节点，并递归选择其孙子节点
若B>A,则不选该节点，并递归选择其儿子节点
'''
class Node:
    def __init__(self,profit,name):
        self.name=name
        self.profit=profit
        self.A=0.0
        self.B=0.0
        self.father=[]
        self.children=[]
        self.adjacent=[]
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return str(self.name)
    def add_adjacent(self,args):
        args = args if isinstance(args, list) else [args]
        for i in args:
            if(i not in self.adjacent):
                self.adjacent.append(i)
            if(self not in i.adjacent):
                i.adjacent.append(self)
def search_from_root():
    reached=[]
    result=[]
    def search(root):
        nonlocal reached
        nonlocal result
        unreached_neighbor=[i for i in root.adjacent if i not in reached]
        root.children=unreached_neighbor
        for i in unreached_neighbor:
            i.father.append(root)
        reached.append(root)
        if unreached_neighbor!=[]:
            for i in unreached_neighbor:
                search(i)
            result.append(root)
        else:
            result.append(root)
        return result
    return search
class find_best_profit:
    chosen=[]
    @staticmethod
    def choose(root,chosen):
        if root.A>root.B:
            chosen.append(root)
            for i in root.children:
                for j in i.children:
                    find_best_profit.choose(j,chosen)
        else:
            for i in root.children:
                find_best_profit.choose(i,chosen)
    @staticmethod
    def find_best_profit(Nodes):
        for i in Nodes:
            if i.children==[]:
                i.A=i.profit
                i.B=0.0
            else:
                i.A=i.profit+sum(j.B for j in i.children)
                i.B=sum(max(j.A,j.B) for j in i.children)
        root=Nodes[len(Nodes)-1]
        find_best_profit.choose(root,find_best_profit.chosen)
        return max(Nodes[len(Nodes)-1].A,Nodes[len(Nodes)-1].B)
def test_case1():
    """
    测试用例1：简单的线性结构
    A(10) -- B(5) -- C(8)
    预期结果：选择 A 和 C，最大利润 = 18
    """
    A = Node(10, "A")
    B = Node(5, "B")
    C = Node(8, "C")
    
    A.add_adjacent(B)
    B.add_adjacent(C)
    
    Nodes = search_from_root()(A)
    print("\n测试用例1 - 线性结构:")
    print(f"最大利润: {find_best_profit.find_best_profit(Nodes)}")
    print(f"选择的节点: {find_best_profit.chosen}")

def test_case2():
    """
    测试用例2：完全二叉树结构
         A(10)
        /     \
      B(8)   C(7)
     /  \    /  \
    D(6) E(5) F(4) G(3)
    """
    A = Node(10, "A")
    B = Node(8, "B")
    C = Node(7, "C")
    D = Node(6, "D")
    E = Node(5, "E")
    F = Node(4, "F")
    G = Node(3, "G")
    
    A.add_adjacent(B)
    A.add_adjacent(C)
    B.add_adjacent(D)
    B.add_adjacent(E)
    C.add_adjacent(F)
    C.add_adjacent(G)
    
    Nodes = search_from_root()(A)
    print("\n测试用例2 - 完全二叉树:")
    print(f"最大利润: {find_best_profit.find_best_profit(Nodes)}")
    print(f"选择的节点: {find_best_profit.chosen}")

def test_case3():
    """
    测试用例3：不规则树结构
         A(12)
        /    \
      B(8)    C(10)
     /        /  \
    D(5)    E(6)  F(7)
              \
               G(4)
    """
    A = Node(12, "A")
    B = Node(8, "B")
    C = Node(10, "C")
    D = Node(5, "D")
    E = Node(6, "E")
    F = Node(7, "F")
    G = Node(4, "G")
    
    A.add_adjacent(B)
    A.add_adjacent(C)
    B.add_adjacent(D)
    C.add_adjacent(E)
    C.add_adjacent(F)
    E.add_adjacent(G)
    
    Nodes = search_from_root()(A)
    print("\n测试用例3 - 不规则树:")
    print(f"最大利润: {find_best_profit.find_best_profit(Nodes)}")
    print(f"选择的节点: {find_best_profit.chosen}")

# 运行所有测试用例
if __name__ == "__main__":
    test_case1()
    find_best_profit.chosen = []  # 重置chosen列表
    test_case2()
    find_best_profit.chosen = []  # 重置chosen列表
    test_case3()
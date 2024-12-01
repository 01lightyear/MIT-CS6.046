'''
对于二分图中找到最大的两端点一一对应（需要通过中间的边）
'''
from collections import deque
def hopcroft_karp(U,V,E):
    adj={u:[] for u in U}
    for u,v in E:
        adj[u].append(v)
    pair_U={u:None for u in U}
    pair_V={v:None for v in V}
    dist={}
    def bfs():#构建层级图以便接下来使用DFS进行搜索
        queue=deque()
        for u in U:#将所有未配对的U中节点u设置未第0层，并且bfs搜索其相邻未匹配的v（如果v已经匹配，从v的匹配节点开始继续搜索，直到搜索到一个未匹配的v）
            if pair_U[u] is None:
                dist[u]=0
                queue.append(u)
            else:
                dist[u]=float('inf')
        dist[None]=float('inf')#（1）设置dist[None]因为未匹配的节点在pair中对应值为None，用以表示v中为匹配的节点，在下面dfs中辅以判断（见下方（1））
        while queue:
            u=queue.popleft()
            if u is not None:
                for v in adj[u]:
                    if dist[pair_V[v]]==float('inf'):#表示未匹配
                        dist[pair_V[v]]=dist[u]+1
                        queue.append(pair_V[v])
        return dist[None]!=float('inf')
    def dfs(u):
        if u is not None:#如果使None则已经达到增广路径的末端
            for v in adj[u]:
                if dist[pair_V[v]]==dist[u]+1:#如果找到的v的匹配节点是层级图中的下一层，则可以采用之 （1）
                    if dfs(pair_V[v]):#即已经到达None节点即已经找到了一条增广路径
                        pair_U[u]=v#在递归搜索的同时递归将未配对路径和配对路径翻转
                        pair_V[v]=u
                        return True
            dist[u]=float('inf')#即这个点怎么搜也搜不到未匹配结点了，于是避免在当次bfs对应的所有dfs中继续在搜索路径中考虑之，即在上面的（1）中条件判断将其排除
            return False
        return True
    matching=0
    while bfs():
        for u in U:
            if pair_U[u] is None:
                if dfs(u):
                    matching+=1
    return matching,pair_U
# 示例测试数据和测试代码

def test_hopcroft_karp():
    U = ['A', 'B', 'C', 'D']
    V = ['1', '2', '3', '4']
    E = [
        ('A', '1'),
        ('A', '2'),
        ('B', '2'),
        ('B', '3'),
        ('C', '3'),
        ('C', '4'),
        ('D', '4')
    ]

    expected_matching = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4'
    }

    matching_count, matching = hopcroft_karp(U, V, E)
    
    assert matching_count == 4, f"期望匹配数为4, 但是得到 {matching_count}"
    assert matching == expected_matching, f"期望匹配关系为 {expected_matching}, 但是得到 {matching}"

    print("所有测试通过！")

if __name__ == "__main__":
    test_hopcroft_karp()
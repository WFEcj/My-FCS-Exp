import networkx as nx
import random

# 参数设置
n = 100  # 顶点数
q = 0.5  # 边生成概率

# 生成随机图 G1
G1 = nx.erdos_renyi_graph(n, q)

# 为 G1 的边分配权重，权重是 [5, 20] 之间的随机整数
# for u, v in G1.edges():
#     G1[u][v]['weight'] = random.randint(10, 50)

# 生成 G2，与 G1 具有相同的顶点和边集
# G2 = G1.copy()

# 为 G2 的边分配权重，权重是 [-5, 0] 之间的随机整数
# for u, v in G2.edges():
#     G2[u][v]['weight'] = random.randint(-10, 0)

# 将 G1 和 G2 的结果写入文件
def write_graph_to_file(graph, filename, mode='w'):
    with open(filename, mode) as f:
        for u, v, data in graph.edges(data=True):
            f.write(f"{u} {v}\n")

# 写入文件
write_graph_to_file(G1, "DstrongTracking_100.txt", mode='w')  # 写入 G1，覆盖模式
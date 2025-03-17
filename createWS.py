import networkx as nx
import random

# 参数设置
n = 100  # 顶点数
q = 0.5  # 边生成概率

# 生成随机图 G1
G1 = nx.erdos_renyi_graph(n, q)

# 为 G1 的边分配权重，权重是 [5, 20] 之间的随机整数
for u, v in G1.edges():
    G1[u][v]['weight'] = random.randint(10, 70)

# 生成 G2，与 G1 具有相同的顶点和边集
G2 = G1.copy()

# 为 G2 的边分配权重，权重是 [-5, 0] 之间的随机整数
for u, v in G2.edges():
    G2[u][v]['weight'] = random.randint(-10, 0)

# 将 G1 和 G2 的结果写入文件
def write_graph_to_file(graph, filename, mode='w'):
    with open(filename, mode) as f:
        for u, v, data in graph.edges(data=True):
            f.write(f"{u} {v} {data['weight']}\n")

# 写入文件
write_graph_to_file(G1, "Dgraph_results_100_min_70.txt", mode='w')  # 写入 G1，覆盖模式
write_graph_to_file(G2, "Dgraph_results_100_min_70.txt", mode='a')  # 写入 G2，追加模式

# print("结果已写入文件 graph_results.txt")

G3 = nx.Graph()  # 创建新图 G3
for u, v in G1.edges():
    weight_G1 = G1[u][v]['weight']
    weight_G2 = G2[u][v]['weight']
    G3.add_edge(u, v, weight=weight_G1 + weight_G2)  # 权重相加
    
final_matrix = nx.to_numpy_array(G3, weight='weight')

# 输出邻接矩阵
print("G3 的邻接矩阵:")
print(final_matrix)

res = 0
W_E = 0
for i in range(n):
    for j in range(i + 1, n):
        W_E += final_matrix[i][j]
        for k in range(j + 1, n):

            if final_matrix[i][j] != 0 and final_matrix[i][k] != 0 and final_matrix[j][k] !=0:
                res += min(min(final_matrix[i][j], final_matrix[i][k]), final_matrix[j][k])
                #  res += max(max(final_matrix[i][j], final_matrix[i][k]), final_matrix[j][k])
                # res += (final_matrix[i][j] + final_matrix[i][k] + final_matrix[j][k]) / 3
                # res += 1
                # T = T + 1

with open("Dgraph_results_100_min_detRes_70.txt", 'w') as f:
    f.write(f"{res}\n")
    f.write(f"{W_E}\n")
print(res)
print(W_E)
print(W_E * (n - 2) / res)

# print(W_E / res)
# print(1200 / T)
import math
import random
import datetime

class L1Sampler:
    def __init__(self, data):
        """
        初始化 L1 Sampler。
        :param data: 一个字典，键是数据项，值是权重（或频率）。
        """
        self.data = data
        self.total_weight = sum(data.values())  # L₁范数总和

    def sample(self):
        """
        从数据流中进行加权采样，返回一个样本。
        """
        # 生成一个随机数，范围是[0, total_weight]
        rand_value = random.uniform(0, self.total_weight)

        # 从数据中按权重进行采样
        cumulative_weight = 0
        for item, weight in self.data.items():
            cumulative_weight += weight
            if rand_value <= cumulative_weight:
                return item
        return None  # 如果没有返回，则出错


# 示例数据流（例如，可以是不同网页或单词的频率）
def read_adjacency_from_file(filename):
    adj_dict = {}

    # 读取文件并逐行处理
    with open(filename, 'r') as f:
        for line in f:
            u, v, weight = line.strip().split()
            u, v, weight = int(u), int(v), int(weight)

            # 使边是无向的，确保边的顺序不影响字典键
            edge = tuple(sorted((u, v)))

            # 如果边已存在，则累加权重，否则添加新边
            if edge in adj_dict:
                adj_dict[edge] += weight
            else:
                adj_dict[edge] = weight

    return adj_dict

# 读取邻接链表并转化为字典
filename = 'Dgraph_results_150_max.txt'  # 文件路径
adjacency_dict = read_adjacency_from_file(filename)


# 输出转换后的字典
# for edge, weight in adjacency_dict.items():
#     print(f"Edge {edge}: {weight}")
# print(len(adjacency_dict))

# 创建 L₁ Sampler 实例
l1_sampler = L1Sampler(adjacency_dict)
# print(l1_sampler.total_weight)
epsilon = 0.1
delta = 0.01
n = 150
t = math.ceil(27 / epsilon**2 * 0.2 * (n - 2)  * math.log(2 / delta, 2))
print(t)

print(datetime.datetime.today())
# 进行加权采样
samples = [l1_sampler.sample() for _ in range(t)]

print(datetime.datetime.today())
res = 0
# index = 0
for edge in samples:
    # print("Complete", index / t, "%")
    l = tuple([-1,-1])
    r = tuple([-1,-1])
    lWeight = 0
    rWeight = 0
    w = random.randint(0, n - 1)
    minWeight = adjacency_dict[edge]
    if minWeight == 0:
        continue
    while w == edge[0] or w == edge[1]:
        w = random.randint(0, n - 1)
    with open(filename, 'r') as f:
        for line in f:
            u, v, weight = line.strip().split()
            u, v, weight = int(u), int(v), int(weight)
            if l == tuple([u,v]):
                lWeight += weight
                continue
            if r == tuple([u,v]):
                rWeight += weight
                continue
            if (u == edge[0] and w == v) or (u == w and v == edge[0]):
                l = tuple([u,v])
                lWeight = weight
            if (u == edge[1] and w == v) or (u == w and v == edge[1]):
                r = tuple([u,v])
                rWeight = weight
    if l != tuple([-1,-1]) and r != tuple([-1,-1]) and lWeight != 0 and rWeight != 0 and minWeight == max(max(lWeight, rWeight), minWeight):
        res += 1
    # index +=1
# and minWeight == max(max(lWeight, rWeight), minWeight)
# print(res / t)
# print(W_Delta / l1_sampler.total_weight / (n - 2))
res = res * l1_sampler.total_weight * (n - 2) / t
with open("Dgraph_results_150_max_ranRes.txt",'w') as f:
    f.write(f"{res}\n")
print(res)
print(datetime.datetime.today())

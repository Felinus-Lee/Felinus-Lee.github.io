# 邻接表表示的图
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

# 打印邻接表
for node, neighbors in graph.items():
    print(f" {node} : {neighbors}")

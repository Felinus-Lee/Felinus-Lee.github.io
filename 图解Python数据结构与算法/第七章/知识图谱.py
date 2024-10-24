import networkx as nx

# 创建一个有向图，用于表示知识图谱
class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # 有向图

    def add_entity(self, entity):
        """添加一个实体到知识图谱"""
        self.graph.add_node(entity)
    
    def add_relationship(self, entity1, entity2, relationship):
        """添加一个关系到知识图谱"""
        self.graph.add_edge(entity1, entity2, relationship=relationship)
    
    def remove_entity(self, entity):
        """从知识图谱中删除一个实体"""
        self.graph.remove_node(entity)
    
    def remove_relationship(self, entity1, entity2):
        """删除两个实体之间的关系"""
        self.graph.remove_edge(entity1, entity2)
    
    def find_relationships(self, entity):
        """查询与某个实体相关的所有关系"""
        relationships = []
        for neighbor in self.graph.neighbors(entity):
            relationships.append((entity, neighbor, self.graph[entity][neighbor]['relationship']))
        return relationships

    def print_graph(self):
        """打印当前的知识图谱"""
        for node in self.graph.nodes:
            print(f"Entity: {node}")
        for edge in self.graph.edges(data=True):
            print(f"Relationship: {edge[0]} -> {edge[1]}, {edge[2]['relationship']}")

# 示例使用
kg = KnowledgeGraph()

# 添加实体
kg.add_entity("Alice")
kg.add_entity("Bob")
kg.add_entity("Company")

# 添加关系
kg.add_relationship("Alice", "Bob", "is_friend")
kg.add_relationship("Alice", "Company", "works_at")
kg.add_relationship("Bob", "Company", "works_at")

# 打印知识图谱
kg.print_graph()

# 查询实体的所有关系
print("\nRelationships for Alice:")
print(kg.find_relationships("Alice"))

# 删除一个关系
kg.remove_relationship("Alice", "Bob")

# 打印知识图谱
print("\nGraph after removing relationship between Alice and Bob:")
kg.print_graph()

# 删除一个实体
kg.remove_entity("Bob")

# 打印知识图谱
print("\nGraph after removing Bob:")
kg.print_graph()

import networkx as nx

class CourseKnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # 使用有向图表示
    
    def add_entity(self, entity):
        """添加一个实体到知识图谱"""
        self.graph.add_node(entity)
    
    def add_relationship(self, entity1, entity2, relationship):
        """添加一个关系到知识图谱"""
        self.graph.add_edge(entity1, entity2, relationship=relationship)
    
    def print_graph(self):
        """打印当前的知识图谱"""
        for node in self.graph.nodes:
            print(f"Entity: {node}")
        for edge in self.graph.edges(data=True):
            print(f"Relationship: {edge[0]} -> {edge[1]}, {edge[2]['relationship']}")
    
    def find_relationships(self, entity):
        """查询与某个实体相关的所有关系"""
        relationships = []
        for neighbor in self.graph.neighbors(entity):
            relationships.append((entity, neighbor, self.graph[entity][neighbor]['relationship']))
        return relationships

# 初始化知识图谱
kg = CourseKnowledgeGraph()

# 添加课程实体
kg.add_entity("Data Structures")  # 数据结构
kg.add_entity("Operating Systems")  # 操作系统

# 添加教授实体
kg.add_entity("Professor Zhang")  # 张教授
kg.add_entity("Professor Li")  # 李教授

# 添加教材实体
kg.add_entity("Introduction to Algorithms")  # 算法导论
kg.add_entity("Operating System Concepts")  # 操作系统概念

# 添加学生实体
kg.add_entity("Student Wang")  # 王同学
kg.add_entity("Student Li")  # 李同学

# 添加关系
kg.add_relationship("Professor Zhang", "Data Structures", "teaches")
kg.add_relationship("Professor Li", "Operating Systems", "teaches")
kg.add_relationship("Data Structures", "Introduction to Algorithms", "uses")
kg.add_relationship("Operating Systems", "Operating System Concepts", "uses")
kg.add_relationship("Operating Systems", "Data Structures", "requires")
kg.add_relationship("Student Wang", "Data Structures", "enrolled_in")
kg.add_relationship("Student Li", "Operating Systems", "enrolled_in")

# 打印知识图谱
kg.print_graph()

# 查询课程的相关信息
print("\nRelationships for Data Structures:")
print(kg.find_relationships("Data Structures"))

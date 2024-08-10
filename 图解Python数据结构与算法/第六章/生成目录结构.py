import os

def generate_directory_structure(path):
    structure = []
    
    def traverse(current_path, level):
        if os.path.isdir(current_path):
            structure.append("  " * level + os.path.basename(current_path) + "/")
            for entry in os.listdir(current_path):
                traverse(os.path.join(current_path, entry), level + 1)
        else:
            structure.append("  " * level + os.path.basename(current_path))
    
    traverse(path, 0)
    return structure

# 生成目录结构图示
structure = generate_directory_structure('test_dir')
for line in structure:
    print(line)

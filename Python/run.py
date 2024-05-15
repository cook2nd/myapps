import yaml
 
# 读取YAML文件
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(e)
 
# 写入YAML文件
def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
 
# 示例YAML文件的路径
yaml_file_path = 'example.yaml'
 
# 读取YAML文件
data = read_yaml(yaml_file_path)
print(data)
 
# 修改YAML数据
data['key'] = 'updated value 999'
 
# 写入修改后的YAML数据到文件
write_yaml(yaml_file_path, data)
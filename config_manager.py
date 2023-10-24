import logging
import os
import argparse
import yaml

# 填入 SYSTEM_CONFIG 路径
SYSTEM_CONFIG = ""

logging.basicConfig(level=logging.INFO)


def parse_task():
    """读取 任务名称
    Returns:
        str: task_name
    """    
    parser = argparse.ArgumentParser()
    parser.add_argument("task_name", type=str, default="DEFAULT_TASK_NAME")
    task_name = parser.parse_args().task_name
    return task_name


def get_date():
    from datetime import datetime
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%m_%d_%H_%M")
    return formatted_datetime


def load_yaml(file_path):
    with open(file_path, 'r') as fin:
        result = yaml.load(fin.read(), Loader=yaml.FullLoader)
    return result

def load_task_yaml():
    """读取当前任务的 config

    Returns:
        dic: 包含全部参数的 dict
    """

    task_name = parse_task()
    logging.info(f"Reading task args {task_name}")
    task_arguments_path = load_yaml(SYSTEM_CONFIG)
    
    # Load base_arguments.yaml
    base_argments = load_yaml(task_arguments_path['bask_arguments'])
    
    # Load MODEL_base.yaml

    # Load TASK.yaml
    modified_arguments = load_yaml(task_arguments_path[task_name])
    base_argments.update(modified_arguments)

    print(base_argments)

    formatted_datetime = get_date() 

    if base_argments['output_path'] != "base_config":
        base_argments['output_path'] = os.path.join(base_argments['output_path'], base_argments['task_name'] + "_" + formatted_datetime)
    
        output_folder = base_argments['output_path']
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"创建 Prediction: {output_folder}")
        else:
            print(f"Predicton 文件夹 '{output_folder}' 已经存在")

    if base_argments['checkpoints'] != "base_config":
        base_argments['checkpoints'] = os.path.join(base_argments['checkpoints'], base_argments['task_name'] + "_" + formatted_datetime)
        output_folder = base_argments['checkpoints']
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"创建 Checkpoints: {output_folder}")
        else:
            print(f"Checkpoints 文件夹 '{output_folder}' 已经存在")

    return base_argments


def update_task_index(task_name, new_config):
    """更新 SYSTEM_CONFIG,添加新配置文件
    Args:
        task_name (str): _description_
        new_config (str): _description_
    """
    system_arguments = yaml.load(open(SYSTEM_CONFIG, 'r').read(), Loader=yaml.FullLoader)
    if task_name in system_arguments:
        logging.warning(f"{task_name} has been in the config.")
        while 1:
            overload = input("输入 y 覆盖, 输入其他退出")
            if overload == 'y' or overload == "Y":
                system_arguments[task_name] = new_config
                print(f"{task_name} 的配置文件已更新为: {new_config}")
            break
    else:
        system_arguments[task_name] = new_config
    with open(SYSTEM_CONFIG, 'w') as fout:
        yaml.dump(system_arguments, fout)
    

if __name__ == "__main__":
    """Main 函数仅用于测试
    """
    print(load_task_yaml("parser_glm2_5shot"))
    
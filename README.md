# 🐱Config_Cat

通过 ``Task``管理配置/模型/输出/日志，每一组训练对应一个 ``Task``。训练/预测前提前写好配置文件，任务开始时用任务名调用，程序读取参数，然后进行其他的配置操作。

## 🖇参数结构

* SYSTEM_CONFIG: 记录所有任务对应的配置文件的路径
* base_arguments.yaml: 基本配置, 维护所有缺省值
* task_name.yaml: 任务对应的配置文件, 文件名为任务名

## ✅已完成功能

* 读配置
  * 读取过程中, 先根据base_config读入缺省参数,之后读入任务定制参数.
  * 可以根据不同的任务建立不同的base_config.
* 增加配置文件
  * 更新 SYSTEM_CONFIG
  * 重复内容做检查, 更新提醒

## 📄使用方法

```python
from config_manager import load_task_yaml

# 读取参数
args = load_task_yaml()

# 更新SYSTEM_CONFIG
from config_manager import update_task_index
update_task_index(NEW_TASK_NAME, NEW_CONFIG_PATH)

```

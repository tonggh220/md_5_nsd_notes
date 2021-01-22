import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# 配置选项
# connection表示连接方式，可以使用local进行本地执行
# 也可以使用ssh远程连接执行，也可以使用smart自动判断
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# Dataloader负责查找并解析ini/yaml/json文件，将其转换成python可以识别的数据类型
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 主机清单文件的配置。有两种方法，一种是用逗号隔开各个主机名；
# 另一种方法是使用主机清单文件
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 准备执行任务时需要的数据源
play_source = dict(
    name="Ansible Play",
    hosts='webservers',  # 在哪些主机上执行任务
    gather_facts='no',   # 是否收集facts变量
    tasks=[  # 要执行的具体的任务
        # 执行任务，将结果保存到名为shell_out的变量中
        dict(action=dict(module='user', args='name=alice state=present'), register='shell_out'),
        # 通过debug模块将前一任务的结果输出
        dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
    ]
)
# 将上面的资源整合成play
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
# 通过任务队列管理器调度执行任务
tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
    )
    result = tqm.run(play)  # most interesting data for a play is actually sent to the callback's methods
finally:
    if tqm is not None:
        tqm.cleanup()

    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# Options用于设置执行选项
# connection用于设置连接方式，local表示本机执行，ssh表示远程连接执行
# smart表示智能判断，一般也是使用ssh
# forks用于设置同时在多少台主机上执行任务
# become, become_xxx用于在远程主机提权
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# DataLoader负责查找和读取yaml、json和ini文件，并把它们转成python的数据类型
loader = DataLoader()
# 保存各种密码
passwords = dict(vault_pass='secret')

# 主机清单，有两种表示方法，一种是将所有主机字符串用逗号分隔
# 另一种是使用主机清单文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# 设置变量
variable_manager = VariableManager(loader=loader, inventory=inventory)
# 配置play所需要的源数据
play_source = dict(
    name="Ansible Play",  # play的名字
    hosts='webservers',   # 在哪些主机上执行任务
    gather_facts='no',    # 不通过setup收集远程主机信息
    tasks=[
        dict(action=dict(module='shell', args='id root'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)
# 创建play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
# 通过任务对象管理器调度任务
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

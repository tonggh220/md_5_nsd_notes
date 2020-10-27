import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 命令选项。connection可用的值有local表示本地执行，有ssh表示远程登陆执行，有smart表示智能判断
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# DataLoader负责查找和读取yaml，json和ini文件并转换成Python能识别的格式
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 主机清单，有两种实现方式。一种是使用主机清单文件列表，另一种方式，是将所有的主机通过逗号进行分隔，组成一个字符串
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# 用于处理变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建表示我们的工作（包括任务）的数据结构，这基本上是我们的yaml加载程序在内部执行的操作。
play_source = dict(
    name="Ansible Play",
    hosts='webservers',  # 在哪些主机上执行任务
    gather_facts='no',
    tasks=[
        dict(action=dict(module='user', args='name=jerry state=absent'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
    ]
)

# 创建play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 运行play
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
    # 清理
    if tqm is not None:
        tqm.cleanup()

    # 删除临时目录
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

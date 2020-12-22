import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# 设置选项connection是连接方式，local表示本机执行，ssh表达远程连接执行，smart表示自动选择
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)
# options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# DataLoader()负责查找和读取yaml，json和ini文件，并表示成python可以识别的数据结构
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 创建主机清单，使用路径将配置文件作为源或以逗号分隔的字符串作为主机
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器负责合并所有不同的源，以便为您提供每种情况下可用变量的统一视图
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建代表我们的工作（包括任务）的数据结构，这基本上是我们的YAML加载程序在内部执行的操作。
play_source = dict(
    name="Ansible Play",
    hosts='webservers',  # 在哪些主机上执行任务
    gather_facts='no',
    tasks=[
        # 将命令的输出注册到名为shell_out的变量里，再用debug输出
        dict(action=dict(module='user', args='name=bob state=absent'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
    ]
)

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
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
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

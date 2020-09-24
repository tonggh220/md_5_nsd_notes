import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# ansible命令选项。connection是连接主机的方式，local表示本地执行，ssh表示ssh到主机执行，
# smart表示智能判断，通常也是ssh
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# Dataloader负责读取yaml/ini/json格式的文件，并将其转换成python能够识别的形式
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 创建清单，使用路径将配置文件作为源或以逗号分隔的字符串作为主机
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器负责合并所有不同的源，以便为您提供每种情况下可用变量的统一视图
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建代表我们的工作（包括任务）的数据结构，这基本上是我们的YAML加载程序在内部执行的操作。
play_source = dict(
    name="Ansible Play",
    hosts='dbservers',  # 在哪些主机上执行任务
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
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

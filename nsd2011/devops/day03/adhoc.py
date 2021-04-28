import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# connection指的是连接方式，取值有：local表示本地执行，ssh表示远程执行，smart表示自动选择
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)
# options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# 负责查找和读取yaml，json和ini文件
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 主机清单。有两种方式，一种是使用逗号将所有主机分隔的字符串；另一种是主机清单文件列表
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建代表我们的工作（包括任务）的数据结构，这基本上是我们的YAML加载程序在内部执行的操作。
play_source = dict(
    name="Ansible Play",   # 任务名
    hosts='dbservers',     # 目标主机
    gather_facts='no',     # 不收集facts变量
    tasks=[
        dict(action=dict(module='user', args='name=tom state=absent'), register='output'),
        dict(action=dict(module='debug', args=dict(msg='{{output}}')))
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

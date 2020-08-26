import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# 选项，大多都不用关心，需要了解的有connection
# connection的值有local，表示本机执行；ssh表示远程ssh执行；smart表示智能判断，通常也是ssh
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# Dataloader负责查找读取ini/yaml/json格式的文件，并将其转换为python的数据类型
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 主机清单文件，有两种方式。一种是主机清单文件列表，另一种方式是用逗号将所有的主机串连
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')
# 变量管理器，负责统一管理变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# play源
play_source = dict(
    name="Ansible Play",
    hosts='webservers',  # 在哪些主机上执行任务
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='id root'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)

# 创建Play
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 通过任务队列管理器运行Play
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

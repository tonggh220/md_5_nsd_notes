import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# 设置选项。其中connection是连接类型。local表示本机执行，ssh表示远程登陆执行，smart表示智能选择，一般也会选为ssh
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# Dataloader用于查找并将ini/yaml/json等文件内容转为python可以识别的数据类型
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 主机清单。可以使用逗号将各个主机分开，也可以采用主机清单文件
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器，分析变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建用于执行命令的、构成play的源
play_source = dict(
    name="Ansible Play",  # play名字
    hosts='webservers',   # 在哪些主机上执行任务
    gather_facts='no',
    tasks=[  # 使用哪个模块，执行哪些任务
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
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

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# 为ansible设置默认选项
# connection是连接方式。local表示本地执行；ssh表示远程连接服务器执行；smart表示智能选择
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# Dataloader用于读取、分析json/yaml/ini文件，把它们表示成python能识别的数据类型
loader = DataLoader()
passwords = dict(vault_pass='secret')

# 主机清单。有两个实现方式，一个是使用逗号分隔所有的主机；另一个方式是使用主机清单文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,192.168.1.11')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)
# 创建play源
play_source = dict(
    name="Ansible Play",  # play名
    hosts='dbservers',  # 在哪些主机上执行命令
    gather_facts='no',  # 不收集facts信息
    tasks=[
        dict(action=dict(module='user', args='name=bob state=present'), register='shell_out'),
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

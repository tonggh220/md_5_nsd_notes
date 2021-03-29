import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# ansible adhoc选项。connection是连接方式，可以设置为local表示本地执行，ssh表示ssh执行，smart表示自动选择，一般也会选择ssh
# forks表示多少台机器分成一批，执行命令
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)
# options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# loader负责分析ini/yaml/json等格式的文件，并将其转换成python可以识别的形式
loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
# vault password
passwords = dict(vault_pass='secret')

# 主机清单，可以将所有被管的主机用逗号分隔，形成字符串
# 也可以使用主机清单文件
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])
# inventory = InventoryManager(loader=loader, sources='localhost,')

# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 将收集的信息组合成一个Play
play_source = dict(
    name="Ansible Play",
    hosts='webservers',   # 在哪些主机上执行任务
    gather_facts='no',   # 不收集facts变量
    tasks=[              # 在目标主机上执行的任务
        dict(action=dict(module='user', args='name=tom state=present'), register='result'),
        dict(action=dict(module='debug', args=dict(msg='{{result}}')))
    ]
)
# 整合上述配置资源，形成Play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 通过任务队列管理器运行它
tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
    )
    result = tqm.run(play)
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

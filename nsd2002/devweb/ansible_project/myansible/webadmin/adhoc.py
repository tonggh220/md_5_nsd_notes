import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc(sources, targets, module, params):
    # connections有三种连接方式，分别是local / ssh / smart
    # local: 本地执行; ssh: ssh到目标主机执行; smart: 自动选择，一般也是ssh
    # forks是一次在多少台主机上并行执行命令
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    # DataLoader负责查找并将yaml, json, ini文件内容转换成python可以识别的数据对象
    loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
    passwords = dict(vault_pass='secret')

    # 主机清单文件，有两种写法，一种是将被管理的主机使用逗号分隔构成一个字符串
    # 另一种写法是使用主机清单文件名列表
    # inventory = InventoryManager(loader=loader, sources='localhost,')
    inventory = InventoryManager(loader=loader, sources=sources)
    # 分析主机清单文件的变量
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # 创建play源
    play_source = dict(
        name="Ansible Play",  # play名字
        hosts=targets,  # 在哪些主机上执行命令
        gather_facts='no',  # 是否收集facts变量
        tasks=[  # 通过模块，执行任务
            dict(action=dict(module=module, args=params), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
        ]
    )

    # 创建play对象
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # 通过任务队列管理器执行play
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
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

if __name__ == '__main__':
    adhoc(['myansible/hosts'], 'webservers', 'user', 'name=tom state=absent')

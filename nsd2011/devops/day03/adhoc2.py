import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc(host_files, hosts, module, args):
    # connection指的是连接方式，取值有：local表示本地执行，ssh表示远程执行，smart表示自动选择
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    # 负责查找和读取yaml，json和ini文件
    loader = DataLoader()
    passwords = dict(vault_pass='secret')
    # 主机清单。有两种方式，一种是使用逗号将所有主机分隔的字符串；另一种是主机清单文件列表
    inventory = InventoryManager(loader=loader, sources=host_files)
    # 变量管理器
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    # 创建代表我们的工作（包括任务）的数据结构，这基本上是我们的YAML加载程序在内部执行的操作。
    play_source = dict(
        name="Ansible Play",   # 任务名
        hosts=hosts,     # 目标主机
        gather_facts='no',     # 不收集facts变量
        tasks=[
            dict(action=dict(module=module, args=args), register='output'),
            dict(action=dict(module='debug', args=dict(msg='{{output}}')))
        ]
    )
    # 创建play对象
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    # 通过任务队列管理器执行任务
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
        # 清理产生的临时文件等无用资源
        if tqm is not None:
            tqm.cleanup()
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

if __name__ == '__main__':
    adhoc(['myansible/hosts'], 'dbservers', 'user', 'name=tom state=present')

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc(sources, hosts, module, args):
    # ansible命令选项。connection是连接主机的方式，local表示本地执行，ssh表示ssh到主机执行，
    # smart表示智能判断，通常也是ssh
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    # Dataloader负责读取yaml/ini/json格式的文件，并将其转换成python能够识别的形式
    loader = DataLoader()
    passwords = dict(vault_pass='secret')

    # 创建清单，使用路径将配置文件作为源或以逗号分隔的字符串作为主机
    inventory = InventoryManager(loader=loader, sources=sources)

    # 变量管理器负责合并所有不同的源，以便为您提供每种情况下可用变量的统一视图
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # 创建代表我们的工作（包括任务）的数据结构，这基本上是我们的YAML加载程序在内部执行的操作。
    play_source = dict(
        name="Ansible Play",
        hosts=hosts,  # 在哪些主机上执行任务
        gather_facts='no',
        tasks=[
            dict(action=dict(module=module, args=args), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
        ]
    )

    # 创建播放对象，剧本对象使用.load代替init或新方法，
    # 这还将根据play_source中提供的信息自动创建任务对象
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # 运行它-实例化任务队列管理器，它负责分叉和设置所有对象以遍历主机列表和任务
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

if __name__ == '__main__':
    adhoc(['myansible/hosts'], 'dbservers', 'user', 'name=tom state=absent')
    # adhoc(['myansible/hosts'], 'dbservers', 'user', 'name=tom state=present')

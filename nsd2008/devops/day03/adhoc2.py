import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc(host_files, hosts, module, args):
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict(vault_pass='secret')
    inventory = InventoryManager(loader=loader, sources=host_files)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",
        hosts=hosts,  # 在哪些主机上执行任务
        gather_facts='no',   # 是否收集facts变量
        tasks=[  # 要执行的具体的任务
            dict(action=dict(module=module, args=args), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
        ]
    )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

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
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

if __name__ == '__main__':
    host_files = 'myansible/hosts'
    hosts = 'webservers'
    module = 'user'
    args = 'name=alice state=absent'
    adhoc(host_files, hosts, module, args)


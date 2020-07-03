import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc(sources=None, hosts=None, module=None, args=None):
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict(vault_pass='secret')
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",  # play的名字
        hosts=hosts,   # 在哪些主机上执行任务
        gather_facts='no',    # 不通过setup收集远程主机信息
        tasks=[
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
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

if __name__ == '__main__':
    inventory = ['myansible/hosts']
    hosts = 'dbservers'
    module = 'user'
    # args1 = 'user=tom state=present'
    # adhoc(inventory, hosts, module, args1)
    args2 = 'user=tom state=absent'
    adhoc(inventory, hosts, module, args2)

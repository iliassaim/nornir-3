from nornir import InitNornir
from nornir_scrapli.tasks.core import send_configs 
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file = 'config.yaml')
def push_config(task):
    task.run (task=send_configs, configs=[
        'banner motd %ILYES%'
        'ntp server 192.168.1.1',
        'no router ospf 1'
    ])
results = nr.run(task = push_config)
print_result(results)
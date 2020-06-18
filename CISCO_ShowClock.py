
import netmiko
import json
from config_file import host_conf


#Passing dictonaries to NetMiko

r1 = {
        'ip': '192.168.1.97',
        'device_type': 'cisco_ios',
        'username': 'mawood',
        'password': 'kim123'
        }

r2 = {
        'ip': '192.168.1.254',
        'device_type': 'cisco_ios',
        'username': 'mawood',
        'password': 'kim123'
        }

"""s1 = {
        'ip': '192.168.1.97',
        'device_type': 'cisco_ios',
        'username': 'mawood',
        'password': 'kim123'
        }
"""
devices = [r1, r2]

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)


for device in devices:
    try:
        print ('-'*79)
        print {'Connecting to device', device['ip']}
        connection  = netmiko.ConnectHandler(**device)
        #connection.enable()
        #connection.send_command('enable')
        output = ''
        for command in host_conf:
            print(command)
            output += connection.send_command(command, delay_factor=2)
            print(output)
        #print(connection.send_command('show clock'))      
        #print(connection.send_command('clock set 10:53:00 6 JUNE 2020'))
        #print(connection.send_command('show clock'))
        connection.disconnect()
    except Exception as e:
        print('Failed to ', device['ip'], e)
        


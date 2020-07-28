from netmiko import ConnectHandler
from getpass import getpass
device1 = {
            "host": 'cisco3.lasthop.io',
            "username": 'pyclass',
            "password": getpass(),
            "device_type": 'cisco_ios',
            "session_log" : 'seesion.txt',
}
netconnect = ConnectHandler(**device1)
print(netconnect.find_prompt())
output = netconnect.send_command("sh ip arp")
print(output)


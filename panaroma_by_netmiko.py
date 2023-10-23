from netmiko import ConnectHandler


PaloAlto_Panorama ={
                        "device_type": "paloalto_panos",
                        'ip': 'ip_of_Device',
                        'username': 'username',
                        'password': 'password'
}
 # For multiple commands we pass command in 'list'
 # e.g. my_command =['','',''];

#  ConnectHandler estb. ssh connection with device
pan_connect = ConnectHandler(**PaloAlto_Panorama)

#TO pass list we use Send_config_set() command and to pass ingle command use send_command.

# expect_string helps to wait until complete output

output = pan_connect.send_command('show system info', expect_string=r">")
pan_connect.disconnect()

with open(r'F:\Fakepath\panos.txt', 'a') as f:
    f.write(output)
    f.close()

print(output)



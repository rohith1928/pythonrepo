from pynet_cisco import ConnectHandler
CSR= {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "port":22,
    "username":"developer",
    "password":"C1sco12345"
}
net_connect=ConnectHandler(**CSR)
hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname, device, *rest = hostname.split(" ")
print("backing up" +device)
filename = "C:/Users/user702/PycharmProjects/pythonProject/device04.txt"
showrun = net_connect.send_command('show run')
showvlan =net_connect.send_command('show ver')
showver = net_connect.send_command('show ver')
log_file= open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
net_connect.disconnect()
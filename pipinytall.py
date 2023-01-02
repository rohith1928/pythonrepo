import ifaddr
adapters = ifaddr.get_adapters(include_unconfigured= True)
for adapter in adapters:
    print("IP of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print(" %s/%s" %(ip.ip,ip.network_prefix))
    else:
        print(" no ips configured")
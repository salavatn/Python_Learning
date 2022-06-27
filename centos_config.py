from jinja2 import Environment, FileSystemLoader, Template


my_file_loader = FileSystemLoader('venv/Linux/LinuxConfig')
my_env = Environment(loader=my_file_loader)


# centos_ip_address = input("Enter IP address:\t")
# centos_mask_length = input("Enter Mask length:\t")
# centos_default_gateway = input("Enter Default Gateway:\t")
# centos_dns_address = input("Enter DNS address:\t")


centos_ip_address = "172.30.0.145"
centos_mask_length = "24"
centos_default_gateway = "172.30.0.1"
centos_dns_address = "77.88.8.8"

template_LinuxNetworkConfig = my_env.get_template('Linux_Config.txt')
msg1 = template_LinuxNetworkConfig.render(set_ip_address = centos_ip_address,
                                   set_mask_prefix = centos_mask_length,
                                   set_gateway_address = centos_default_gateway)


template_LinuxDNSConfig = my_env.get_template('Linux_Config_DNS.txt')
msg2 = template_LinuxDNSConfig.render(set_dns_address = centos_dns_address)



print("CentOS network configuration:", msg1, msg2, sep="\n")
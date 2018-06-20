import ansible_runner

#raw data
ip_1 = '192.168.122.158'
ip_2 = '192.168.122.18'
ip_3 = '192.168.122.145'

#create ip list from raw data
ip_list = []
ip_list.append(ip_1)
ip_list.append(ip_2)
ip_list.append(ip_3)

#create ips dict from list of ips
ip_dict = {}
for i in ip_list:
    ip_dict[i] = ''

#create hosts from ips
hosts = {}
hosts['hosts'] = ip_dict

#creat test group and fill with hosts
inventory = {}
inventory['test'] = hosts

#run playbook wiht inventory
r = ansible_runner.run(private_data_dir = '/home/dpivonka/Documents/ansible_runner_testing/ansible',
                       playbook = 'main.yml',
                       inventory = inventory)

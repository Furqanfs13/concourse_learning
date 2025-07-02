with open('ip_list.txt', 'r') as file:
    ips = [line.strip() for line in file.readlines()]

print(f'My name is {ips[0]}')
print(f'I am a {ips[1]}')
print(f'I work at {ips[2]}')
print(f'From {ips[3]}')

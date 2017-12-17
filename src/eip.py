import json

data = json.load(open('confeip.json'))
with open('/home/ec2-user/SQLConfig.conf', 'a') as f:
    f.write(data['Addresses'][0]['PublicIp'])

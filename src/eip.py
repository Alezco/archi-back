import json

data = json.load(open('/home/ec2-user/archi-back/src/confeip.json'))
with open('/home/ec2-user/SQLConfig.conf', 'a') as f:
    f.write(data['Addresses'][0]['PublicIp'])

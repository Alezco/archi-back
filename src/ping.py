import subprocess
import os
import time
import Constants

for i in range(0, 10000):
    time.sleep(5)
    result = subprocess.Popen(["ping","-c", "1", Constants.HOST]).wait()
    if not result:
        print("active")
    else:
        print("inactive")
        result2 = subprocess.Popen(['/home/ec2-user/passToMaster'], shell=True, executable="/bin/bash")
        result3 = subprocess.Popen(['/home/ec2-user/stopSlave'], shell=True, executable="/bin/bash")
        break

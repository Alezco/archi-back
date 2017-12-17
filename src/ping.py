import subprocess
import os
import time
import Constants

for i in range(0, 100):
    time.sleep(5)
    result = subprocess.Popen(["ping","-c", "1", Constants.HOST]).wait()
    if not result:
        print("active")
    else:
        print("inactive")

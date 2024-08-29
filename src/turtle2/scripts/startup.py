#!/usr/bin/env python3
import subprocess
import time
subprocess.Popen(['rosrun','turtle2','window.py'])
subprocess.Popen(['rosrun','turtle2','control.py'])
time.sleep(0.7)
subprocess.Popen(['rosrun','turtle2','node.py']).wait()

  

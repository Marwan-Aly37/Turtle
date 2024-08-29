#!/usr/bin/env python3
import subprocess
import time
subprocess.Popen('roscore')
subprocess.Popen(['rosrun','turtle2','window.py'])
subprocess.Popen(['rosrun','turtle2','control.py'])
time.sleep(1)
subprocess.Popen(['rosrun','turtle2','node.py']).wait()

  

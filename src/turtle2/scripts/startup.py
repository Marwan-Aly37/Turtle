#!/usr/bin/env python3
import subprocess
import time
subprocess.Popen(['rosrun','turtle2','window.py'])
time.sleep(1)
subprocess.Popen(['rosrun','turtle2','node.py']).wait()

  
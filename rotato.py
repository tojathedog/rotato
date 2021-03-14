#!/usr/bin/env python3
#
# rotato -  rotate my ssh keys because i am a lazy dog
#
# tojathedog 🐶

import sys
import os
import subprocess
import time

poptime=time.strftime("%m-%d-%y-%I-%M")

subprocess.run(["ssh-keygen", "-q", "-N''", "-b 4096", "-ftest-" + poptime])

os.chmod("test-" + poptime, 0o600)
os.chmod("test-" + poptime + ".pub", 0o600)


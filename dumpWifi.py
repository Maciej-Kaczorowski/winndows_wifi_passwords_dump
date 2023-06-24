#!/bin/python3

import subprocess
import re

cmd = "netsh wlan show profiles"

returned_output = subprocess.check_output(cmd)

pattern = r"All User Profile\s+:\s+(.*?)\\r\\n";
profiles = re.findall(pattern, str(returned_output), flags=re.M)

for profile in profiles:
    cmd = "netsh wlan show profiles name=\"" + profile + "\" key=clear"
    returned_output = subprocess.check_output(cmd)
    pattern = r"Key Content\s+:\s+(\w+)"
    password = re.findall(pattern, str(returned_output))
    print(profile, password)

import os
import sys
import subprocess

TARGET = "/tmp/python_packages"

os.makedirs(TARGET, exist_ok=True)

# Make packages installed into /tmp importable
if TARGET not in sys.path:
    sys.path.insert(0, TARGET)

# Install requirements into /tmp
subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "--target",
    TARGET,
    "-r",
    "requirements.txt",
])

# Example imports
import requests
import socketio

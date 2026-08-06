import os
import sys
import subprocess

REPO_URL = "https://github.com/yawnerss/livtrmnlasdasd.git"
REPO_DIR = "/tmp/livtrmnlasdasd"
PKG_DIR = "/tmp/python_packages"

os.makedirs(PKG_DIR, exist_ok=True)

env = os.environ.copy()
env["PYTHONPATH"] = PKG_DIR + os.pathsep + env.get("PYTHONPATH", "")

# Clone or update the repository
if not os.path.exists(REPO_DIR):
    subprocess.check_call([
        "git",
        "clone",
        REPO_URL,
        REPO_DIR
    ])
else:
    subprocess.check_call([
        "git",
        "-C",
        REPO_DIR,
        "pull"
    ])

# Install requirements into /tmp/python_packages
subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "--target",
    PKG_DIR,
    "-r",
    os.path.join(REPO_DIR, "requirements.txt")
])

# Change into the repository
os.chdir(REPO_DIR)

# Run client.py using the installed packages
subprocess.check_call(
    [sys.executable, "client.py"],
    env=env
)

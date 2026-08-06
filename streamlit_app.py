import subprocess
import sys
import importlib

packages = {
    "requests": "requests",
    "socketio": "python-socketio"
}

for module_name, package_name in packages.items():
    try:
        importlib.import_module(module_name)
        print(f"[✓] {package_name} is already installed.")
    except ImportError:
        print(f"[+] Installing {package_name}...")
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            package_name
        ])
        print(f"[✓] {package_name} installed successfully.")

print("\nAll required modules are ready!")

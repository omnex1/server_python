import subprocess, sys

process = subprocess.Popen([sys.executable, "-m", "pip", "install", "streamlit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

def Print(value):
    print(f"{__file__} --- {value}")

stdout, stderr = process.communicate()

Print("start")
Print(stdout.decode())
Print(stderr.decode())
Print("end")
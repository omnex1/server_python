import subprocess, sys, os

os.system("clear")

def Print(value):
    print(f"{__file__} --- {value}")

Print("start")

process = subprocess.Popen([sys.executable, "-m", "pip", "install", "streamlit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

stdout, stderr = process.communicate()


Print(stdout.decode())
Print(stderr.decode())
Print("end")
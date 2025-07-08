import subprocess
process = subprocess.Popen(["pip", "install", "streamlit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def Print(value):
    print(f"{__file__} --- {value}")

stdout, stderr = process.communicate()

Print("start")
Print(stdout.decode(), stderr.decode())
Print("end")
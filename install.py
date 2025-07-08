import subprocess
process = subprocess.Popen(["pip", "install", "streamlit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

stdout, stderr = process.communicate()

print(stdout.decode(), stderr.decode())
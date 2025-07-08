import subprocess
process = subprocess.Popen("pip", "install", "streamlits", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

stdout, stderr = process.communicate()
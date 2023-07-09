import os
import subprocess

# Get the directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change directory to the script's directory
os.chdir(script_dir)

# Close all cmd windows
subprocess.Popen(["taskkill", "/F", "/IM", "cmd.exe"], shell=True)

# Execute the run.bat file
subprocess.Popen(["cmd", "/c", "start", "run.bat"], shell=True)

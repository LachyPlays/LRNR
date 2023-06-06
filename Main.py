import subprocess
import os

subprocess.run(["python", os.getcwd() + "/lrnrsite/manage.py", "runserver"])
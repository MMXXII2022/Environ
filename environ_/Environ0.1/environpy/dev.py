import os
from __init__ import fetch


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m]'


# MAKEFILE

def makefile(name, contents):
    """

    ### makefile



    ` makefile(name='example_fie', contents='hello world, this is a file' ) `
    """
    with open(f"{name}", 'r') as f:
        f.write(f"""{contents}""")



contents="""



{
envshell: {
"EnvironShell_Access": true
"EnvironShell_Password": "changeme"
},

"LocalHostPanel": {

    "Host": "127.0.0.1"
    "port": "8080"


}


}


"""

html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>environment</title>
</head>
<body>
    <!--Styles-->
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .textCenter {
            margin: auto;
            text-align: center;
        }
        
        #btnpannel {
            background-color: black;
        }

        .inst {
            color:white
        }

        ul {
            background-color: black;
        }

        



    </style>
    <!--Script-->

    


    <script> 

    </script>

    <h1 class=".textCenter">localhost environ panel</h1>

    <p>Follow these steps if you want to stop this panel</p>

    <hr>

    <ul>
        <p class="inst">go to terminal where the command was ran</p> <br>
        
        <p class="inst">do CTRL+C to stop the process></p>


    </ul>
    <hr>

    <p>report a bug</p>

    <a href="https://www.github.com/MMXXII2022/environ/issues/new/choose"></a>

    <p>ask a question</p>

    COMING SOON








</body>
</html>
"""


hostpy = """
import os
import json

with open("./settings.json", 'r') as cfg:
    data = cfg.read()

settings = json.loads(data)


lhp = settings["LocalHostPanel"]

port = lhp["port"]
host = lhp["Host"]


# RUN THIS FUNCTION TO HOST YOUR env ON HOST:PORT


def host():
    os.system(f"python -m http.server --directory panel {port} --bind {host}")







"""

browsepy = """
from environpy.dev import browse
import random

files = []

for file in os.listdir():
    if os.path.isfile(file)
        files.append(file)
    else:
        continue

F = random.choice()


browse(F)

"""




# create C_D function

def create_dependencies(envname):
    os.mkdir(f"{envname}")
    makefile("settings.json", 'w', contents=contents)
    os.mkdir(f'{envname}_panel')
    makefile("host.py", 'w', contents=hostpy)
    makefile("panel/base.html", contents=html)
    makefile(browsepy)
    os.mkdir('UploadConfigs')
    makefile("UploadConfigs/note.txt", "the current folder is for")


def browse(filename):
    for file in os.listdir('./'):
        if file == os.path.isfile():
            print(True)
            print("found file")
            with open(file) as f:
                data = f.read()
            print(f"""Read file and found:\t\n{data } """)



class Colors:
    pass
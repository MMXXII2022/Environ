import sys
from dev import create_dependencies
import PyColors
from . import environshell





cmddict = {
    'help': "gives a list of commands",
    'env': "Creates an environment with provided arguments",
    '--version': "Gets the current version of environ",
    'vdict': "gets a version and mini changelog dictionary"

}


__vdict__ = {
    '0.0.1': "initial release of version 0.0.1"
}


__version__ = '0.0.1'

def fetch(obj):

    if obj == "help":
        return cmddict


    if obj == "version":
        return __version__

    if obj == "vdict":
        return __vdict__


if sys.argv[1] == "env":
    create_dependencies(sys.argv[2])
    if sys.argv[2] == "":
        print("Please provide a name for the environment")
# else:
#     print("run help to get a list of commands or provide a command ' python -m environpy [COMMAND] *[OPTION]/*[ARGS] *[ARGS]  ' ")

elif sys.argv[1] == "--version":
    fetch("version")


elif sys.argv[1] == "vdict":
    fetch("vdict")


elif sys.argv[1] == "--version":
    fetch('version')

elif sys.argv[1] == "shell":
    environshell.prompt()


else:
    print(f"run help to get a list of commands or to browse a certain command ' python -m environpy [COMMAND] *[OPTION]/*[ARGS] *[ARGS]  '")



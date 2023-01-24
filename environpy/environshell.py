from dev import *
import os


def prompt():
    prompt = True

    while prompt:
        x = input("EnvironShell> ")

        if x == 'exit':
            print("exited prompt")
            prompt = False
        
        xs = x.split()

        host = xs[1]
        port = xs[2]

        UPLOAD_CMD = "upload"

        DEL = "DEL"
        NONE = ""
        F_ = "mkf"






        if (xs[0]) == "host":
            os.system(f"python -m http.server --directory panel {port} --bind {host}")


            if xs[1] == NONE:
                print("Please provide a host and port in numeric order 1: Host, 2: Port")

            



        elif (xs[0]) == UPLOAD_CMD:
            print("This Feature is Coming soon")
        elif (xs[0]) == DEL:
            os.remove(xs[1])
            print(f"removed file {xs[1]}")

            if xs[1] == NONE:
                print("please provide a filename to remove")
        
        elif (xs[0]) == F_:
            print("Created file")
            makefile(xs[1], "__CONTENTS__")
            print("successfully created file")

            if xs[1] == NONE:
                print("Please Provide a name to create the file")


import os
import sys
import subprocess
import time

def execute_command(command):
    try:
        if "|" in command:
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)

            for cmd in command.split("|"):
                os.dup2(fdin, 0)
                os.close(fdin)

                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print(".dreamShell # command not found: {}".format(cmd.strip()))

            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print("psh: command not found: {}".format(command))


def psh_cd(path):
    """convert to absolute path and change directory"""
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("CD # no such file or directory: {}".format(path))


def dreamshell_help():
    print("""Best discord bot controlling shell ever created
    
        Command List:
    > help - Shows this message
    > exit - Stop the bot process
    > print - Print Some text in shell
    > ping - Get bot latency
    """)


def dreamshell():
    while True:
        inp = input(".dreamShell # ")
        if inp == "exit":
            sys.exit()
        elif inp[:3] == "cd ":
            psh_cd(inp[3:])
        elif inp == "help":
            dreamshell_help()
        else:
            execute_command(inp)
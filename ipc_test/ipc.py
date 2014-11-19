import os
import subprocess


def run():
    proc = subprocess.Popen(["./ipc", "param"],
        stdout = subprocess.PIPE,
        stdin = subprocess.PIPE)
    
    out = proc.stdout.readline()
    print out
    proc.stdin.write("greetings\n")
    proc.stdin.flush()
    out = proc.stdout.readline()
    print out
    #proc.stdin.write("hello")
    #proc.kill()

run()

#!/usr/bin/python3
#

from typing import Callable

import argparse
import logging
import importlib
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(" ","\ ")

def main():
    logging.basicConfig(format="%(message)s")

    parser = argparse.ArgumentParser(description="Run GDB with automatic acctions triggered on specific breakpoints")
    parser.add_argument("-f","--file",help="Python script containing a 'get_events' function that returns a dictionary of breakpoints with the associated event that needs to be called",type=str)
    parser.add_argument("-e","--executable",help="Set gdb executable that will be called",default="gdb",type=str)
    args = parser.parse_args()
    
    if not args.file:
        logging.error("\x1b[31m" + "Script file absent" + "\x1b[0m")
        return
    
    gdb_scripts = [" -x",args.file, 
                " -x " + ROOT_DIR +"/utils/IsolateExecutionListener.py", 
                "-x " + ROOT_DIR + "/utils/init.py"]
    os.system(args.executable + " ".join(gdb_scripts))

if __name__ == "__main__":
    main()


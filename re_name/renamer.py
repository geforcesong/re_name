import os
import argparse


class Renamer:

    def __init__(self):
        self.currentPath = os.getcwd()
        self.oldPatten = ''
        self.newPatten = ''
        self.parseInputs()
        print('Working Path:' + self.currentPath)

    def update(self):
        files = os.listdir(self.currentPath)
        if(len(files) > 0):
            for file in files:
                if(os.path.isfile(file)):
                    print(file)
        print('Renamer update is called!')

    def parseInputs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-o", "--old", help="specify old patten")
        parser.add_argument(
            "-n", "--new", help="specify new patten to replace")
        args = parser.parse_args()
        if(args.old):
            self.oldPatten = args.old.strip()
        if(args.new):
            self.newPatten = args.new.strip()
        if(self.oldPatten == "" or self.newPatten == ""):
            print("You haven't spcify valid parameters, use --help for usage")
            os._exit(1)

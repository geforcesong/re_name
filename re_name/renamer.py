import os
import argparse


class Renamer:

    def __init__(self):
        # self.currentPath = os.getcwd()
        self.currentPath = '/Users/george/lll/'
        self.oldPatten = ''
        self.newPatten = ''
        self.isPreview = False
        self.parseInputs()
        print('Working Path:' + self.currentPath)

    def update(self):
        files = os.listdir(self.currentPath)
        if(len(files) > 0):
            for file in files:
                if(os.path.isfile(os.path.join(self.currentPath, file))):
                    print(file)
        print('Renamer update is called!')

    def parseInputs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("old", help="specify old patten to remove")
        parser.add_argument("new", help="specify new patten you wanted")
        parser.add_argument("-p", "--preview", action="store_true",
                            help="This will show what the result will be.", default=False)
        args = parser.parse_args()
        if(args.old):
            self.oldPatten = args.old.strip()
        if(args.new):
            self.newPatten = args.new.strip()
        self.isPreview = args.preview
        print(self.oldPatten, self.newPatten)
        # if(self.oldPatten == "" or self.newPatten == ""):
        #     print("You haven't spcify valid parameters, use --help for usage")
        #     os._exit(1)

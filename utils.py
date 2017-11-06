import argparse
import sys
import os

if len(sys.argv) < 2:
    print("Welcome to the utility cli for your computer")
    print("Please 'help' command function to see available commands")
    exit()

command = sys.argv[1]


# Global Flags
parser = argparse.ArgumentParser(description = "Operations Utility")
parser.add_argument('command', help = 'commmand')
parser.add_argument('--verbose', '-v', help = "verbose") 
parser.add_argument('-f', '--file', help = "file input")
args = parser.parse_args()

def img2s3():
    if args.file is None:
        print("Please make sure to specify file")
        exit()
    command = ('aws s3 cp {} s3://{}/images/sj/'.format(args.file, os.environ['BUCKET_NAME']))
    print("Running command" + command)
    os.system(command)

def mp42srt():
    if args.file is None:
        print("Please make sure to specify file")
        exit()
    command = ('python2.7 /usr/local/bin/autosub {} -K {} -D en -S en -F srt').format(args.file, os.environ['GOOGLE_AK']) 
    print("Running command " + command)
    os.system(command)

def help():
    print("Commands: ")
    for key in HELP:
        print(key, ':', HELP[key])


HELP = {
    'img2s3' : 'Push an image into the ss3 henosisknot bucket',
    'mp42srt' : 'Convert an mp4 file into an srt file',
    'help' : 'Get Helpful information'
}


FUNCTION_MAP = {
    'img2s3': img2s3,
    'mp42srt': mp42srt,
    'help': help
}



run = FUNCTION_MAP[command]

run()

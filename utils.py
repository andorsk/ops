import argparse
import sys
import os

command = sys.argv[1]


# Global Flags
parser = argparse.ArgumentParser(description = "Operations Utility")
parser.add_argument('command', help = 'commmand')
parser.add_argument('--verbose', '-v', help = "verbose") 
parser.add_argument('-f', '--file', help = "file input")
args = parser.parse_args()

def img2s3():
    command = ('aws s3 cp {} s3://BUCKET_NAME/images/sj/'.format(args.file))
    os.system(command)

def command2():
    print("COMMAND 2")

def help():
    for key in HELP:
        print(key, ':', HELP[key])


HELP = {
    'img2s3' : 'Push an image into the ss3 henosisknot bucket',
    'help' : 'Get Helpful information'
}


FUNCTION_MAP = {
    'img2s3': img2s3,
    'help': help
}



run = FUNCTION_MAP[command]
run()

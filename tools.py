import argparse
import sys
import json

parser = argparse.ArgumentParser(
    description=f'example: python {sys.argv[0]} /var/log/error.log -t text')
parser.add_argument('file', help='position file',
                    metavar='file')
parser.add_argument('-t', help='output converter flag')
parser.add_argument('-o', help='save output file')
cmd = parser.parse_args()

if cmd.t:
    if cmd.o:
        if cmd.t == "json":
            errorLog = open(cmd.file, "r").read().splitlines()
            outputJson = []
            for items in errorLog:
                items = items.split(" ")
                outputJson.append({
                    'date': items[0],
                    'time': items[1],
                    'status': " ".join(items[2::])
                })
            with open(cmd.o, 'w') as f:
                f.write(str(json.dumps(outputJson)))
                f.close()
            print(f'file saved to {cmd.o} with type json')
        if cmd.t == "text":
            errorLog = open(cmd.file, "r").read()
            with open(cmd.o, 'w') as f:
                f.write(errorLog)
                f.close()
            print(f'file saved to {cmd.o} with type plaintext')
    else:
        if cmd.t == "json":
            errorLog = open(cmd.file, "r").read().splitlines()
            outputJson = []
            for items in errorLog:
                items = items.split(" ")
                outputJson.append({
                    'date': items[0],
                    'time': items[1],
                    'status': " ".join(items[2::])
                })
            print(json.dumps(outputJson))
        if cmd.t == "text":
            errorLog = open(cmd.file, "r").read()
            print(errorLog)
else:
    if cmd.o:
        errorLog = open(cmd.file, "r").read()
        with open(cmd.o, 'w') as f:
            f.write(errorLog)
            f.close()
        print(f'fle saved to {cmd.o} with type plaintext')
    else:
        errorLog = open(cmd.file, "r").read()
        print(errorLog)

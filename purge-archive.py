#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser(description='removes lines from archive.txt that don\'t exist in the directory')
parser.add_argument("dir", type=str, help='Directory of the archive.txt to purge and the corresponding videos')
args = parser.parse_args()

hash_length = 11


#Get all of the hashes that we have from every file
hashes = {}
files = os.listdir(args.dir)
for ytfile in files:
    if len(ytfile) > hash_length: 
        lastChar = ytfile.rfind('.') 
        hashes[ytfile[lastChar - hash_length: lastChar ]] = True

print(hashes)

lines = []

#if a hash exists in archive.txt, but does not in the files, that means
#we should delete it from archive.txt
with open(args.dir + "archive.txt", "r") as textFile: 
    lines = textFile.readlines()
    for i, line in enumerate(lines):
        thisLine = line[len('youtube '):-1]
        if thisLine not in hashes:
           print("oh shit " + thisLine + " not download") 
           del lines[i]

print(lines)

with open(args.dir + "archive.txt", "w") as textFile: 
    textFile.writelines(lines)


#!/usr/bin/env python
import sys
import string

def CleanFile():
    """Removes all trailing and leading from whitespace from each line in a text file, will overwrite or create new file depedning on user input"""
    ActionChoice = raw_input("Do you want to overwrite or create new file, please enter 'new' or 'overwrite':")
    Source = open(FileName , 'r')
    Lines = Source.readlines()
    if ActionChoice == 'overwrite':
        Overwrite = open(FileName , 'w+')
        NewLines = [line.strip()+"\n" for line in Lines]
        # With Map :
        #NewLines = map lambda line : line.strip()+"\n" , Lines)
        Overwrite.writelines(NewLines)
    elif ActionChoice == 'new':
        New = open("new_"+FileName, 'w+')
        NewLines = [line.strip()+"\n" for line in Lines]
        New.writelines(NewLines)
    else:
        print "Please enter 'new' or 'overwrite':"
        CleanFile()
    


if __name__ == "__main__":
    FileName = sys.argv[1]
    CleanFile()


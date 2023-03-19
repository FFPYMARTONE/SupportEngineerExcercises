#Excercise 1
#Write a python or bash script that takes three parameters, two strings and a directory
#name, and substitutes any occurrence of the first string with the second string for any file
#in the directory, recursively

import sys #incluso nella python standard library
import os


def replaceInFile(path,stringToFind, stringToReplace):
    fin=open(path,"rt")
    data = fin.read()
    data=data.replace(stringToFind,stringToReplace)
    fin.close()
    fout=open(path,"wt")
    fout.write(data)
    fout.close()


def main():
    
    if len(sys.argv) != 4:
        print("Error: bad parameter")
        exit()
    
    stringToFind=sys.argv[1]
    stringToReplace=sys.argv[2]
    dir=sys.argv[3]

   
    for path, currentDirectory, files in os.walk(dir):
        for file in files:
            replaceInFile(os.path.join(path, file),stringToFind,stringToReplace)







if __name__ == "__main__": #Un programma Python utilizza 
    #la condizione if _name_ == '_main_' per eseguire solo il codice all'interno dell'istruzione if quando il programma viene eseguito direttamente dall'interprete Python.  Il codice all'interno dell'istruzione if non viene eseguito quando 
    #il codice del file viene importato come modulo.
    #aggiunta di commenti in python
    main()





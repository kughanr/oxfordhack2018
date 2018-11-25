# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 2018

@author: HendR
"""

from WordList import WordList
from Parser import Parser

#Returns a list of the words in the document, which are each objects with a list
#of their following words and how many times they show up
def getArrayOfFollowingWords(wordList):
    
    #Initialiing the list
    followingWordsList = WordList(wordList[0], wordList[1])
    
    #Looping through the word list that was fed in as a parameter, which would 
    #just be a list of the parsed words in the file to be analyzed
    for x in range(1, len(wordList)):
        if (x + 1 != len(wordList)):
            #If the word is already in the list, add its following word to the
            #following words list
            if not followingWordsList.addWordToList(wordList[x], wordList[x+1]):
                followingWordsList.addFollowWord(wordList[x], wordList[x+1])
    return followingWordsList.getList()

def main():
    file = input("Which file would you like to get data from? ")
    poem = input("Would you like the output in poem format? (y/n) ")
    word = input("Please enter the first word you would like to use: ")
    number = input("How many words would you like the output to contain? ")
    
    #Parsing the input file for a list of the words
    parser = Parser(file)
    fileList = parser.getData()
    
    #Getting the array of the following words
    listOfWords = getArrayOfFollowingWords(fileList)
    string = word

    #Creating a string with the length equal to the amount of words the user
    #wanted the output to be
    for y in range(int(number)):
        for x in listOfWords:
            if x.getWord() == word:
                word = x.returnMostLikelyFollowWord()
                while (word == None):
                    word = x.returnMostLikelyFollowWord()
                string += " " + word

    #If the user said yes to poem format, this formats the text as a poem
    if (poem == "y"):
        lists = string.split()
        newString = ""
        counter = 0
        for w in lists:
            if (w[0].isupper()) and (counter !=0):
                newString += ",\n" + w
            else:
                if counter == 0:
                    newString += w.title()
                else:
                    newString += " " + w
            counter += 1
        string = newString
    #Printing the output to the screen
    print(string + ".")

if __name__ == "__main__":
    main()

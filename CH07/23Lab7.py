#----------------------------------#
#   Connor Seemann Seat 23 Lab 7   #
#----------------------------------#

# This program will convert a sentence the user enters into pig latten.
# This will be accomplished by taking the first letter of the word and
# adding it to the end of the word. The next step will be to add ay to
# The end of that new word

def firstCharTolastChar(stringList):
    newList = [] # defininf a new temporary list to store the modified strings in
    for i in stringList: # setting i to be each element inside the list
        newList.append(i[1:]+i[0]) # having the string start with the second character and ending with the first
    return newList # returning the newList

def addAy(stringList):
    newList = [] # defininf a new temporary list to store the modified strings in
    for i in stringList: # setting i to be each element inside the list
        newList.append(i+"ay") # adding 'ay' to the end of the words in the word lists
    return newList # returning the newList

def main():
    moreWords = True
    while moreWords == True:
        sentence = input("Please enter a sentence you want translated into pig latten\n") # getting the user input

        wordList = sentence.split(' ') # splitting the sentence up at each space
        # print(wordList, "\n") # for debugging purpouses

        # print(firstCharTolastChar(wordList)) # for debugging purpouses splicing the string to have the first character be the new last
        # print(addAy(firstCharTolastChar(wordList))) # for debugging purpouses adding 'ay' to the end of the words in the word lists
        
        wordList = addAy(firstCharTolastChar(wordList)) # setting wordList to be the new modified sentence
        sentence = ' '.join(wordList) # joining the wordList back together and setting it back to the sentence
        
        print(" The translated sentence is the following:\n {}".format(sentence)) # out put for the new sentence

        cont = input ("\n\nWould you like to enter another sentence? (Y / N): ")
        
        if cont.lower() == 'y':
            print("\n\n")

        elif cont.lower() == 'n':
            print("Goodbye!\n")
            moreWords = False

if __name__ == '__main__':

    #introduction print statement
    print(" This program will convert a sentence the user enters into pig latten.\n"+  
          " This will be accomplished by taking the first letter of the word and \n"+
          " adding it to the end of the word. The next step will be to add ay to \n"+
          " the end of that new word.\n\n")
    
    main() # going to main with the word string sentence



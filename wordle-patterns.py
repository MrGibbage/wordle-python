import pandas
import numpy

startWord = "crane" #must be five letters long
answers = pandas.read_csv('answers.csv', sep=',',header=None, index_col=False, usecols=[0]).squeeze("columns")

clue = "xxxxx"
clues = []

#look for yellow and green matches
#first look for yellows and mark them by looking to see if a letter is in the answer.
#It may actually be in the right spot, but first just check to see if is is in there.
#Next check to see if it is in the right spot. If it is, it will already be marked
#as yellow from step 1, but change it to green.
for answer in answers:
    for i in range(0, len(startWord)):
        #look for yellow match
        if (startWord[i:i + 1] in answer):
            clue = clue[:i] + "y" + clue[i + 1:]
        
        #look for green match
        if (startWord[i:i + 1] == answer[i:i + 1]):
            clue = clue[:i] + "g" + clue[i + 1:]
    
    #add the clue to the clues array and then reset the clue variable
    clues.append(clue)
    clue = "xxxxx"

#Summarize the results
#from https://www.delftstack.com/howto/numpy/python-numpy-value-counts/
unique, counts = numpy.unique(clues, return_counts = True)
result = numpy.column_stack((unique, counts))
print(result)

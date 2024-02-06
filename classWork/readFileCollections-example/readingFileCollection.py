import spacy
#nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')
import os

##############################
# OBJECTIVE: Find out which words in my document are most similar to a particular word of interest
# How to find this using spaCy similarity vectors?

# Helpful resource for spaCy similarity calculation based on a selected word:
# https://stackoverflow.com/questions/55921104/spacy-similarity-warning-evaluating-doc-similarity-based-on-empty-vectors
##############################

workingDir = os.getcwd()
print("current working directory: " + workingDir)

insideDir = os.listdir(workingDir)
print("inside this directory are the following files AND directories: " + str(insideDir))

# use os.path.join to connect the subdirectory to the working directory:
CollPath = os.path.join(workingDir, 'textCollection')
print(CollPath)

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)
        tokens = nlp(stringFile)
        vectors = tokens.vector

        wordOfInterest = nlp(u'music')
        print(wordOfInterest, ': ', wordOfInterest.vector_norm)

        highSimilarityDict = {}
        for token in tokens:
            if(token and token.vector_norm):
                if wordOfInterest.similarity(token) > .3:
                    highSimilarityDict[token] = wordOfInterest.similarity(token)
                        # print(token.text, "about this much similar to", wordOfInterest, ": ", wordOfInterest.similarity(token))
        print("This is a dictionary of words most similar to the word " + wordOfInterest.text + " in this file.")
        #highSimilarityWords = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

        #sorted_highSimilarityWords = sorted(highSimilarityWords.items(), key=lambda x: x[1])
        #converted_dict = dict(sorted_highSimilarityWords)

        #print(converted_dict)
        # Output: {'Cruyff': 104, 'Eusebio': 120, 'Messi': 125, 'Ronaldo': 132, 'Pele': 150}

# I threw the flag in for this one :(
        highSimilarityReduced = {}
        for key, value in highSimilarityDict.items():
            if value not in highSimilarityReduced.values():
                highSimilarityReduced[key] = value


        lowSimilarityDict = {}
        for token in tokens:
            if(token and token.vector_norm):
                if wordOfInterest.similarity(token) < .3:
                    lowSimilarityDict[token] = wordOfInterest.similarity(token)
                        # print(token.text, "about this much similar to", wordOfInterest, ": ", wordOfInterest.similarity(token))
        print("This is a dictionary of words least similar to the word " + wordOfInterest.text + " in this file.")
        print(lowSimilarityDict)

        lowSimilarityReduced = {}
        for key, value in lowSimilarityDict.items():
            if value not in lowSimilarityReduced.values():
                lowSimilarityReduced[key] = value

for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)
dict1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}

temp = []

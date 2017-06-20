# coding: utf-8
# Name: Leon Ren
# Final Project - TextID

import string, math
from porter import create_stem

class TextModel:

    def __init__(self, name):
        """ the constructor for the TextModel class
            all dictionaries are started at empty
            the name is just for our own purposes, to keep things 
            organized
        """
        self.name = name
        self.words = {}   # starts empty
        self.wordlengths = {}
        self.stems = {}
        self.sentencelengths = {}
        self.punctuation = {}
        self.conjunctions = {}
        self.caps = {}
        self.indpClause = {}
        self.hiFreqWords = {}
        self.FANBOYS = ["for", "and", "nor", "but", "or", "yet", "so"]


    def __repr__(self):
        """ this method creates the string version of TextModel objects
        """
        s  = "\nModel name: " + str(self.name) + "\n"
        s += "    n. of words: " + str(len(self.words))  + "\n"
        s += "    n. of word lengths: " + str(len(self.wordlengths))  + "\n"
        s += "    n. of sentence lengths: " + str(len(self.sentencelengths))  + "\n"
        s += "    n. of stems: " + str(len(self.stems))  + "\n"
        s += "    n. of punctuation marks: " + str(len(self.punctuation))  + "\n"
        s += "    n. of conjunctions: " + str(len(self.conjunctions))  + "\n"
        s += "    n. of captial letters used: " + str(len(self.caps))  + "\n"
        s += "    n. of indpendent clauses lengths used: " + str(len(self.indpClause))  + "\n"
        s += "    n. of high frequency words: " + str(len(self.hiFreqWords))  + "\n"
        return s

    def readTextFromFile(self, filename):
        """ This is a file-handling class. Reads text from filename.txt
            and stores in a string, which is returned. If cannot read 
            from file, throws an error.
        """
        try:
            f = open (filename)
        except IOError:
            print("Cannot open file: ", filename)
            return
        text = f.read()
        f.close()

        return text

    def makeSentenceLengths(self, s):
        """ From a string s, build a dictionary containing number of each
            sentence length. Keys are sentence lengths, values are number
            of each sentence length.

            For example: 5 setences of 3 words each, 3 sentences of 1 word 
            each builds a dictionary:
            d = {3: 5, 1: 3}

            This is stored in self.sentencelengths
        """
        LoW = s.split()
        d = self.sentencelengths

        senLen = 0 #store number of words in sentence

        for word in LoW: #for each word in list of words
            senLen += 1
            if word[-1] in ".!?;":
                if senLen in d:
                    d[senLen] += 1 
                else:
                    d[senLen] = 1
                senLen = 0

    def cleanString(self, s):
        """ cleanString takes in a string S and returns it without 
            and capital letters or punctuation
        """
        s = s.lower()
        for p in string.punctuation:
            s = s.replace(p, '')
        return s

    def makeWordLengths(self, s):
        """ From a string s, build a dictionary containing numbers of each
            word length. Keys are sentence lengths, Values are number
            of each word length.

            For example: 5 words of 3 chars each, 3 words of 2 chars 
            each builds a dictionary:
            d = {3: 5, 2: 3}

            This is stored in self.wordlengths
        """
        s = self.cleanString(s)
        LoW = s.split()
        d = self.wordlengths


        for word in LoW: #for each word in list of words
            wordLen = len(word)
            if wordLen in d:
                d[wordLen] += 1
            else:
                d[wordLen] = 1
    
    def makeWords(self, s):
        """ From a string s, build a dictionary containing numbers of each
            word. Keys are words, Values are number of each word.

            For example: A string "I I I. Me me me me." contains 3 instances of
            "I" and 4 instances of "me," resulting in the following dictionary:
            d = {'I': 3, 'me': 4}

            This is stored in self.words
        """
        s = self.cleanString(s)
        LoW = s.split()
        d = self.words

        for word in LoW: #for each word in list of words
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

    def makeStems(self, s):
        """ From a string s, build a dictionary containing numbers of each
            word with the stems of words [e.g. -ing, -ed, -s, ...] cleaned.
            Keys are words, Values are number of each word.

            This is stored in self.stems
        """
        s = self.cleanString(s)
        LoW = s.split()
        d = self.stems

        for word in LoW: #for each word in list of words
            stem = create_stem(word)
            if stem in d:
                d[stem] += 1
            else:
                d[stem] = 1
                
        
    def makePunctuation(self, s):
        """ From a string s, build a dictionary containing numbers of each
            punctuation mark. Keys are punctuation marks, Values are number
            of each punctuation mark.

            This is stored in the dictionary self.punctuation
        """
        d = self.punctuation

        for c in s: #for each character in string
            if c in string.punctuation:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
    
    def makeConjunction (self, s):
        """ makeConjunction creates a dictionary of the number of times each
            coordinating conjunction [that is, a word deliniating the start of 
            an independent clause, (for, and ,not, but, or, yet, so)] is used
        """

        LoW = s.split()
        d = self.conjunctions

        prevIsComma = False

        for w in LoW: #for word in List of words
            if prevIsComma:
                if w in self.FANBOYS:
                    if w in d:
                        d[w] += 1
                    else:
                        d[w] = 1
                prevIsComma = False
            if w[-1] in ",":
                prevIsComma = True
        
    def makeCaps (self, s):
        """ makeCaps creates a dictionary of the number of times each
            captial letter is used.
        """
        d = self.caps
        upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for c in s: #for each character in string
            if c in upperChars: # if this is a captial Letter
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
    
    def makeClauses (self, s):
        """ makeClauses creates a dictionary of the number of times each
            length of an independent clause proceeding a conjunciton is used. 

            For example, the sentence: "I am Leon, and I am a student" has one
            independent clause: "I am a student," with a length of 4. Thus:
            d = {4:1}
        """

        LoW = s.split()
        d = self.indpClause

        prevIsComma = False
        clauseLen = 0
        counting = False

        for w in LoW: #for word in List of words
            if counting == True:
                clauseLen += 1
                if w[-1] in '.!?,':
                    counting = False
                    if clauseLen in d:
                        d[clauseLen] += 1
                    else:
                        d[clauseLen] = 1
            
            if prevIsComma:
                if w in self.FANBOYS:
                    clauseLen = 0
                    counting = True
                    
                prevIsComma = False
            if w[-1] in ",":
                prevIsComma = True

    def makeHiFreqWords (self, s):
        """ makeHiFreqWords creates a dictionary of words that are "high
            frequency," meaning that they are more than 2% of all words
            in the text
        """
        s = self.cleanString(s)
        LoW = s.split()
        d = self.words
        f = self.hiFreqWords

        if len(d) == 0:
            for word in LoW: ##first compile dictionary of words
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1

        for word in d: #then save only high frequency word
            if d[word] > 0.02 * len(LoW):
                f[word] = d[word]

    def normalizeDictionary(self, d):
        """ normalizeDictionary takes in a dictionary (d) and normalizes it,
            meaning that all values add up to 1 while the keys and proporitons
            are maintained
        """
        LoV = d.values()
        s = sum(LoV)
        nd = {}
        for k in d:
           nd[k] = d[k]/s
        return nd

    def smallestValue(self, nd1, nd2):
        """ this method takes in two model dictionaries, nd1 and nd2
            and then returns the smallest postive value across them both
        """
        if len(nd1) > 0:
            m = list(nd1.values())[0]
        elif len(nd2) > 0:
            m = list(nd1.values())[0]
        else:
            return -1
            
        for x in nd1.values():
            if x > 0 and x < m:
                m = x

        for x in nd2.values():
            if x > 0 and x < m:
                m = x

        return m
    
    def compareDictionaries(self, d, nd1, nd2):
        """ returns the log probability that the dictionary arose from the distribution of
            normalized data in nd1 and the log probability that the dictionary arose from
            the normalized dictionary nd2 in a list [log-prob1, log-prob2]
        """
        #ensures that nd1 and nd2 are both normalized
        nd1 = self.normalizeDictionary(nd1)
        nd2 = self.normalizeDictionary(nd2)
        
        total_log_prob1 = 0.0
        total_log_prob2 = 0.0
        epsilon = self.smallestValue(nd1, nd2) / 2.0
        if epsilon < 0: #no comparison, result in tie
            epison = 1
        for k in d:
            if k in nd1:
                total_log_prob1 += (d[k] * math.log(nd1[k]))
            else:
                total_log_prob1 += (d[k] * math.log(epsilon))
            if k in nd2:
                total_log_prob2 += (d[k] * math.log(nd2[k]))
            else:
                total_log_prob2 += (d[k] * math.log(epsilon)) 

        return [total_log_prob1, total_log_prob2]

    def createAllDictionaries(self, s): 
        """ should create all nine of self's 
            dictionaries in full - for testing and 
            checking how they are working...
        """
        self.makeSentenceLengths(s)
        self.makeWords(s)
        self.makeStems(s)
        self.makePunctuation(s)
        self.makeWordLengths(s)
        self.makeConjunction(s)
        self.makeCaps(s)
        self.makeClauses(s)
        self.makeHiFreqWords(s)

    

    def printAllDictionaries(self):
        """ print all five dictionaries in full
        """
        print ("The text model named [", self.name, "] has dictionaries:")
        print ("self.sentencelengths:", self.sentencelengths)
        print ("self.words:", self.words)
        print ("self.wordlengths:", self.wordlengths)
        print ("self.stems:", self.stems)
        print ("self.punctuation:", self.punctuation)
        print ("self.conjunctions:", self.conjunctions)
        print ("self.caps:", self.caps)
        print ("self.indpClause", self.indpClause)
        print ("self.hiFreqWords", self.hiFreqWords)

    def compareTextWithTwoModels(self, model1, model2):
        """ compare the self text model with the other two text models
            and indicates which model is closer 
            inputs: model1, model2 to be compared to models
            output: the print results of the comparison
        """

        words_comp = self.compareDictionaries(self.words, self.normalizeDictionary(model1.words), self.normalizeDictionary(model2.words))
        wordlengths_comp = self.compareDictionaries(self.wordlengths, self.normalizeDictionary(model1.wordlengths), self.normalizeDictionary(model2.wordlengths))
        stems_comp = self.compareDictionaries(self.stems, self.normalizeDictionary(model1.stems), self.normalizeDictionary(model2.stems))
        sentencelengths_comp = self.compareDictionaries(self.sentencelengths, self.normalizeDictionary(model1.sentencelengths), self.normalizeDictionary(model2.sentencelengths))
        punc_comp = self.compareDictionaries(self.punctuation, self.normalizeDictionary(model1.punctuation), self.normalizeDictionary(model2.punctuation))
        conj_comp = self.compareDictionaries(self.conjunctions, self.normalizeDictionary(model1.conjunctions), self.normalizeDictionary(model2.conjunctions))
        cap_comp = self.compareDictionaries(self.caps, self.normalizeDictionary(model1.caps), self.normalizeDictionary(model2.caps))
        indpClause_comp = self.compareDictionaries(self.indpClause, self.normalizeDictionary(model1.indpClause), self.normalizeDictionary(model2.indpClause))
        hiFreqWords_comp = self.compareDictionaries(self.hiFreqWords, self.normalizeDictionary(model1.hiFreqWords), self.normalizeDictionary(model2.hiFreqWords))
        
        print ("Overall comparison of", self.name, "vs", model1.name, "and", model2.name)
        print ()
        print ("{0: >20} {1: >10}  {2: >10} {3: >20}".format("name", "vsTM1", "vsTM2", "winning model"))
        print ("{0: >20} {1: >10}  {2: >10} {3: >20}".format("----", "-----", "-----", "-------------"))
        result = "Overall comparison of " + self.name + " vs " + model1.name + " and " + model2.name + '\n'
        result += ' ' * 16 + "name" + ' ' * 5 + "vsTM1" + ' ' * 5 + "vsTM2" + ' ' * 7 + "winning model" + '\n'
        result += ' ' * 16 + "----" + ' ' * 5 + "-----" + ' ' * 5 + "-----" + ' ' * 7 + "-------------" + '\n'
        confidence = 0
        total = 0
        win1 = 0
        win2 = 0
        if words_comp[0] > words_comp[1]:
            confidence += abs(words_comp[0] - words_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(words_comp[1] - words_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(words_comp[0] + words_comp[1]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2:>10.2f} {3: >20}".format("words", round(words_comp[0],2), round(words_comp[1], 2), winner)) 
        result += ' ' * 15 + "words" + ' ' * (10 - len(str(round(words_comp[0], 2)))) + str(round(words_comp[0],2)) + ' ' * (10 - len(str(round(words_comp[1], 2)))) + str(round(words_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if wordlengths_comp[0] > wordlengths_comp[1]:
            confidence += abs(wordlengths_comp[0] - wordlengths_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(wordlengths_comp[1] - wordlengths_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(words_comp[0] + words_comp[1]) / 2.0
        print ("{0: >20} {1:>10.2f}  {2: >10.2f} {3: >20}".format("wordlengths", round(wordlengths_comp[0],2), round(wordlengths_comp[1], 2), winner)) 
        result += ' ' * 9 + "wordlengths" + ' ' * (10 - len(str(round(wordlengths_comp[0], 2)))) + str(round(wordlengths_comp[0],2)) + ' ' * (10 - len(str(round(wordlengths_comp[1], 2)))) + str(round(wordlengths_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if stems_comp[0] > stems_comp[1]:
            confidence += abs(stems_comp[0] - stems_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(stems_comp[1] - stems_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(stems_comp[0] + stems_comp[1]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("stems", round(stems_comp[0],2), round(stems_comp[1], 2), winner)) 
        result += ' ' * 15 + "stems" + ' ' * (10 - len(str(round(stems_comp[0], 2)))) + str(round(stems_comp[0],2)) + ' ' * (10 - len(str(round(stems_comp[1], 2)))) + str(round(stems_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if sentencelengths_comp[0] > sentencelengths_comp[1]:
            confidence += abs(sentencelengths_comp[0] - sentencelengths_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(sentencelengths_comp[1] - sentencelengths_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(sentencelengths_comp[1] + sentencelengths_comp[0]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("sentencelengths", round(sentencelengths_comp[0],2), round(sentencelengths_comp[1], 2), winner)) 
        result += ' ' * 5 + "sentencelengths" + ' ' * (10 - len(str(round(sentencelengths_comp[0], 2)))) + str(round(sentencelengths_comp[0],2)) + ' ' * (10 - len(str(round(sentencelengths_comp[1], 2)))) + str(round(sentencelengths_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if punc_comp[0] > punc_comp[1]:
            confidence += abs(punc_comp[0] - punc_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(punc_comp[1] - punc_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(punc_comp[0] + punc_comp[1]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("punctuation", round(punc_comp[0],2), round(punc_comp[1], 2), winner)) 
        result += ' ' * 9 + "punctuation" + ' ' * (10 - len(str(round(punc_comp[0], 2)))) + str(round(punc_comp[0],2)) + ' ' * (10 - len(str(round(punc_comp[1], 2)))) + str(round(punc_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if conj_comp[0] > conj_comp[1]:
            confidence += abs(conj_comp[0] - conj_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(conj_comp[1] - conj_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(conj_comp[0] + conj_comp[1]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("conjunctions", round(conj_comp[0],2), round(conj_comp[1], 2), winner))
        result += ' ' * 8 + "conjunctions" + ' ' * (10 - len(str(round(conj_comp[0], 2)))) + str(round(conj_comp[0],2)) + ' ' * (10 - len(str(round(conj_comp[1], 2)))) + str(round(conj_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if cap_comp[0] > cap_comp[1]:
            confidence += abs(cap_comp[0] - cap_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(cap_comp[1] - cap_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(cap_comp[1] + cap_comp[0]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("capitalization", round(cap_comp[0],2), round(cap_comp[1], 2), winner))
        result += ' ' * 6 + "capitalization" + ' ' * (10 - len(str(round(cap_comp[0], 2)))) + str(round(cap_comp[0],2)) + ' ' * (10 - len(str(round(cap_comp[1], 2)))) + str(round(cap_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if indpClause_comp[0] > indpClause_comp[1]:
            confidence += abs(indpClause_comp[0] - indpClause_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(indpClause_comp[1] - indpClause_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(indpClause_comp[0] + indpClause_comp[1]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("independentClauses", round(indpClause_comp[0],2), round(indpClause_comp[1], 2), winner))
        result += ' ' * 2 + "independentClauses" + ' ' * (10 - len(str(round(indpClause_comp[0], 2)))) + str(round(indpClause_comp[0],2)) + ' ' * (10 - len(str(round(indpClause_comp[1], 2)))) + str(round(indpClause_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        if hiFreqWords_comp[0] > hiFreqWords_comp[1]:
            confidence += abs(hiFreqWords_comp[0] - hiFreqWords_comp[1])
            winner = model1.name
            win1 += 1
        else:
            confidence += abs(hiFreqWords_comp[1] - hiFreqWords_comp[0])
            winner = model2.name
            win2 += 1
        total += abs(hiFreqWords_comp[0] + hiFreqWords_comp[1]) / 2.0
        print ("{0: >20} {1: >10.2f}  {2: >10.2f} {3: >20}".format("highFrequencyWords", round(hiFreqWords_comp[0],2), round(hiFreqWords_comp[1], 2), winner))
        result += ' ' * 2 + "highFrequencyWords" + ' ' * (10 - len(str(round(hiFreqWords_comp[0], 2)))) + str(round(hiFreqWords_comp[0],2)) + ' ' * (10 - len(str(round(hiFreqWords_comp[1], 2)))) + str(round(hiFreqWords_comp[1], 2)) + ' ' * (20-len(winner)) + winner + '\n'

        print()

        print ("  --> Model1 wins on", win1, "features")
        print ("  --> Model2 wins on", win2, "features")

        print()
        result += '\n' + "  --> Model1 wins on " + str(win1) + " features" + '\n' + "  --> Model1 wins on " + str(win2) + " features" + '\n'

        print("  OVERALL RESULT:")
        result += "  OVERALL RESULT:" + '\n'
        if win1 > win2:
            print("  ++++++    ", model1.name, "is the better match!     +++++")
            result += "  ++++++     " + model1.name + " is the better match!     +++++" + '\n'
        else:
            print("  ++++++    ", model2.name, "is the better match!     +++++")
            result += "  ++++++     " + model2.name + " is the better match!     +++++" + '\n'
        
        print()

        print("  Confidence Level (out of 100) [<0.5 is low, >3 is high]: ", (confidence/total) * 100.0)
        result += '\n' + "  Confidence Level (out of 100) [<0.5 is low, >3 is high]: " + str((confidence/total) * 100.0) +  "                      " + '\n'

        return result



def test ():
    """ runs a full version of two training files and 1 unknown file to test
        training file 1 should be called "train1.txt"
        training file 2 should be called "train2.txt"
        the unknown file should be called "unknown.txt"

        If the unknown file better matches training file 1, the
        program will tell you that "Model1" is the better match.
        The same goes for training file 2  and "Model2"
    """

    print(" +++++++++++ Model1 +++++++++++ ")
    trained_tm1 = TextModel( "Model1" )
    text1 = trained_tm1.readTextFromFile( "train1.txt" )
    trained_tm1.createAllDictionaries(text1)  # provided in hw description

    print(" +++++++++++ Model2 +++++++++++ ")
    trained_tm2 = TextModel( "Model2" )
    text2 = trained_tm2.readTextFromFile( "train2.txt" )
    trained_tm2.createAllDictionaries(text2)  # provided in hw description

    print(" +++++++++++ Unknown text +++++++++++ ")
    unknown_tm = TextModel( "Unknown (trial)" )
    text_unk = unknown_tm.readTextFromFile( "unknown.txt" )
    unknown_tm.createAllDictionaries(text_unk)  # provided in hw description

    unknown_tm.compareTextWithTwoModels(trained_tm1,trained_tm2)

    

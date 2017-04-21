'''
The module 'feedback' is used to give feedback for a speech processing system
in multiple forms, including ARPAbet, IPA, and text-to-speech

'''

# Will probably be best to import modules that convert the text into each form
import nltk

class Feedback:
    
    def __init__(self, text):
        self.text = text
    
    # this function returns the ARPAbet pronunciation of the given text
    def arpabet(self): 
    
        #TODO: Take the given text; for each word in the text
        # take the word, get the ARPAbet pronunciation and store it in
        # a string or a list
        # return the ARPAbet pronunciation for the whole text
        
        #This prints each word and its pronunciation, but not in a list. The phoneme is not a string so I cannot append them into a list.
        arpabet = nltk.corpus.cmudict.dict()
        line=text.readline()
        while(line>0):
            for word in line: #should we read line by line?
                print (word,)
                arpabet_pronunciation=arpabet[word][0]
                for phoneme in arpabet_pronunciation:	
                    phoneme=re.sub("u"," ",phoneme)
                    print (phoneme,)
                print ("\n")
            line=text.readline()
           
	
    
    # this function returns the IPA pronunciation of the given text
    def ipa(self):
        #TODO: Take the given text; for each word in the text
        # take the word, get the IPA pronunciation and store it in
        # a string or a list
        # return the IPA pronunciation for the whole text
    
    # this function returns the text to speech of the given text
    def tts(self):
        #TODO: Use the Microsoft TTS system to get the speech;
        # return (and play?) the audio
    

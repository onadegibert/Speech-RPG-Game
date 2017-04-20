'''
The module 'feedback' is used to give feedback for a speech processing system
in multiple forms, including ARPAbet, IPA, and text-to-speech

'''

# Will probably be best to import modules that convert the text into each form

class Feedback:
    
    def __init__(self, text):
        self.text = text
    
    # this function returns the ARPAbet pronunciation of the given text
    def arpabet(self): 
        #TODO: Take the given text; for each word in the text
        # take the word, get the ARPAbet pronunciation and store it in
        # a string or a list
        # return the ARPAbet pronunciation for the whole text
        
    
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
    
pip install pyspellchecker

import numpy as np
import pandas as pd
from spellchecker import SpellChecker

class isSpam:
    def __init__(self, text_data):
        self.text_data = text_data
    
    def get_mispelled_words(self):
        """Gets the mispelled words in each element of 
           the text data. 
        Args:
            text_data: text data to apply the function to.
        Returns:
            mispelled_list: a list of lists of the mispelled words. 
            the outer list length = the number of elements in the text data.
            mispelling_counts: a list of the number of mispelled words,
            list index number = email element number in the dataset
        """

        #split textdata into a list of emails
        emails = []
        for i in range(self.text_data.shape[0]):
            emails.append(self.text_data[i])

        #split each email into a list of words in the email
        for j in range(len(emails)):
            emails[j] = emails[j].split()
            
        #import spellchecker function as spell
        spell = SpellChecker()
        
        #initialize empty list to store the lists of mispelled words
        mispelled_list = []
        
        #iterate through all of the emails in the text dataset
        for i in range(len(emails)):
                
            #initialize empty list to store the mispelled words in each email
            email_mispellings = []
                
            #iterate through all of the words in the email
            for j in emails[i]:
                
                #if j is mispelled, append j to email_mispellings
                #don't add 'Subject:' as a mispelling, it's every email's initial word
                if j != spell.correction(j) and j != 'Subject:':
                    email_mispellings.append(j)
                    
            #append to the overall list of mispelled words each email's list of mispellings
            mispelled_list.append(email_mispellings)

        #initialize empty list to store the amount of mispelled words per email
        mispelling_counts = []
        
        #iterate through the list of lists of mispelled words
        for k in range(len(mispelled_list)):
            
            #append to mispelling_counts the number of mispelled words in each email
            mispelling_counts.append(len(mispelled_list[i]))
    
        return mispelled_list, mispelling_counts
                
    def get_mispelling_duplicates(self):
        """Gets the repeated mispelled words in each element of the text data. 
        Args:
            text_data: text data to apply the function to.
        Returns:
            duplicate_list: a list of lists of repeated mispelled words. 
            the outer list length = the number of elements in the text data.
            duplicate_counts: a list of the number of repeated mispelled words,
            list index number = email element number in the dataset
        """
        
        #grab the list of lists of mispelled words from the previous function
        mispelled_words = self.get_mispelled_words()[0]
        
        #initialize an empty list to store the lists of repeated mispelled words
        duplicate_list = []

        #iterate through the email lists of the overall mispelled word list
        for lists in mispelled_words:
            
            #initialize an empty dictionary to keep track of any repeated mispellings
            D = {}
            
            #iterate through each email list
            for i in range(len(lists)):
                
                #assign each word of the email mispelled list as a key in dictionary D, with a base value 0
                D[ lists[i] ] = 0
                
            #iterate through the email list
            for j in range(len(lists)):
                
                #if the word is the current key in D, add 1 to its value
                if lists[j] in D :
                    D[ lists[j] ] = D[ lists[j] ] + 1  
            
            #initialize an empty list to store the list of repeated mispellings      
            email_duplicates = []
            
            #iterate through the dictionary
            for key in D:
                
                #if the mispelling (key) has a value > 1
                if D[key] > 1:
                    #then it was repeated and should be added to the duplicates list
                    email_duplicates.append(key)
                    
            #append to the overall list of repeated mispelled words each email's list of repeated mispellings
            duplicate_list.append(email_duplicates)
        
        #initialize empty list to store the amount of repeated mispelled words per email
        duplicate_counts = []
        
        #iterate through the list of lists of repeated mispelled words
        for i in range(len(duplicate_list)):
            
            #append to duplicate_counts the number of repeated mispelled words in each email
            duplicate_counts.append(len(duplicate_list[i]))
  
        return duplicate_list, duplicate_counts

# EG of how to use the functions from the isSpam class:

# a = isSpam(email_data["text"])

# a.get_mispelled_words()
    #a.get_mispelled_words()[0] returns mispelled_list 
    #a.get_mispelled_words()[1] returns mispelling_counts 


# a.get_mispelling_duplicates()
    #a.get_mispelling_duplicates()[0] returns duplicate_list 
    #a.get_mispelling_duplicates()[1] returns duplicate_counts 
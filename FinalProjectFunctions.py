# Loading required packages
import string
import re
from collections import Counter

## Might not need! ####
# import io 
# import nltk
# # Had to run this once
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize 
#####

# Installed running this command in the terminal
# pip install pyspellchecker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from spellchecker import SpellChecker

class isSpam:
    """
    INSERT DOCSTRING
    """
    def __init__(self, text_data):
        self.text_data = text_data
    
    ### OLIVIA'S FUNCTIONS ###
    
    def text_to_dict(self):
        """Count the number of occurrences of n-grams in a string. 
        Args:
            text_data: text data to apply the function to.
        Returns:
            a dict keyed by the email subject, with values representing 
            the body of the email.
        """
        # initialize empty lists to store subject and body of emails
        subject = []
        body = []

        # iterate through each row in text data
        for i in range(self.text_data.shape[0]):
            # split the email text by the first instance of `\n` by utilizing `maxsplit` arg
            split_email = self.text_data[i].split('\n', maxsplit = 1)

            # append corresponding parts of the split email
            # For subject list, delete word 'Subject: '
            subject.append(split_email[0].removeprefix("Subject: "))
            body.append(split_email[1])

        # return dictionary made from subject, body lists
        return dict(zip(subject, body))

    def get_common_words(self, n):
        """Gets the n most frequently occuring words in each element of 
           the text data. 
        Args:
            text_data: text data to apply the function to.
            n: a parameter specifying the number of most common
               words to find.
        Returns:
            a list of lists of tuples, with the fist element of the tuple being the 
            commonly occuring word, and the second element being the count of the 
            number of times the word occured. The outer list will have the same length 
            as the dataset. Each inner list will have length n.
        """
        # grab body of each email and store as list
        email_bodies = list(self.text_to_dict().values())

        # clean the emails 
        # remove punctuation
        clean_punct = [''.join(c for c in s if c not in string.punctuation) for s in email_bodies]

        # remove numbers
        clean_digit = [''.join(i for i in s if not i.isdigit()) for s in clean_punct]

        # remove special characters
        filter = ''.join([chr(i) for i in range(1, 32)])
        clean_spc_char = [w.translate(str.maketrans('', '', filter)) for w in clean_digit]

        # remove extra saces
        clean_spaces = [re.sub('\s+',' ', j) for j in clean_spc_char]

        # split strings into individual words
        # output is a list of word lists
        words = [s.split() for s in clean_spaces]

        # Check to see if n is a reasonable value 
        # (less than the number of words in each email)
        if n > len(words):
            # If unreasonable number, throw ERROR
            raise ValueError('Input a smaller n')
        # else, will continue with the rest of the code:

        most_occ_list = []
    
        # iterate through all of the lists of words from each email body
        for i in words:
            # initialize instance of counter for current word list
            counter = Counter(i)

            # most_common() produces k frequently encountered
            # input values and their respective counts.
            most_occur = counter.most_common(n)

            # append k most frequently encountered to list output
            most_occ_list.append(most_occur)

        return most_occ_list
    
    ### MADDIE'S FUNCTIONS ###
    
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
            mispelling_counts.append(len(mispelled_list[k]))
    
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

### EG of how to use the functions from the isSpam class: ###

# a = isSpam(email_data["text"]) -> Creates instance of class
# a.get_common_words(5) -> gets 5 most common words from each text 
# a.text_to_dict() -> creates a dictionary of email subject and body
# a.get_mispelled_words()
    # a.get_mispelled_words()[0] -> returns mispelled_list 
    # a.get_mispelled_words()[1] -> returns mispelling_counts 
# a.get_mispelling_duplicates()
    # a.get_mispelling_duplicates()[0] -> returns duplicate_list 
    # a.get_mispelling_duplicates()[1] -> returns duplicate_counts 

    
### FUNCTION OUTSIDE OF CUSTOM CLASS ###
def graphMispellings(spamList, hamList) :
    """Shows a graph with the spamList and hamList plotted on it. 
        Args:
            spamList: first list plotted on graph
            hamList: second list plotted on graph
        Returns:
            ax: line graph with spamList and hamList plotted on the same plot
    """
    #initialize figure with 1 plot
    fig, ax = plt.subplots(1)
    
    #label axes & title
    ax.set( xlabel = 'Emails', ylabel = '# of Mispellings')
    fig.suptitle( 'Frequency of Mispellings')
    
    #plot the hamList as a red line and label 'ham'
    ax.plot(list(range(len(hamList))), hamList, color = 'red', label = 'Ham')
    
    #plot the spamList as a blue line and label 'spam'
    ax.plot(list(range(len(spamList))), spamList, color = 'blue', label = 'Spam') 
    ax.legend()
    
    return ax

    
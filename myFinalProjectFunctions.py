# Loading required packages
import string
import re
from collections import Counter

class isSpam:
    def __init__(self, text_data):
        self.text_data = text_data
    
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

        # initialize empty list to store output 
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
    
    
# EG of how to use the functions from the isSpam class:

# a = isSpam(email_data["text"])

# a.get_common_words(5)
# a.text_to_dict()
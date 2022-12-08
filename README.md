# PIC16A_Project
Repository for Fall 2022 PIC16A final project.

# Predicting Spam Emails
## Olivia Weisiger, Madeline Chew, Yanming (Steven) Chen

### Description
This project aims to predict whether emails should be labeled as “spam” or not spam (“ham”). By exploring a dataset of emails labeled as “spam” or “ham,” graphing and wordcloud visualizations revealed that spam emails tend to have a higher frequency of misspelled words and include key advertising words such as “click.” From our exploration, we also discovered that vectoring email texts for prediction can be time-consuming and inefficient. So, after removing stopwords, we used TF-IDF vectorization to transform the text data to numerical vectors. For the supervised machine learning classification, we modeled Logistic Regression, Support Vector Machine, Multinomial Naive Bayes, Decision Tree, Random Forests, and K-Neighbors to label an email as “Spam” or “NOT Spam.”

### Python Packages Used
- numpy 1.21.5
- matplotlib 3.5.1
- pandas 1.4.2
- spellchecker 61.2.0
- string 3.9.12
- re 2.2.1
- Counter 1.0.0
- WordCloud 1.16.0
- stopwords from nltk.corpus 3.7
- sklearn 1.0.2

### Description of Demo File
To run the demo file, restart the kernel and run all cells. After doing so, the output will include exploratory data analysis (EDA) of our spam/ham emails dataset. The EDA includes charts detailing the frequency of misspelled words in spam vs ham emails and word clouds of most common words in spam emails compared to ham emails.

This figure is a graph comparing the number of misspellings in spam and ham emails, for the first 25 emails of the dataset (for efficiency because running the entire dataset will kill a Macbook Air). Since spam emails, blue, tend to have a higher number of misspellings compared to ham emails, red, the frequency of misspelled words would be a relevant variable to use to predict if an email is spam or ham.


From the Spam Word Cloud, we can see the most commonly used words in spam emails. Some include “click”, “pills”, and “price.” These words make sense in the context of spam emails, as they are usually advertisements that include a call-to-action so the user will ‘click’ to further investigate their product.


The remaining cells detail our process of building a model for our data using multiple methods, including Logistic Regression, Support Vector Machine (SVM), Multinomial Naive Bayes, Decision Tree, Random Forests, and K-Neighbors for our supervised learning classification task. From the prediction scores for each type of model, we found that SVM is the best model for this dataset, with an accuracy of approximately 98.06 %. 

Then, we play around with the predictive power of different models, to give an example of how different models will perform on the same classification task. For example, given an unlabeled email including the text “USC can beat UCLA,” the Decision Tree classifier model and our SVM model will predict the email to be spam. However, when the Multinomial Naive Bayes model is given the same input, it classifies the email as ham. Although the example input email is not necessarily spam or ham, it is interesting to see that models trained on the same data yield different results.

### Scope and Limitations 
Mislabeling an email could have ethical implications; if a spam email is categorized as ham, users are exposed to potentially dangerous phishing attacks, and if a ham email is categorized as spam, users will miss what might be important messages. Concerning accessibility, our model and dataset worked exclusively with emails that were written in English, so emails in other languages would not be able to be properly labeled. Potential extensions in the future could be expanding the project to include emails from other languages. 

In addition, a limitation to our project is the fact that the dataset contains 71% ham emails and only 29% spam emails. This means that our model might be biased towards identifying emails as ham, given that ham emails are more highly represented in the training data. Another limitation is that our emails were analyzed including “re :” for replied emails and “fw :” for forwarded emails so if a future email dataset only included the main message, no headers, then our model’s labeling might not be as accurate. 

Regarding overfitting, the models trained with the TF-IDF transformed data all showed very high training and testing scores. We believe one reason is that there are only ~5000 emails in this 5 MB dataset, which is too small for training a machine learning model. So, there is some “underfitting” in our model, meaning that our model can only be useful within this dataset. More data is needed if we want to build a more generalizable model for predicting emails. And the latest word2vec is a good choice for vectorizing email texts. 

### References
- How to zip to lists into dict: https://www.tutorialspoint.com/How-to-create-Python-dictionary-from-list-of-keys-and-values
- How to remove particular word from string: https://java2blog.com/remove-word-from-string-python/#:~:text=We%20can%20use%20the%20replace,empty%20character%20to%20remove%20it.&text=We%20can%20also%20specify%20how,to%20replace%20in%20the%20function.
- Techniques to clean text: https://stackoverflow.com/questions/12851791/removing-numbers-from-string, https://stackoverflow.com/questions/8115261/how-to-remove-all-the-escape-sequences-from-a-list-of-strings, https://stackoverflow.com/questions/8115261/how-to-remove-all-the-escape-sequences-from-a-list-of-strings, https://stackoverflow.com/questions/1546226/is-there-a-simple-way-to-remove-multiple-spaces-in-a-string
- Finding most frequent words: https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
- How to import python spell checker ‘pyspellchecker 0.7.0’ based Peter Norvig’s work: https://pypi.org/project/pyspellchecker/
- The Multinomial Naive Bayes result of 0.97 can be verified and similar to: https://www.kaggle.com/code/ansarisakib/spam-mail-dectection-by-naive-bayes 
- The Support Vector Classifier result of 0.98 can be verified is similar to: https://www.kaggle.com/code/alaatahaelmaria/emails-classification-ham-or-spam

### Background and Source of Data
Our dataset is an existing, public dataset found on Kaggle, from the Enron-Spam datasets, as described in the paper: V. Metsis, I. Androutsopoulos and G. Paliouras, "Spam Filtering with Naive Bayes - Which Naive Bayes?". Proceedings of the 3rd Conference on Email and Anti-Spam (CEAS 2006), Mountain View, CA, USA, 2006.

Source: https://www.kaggle.com/datasets/venky73/spam-mails-dataset

### Software Demo Video

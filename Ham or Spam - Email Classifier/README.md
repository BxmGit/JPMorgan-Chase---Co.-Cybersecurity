# Spam or Ham? Building an Email Classifier

## Introduction
In this project, my main objective was to build a functional prototype of an email classification system that can differentiate between spam and ham (non-spam) emails. Business Email Compromise (BEC) is a prevalent form of cybercrime, and my focus was on mitigating its impact through machine learning techniques.

## Background
BEC attacks typically manifest in various forms including CEO fraud, account compromise, false invoice schemes, attorney impersonation, and data theft. The primary entry point for these attacks is seemingly benign emails. With the complexity and variety of content that emails can carry, from text and headers to hyperlinks and attachments, building an effective detection system is a challenging task.

## Task Overview
I was tasked to:

1. Set up my development environment, ensuring all necessary tools, dependencies, and files were properly installed and configured.
2. Develop a machine learning model capable of classifying emails into two categories: spam and ham.

### Development Process
The process was methodically broken down into stages, making the task manageable and organized. 

1. **Data Preparation**: I traversed the dataset and created a Pandas dataframe to hold the email data.
2. **Data Cleaning**: I wrote a `preprocessor` function to normalize the text data, making it more suitable for machine learning models.
3. **Model Training**: I used the `CountVectorizer` to convert text samples into numerical vectors, and then trained a `LogisticRegression` model using scikit-learn.
4. **Evaluation**: I assessed the model's performance using various metrics like accuracy score, confusion matrix, and classification report.
5. **Feature Importance Analysis**: I delved into the model to understand which words (features) were deemed most important in classifying an email as spam or ham.

### Purpose
The primary goal was to learn about the stages involved in developing a machine learning model, applied in the context of email security — a critical area for organizations.

### Acheivements
By the end of this task, I successfully developed a machine learning model using scikit-learn, preprocessed the dataset for training, and evaluated the model's performance. I also gained insights into the model's decision-making process by analyzing the importance of different features.

### Conclusion
This project provided me with hands-on experience in building and evaluating a machine learning model for email classification, enhancing my skills in data preprocessing, model training, and performance evaluation. The insights gained from this project are invaluable for future endeavors in email security and machine learning applications.


# Email Classification using Naive Bayes

## Overview
This project is a machine learning-based solution for classifying emails into two categories: **spam** and **ham** (non-spam). The classification model is built using the **Naive Bayes** algorithm, a probabilistic machine learning method commonly used for text classification tasks. The goal is to train the model on a labeled dataset of emails and use it to predict the category of new, unseen emails.

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [How to Run the Project](#how-to-run-the-project)
- [File Structure](#file-structure)
- [Model Explanation](#model-explanation)
- [License](#license)

---

## Project Description

This project uses **Naive Bayes** for classifying emails into **spam** or **ham** categories. The dataset used for training is from Kaggle, containing labeled email messages with their corresponding categories. The entire process includes:
1. **Data Preprocessing**: Cleaning and transforming the email text into a format suitable for model training.
2. **Feature Extraction**: Converting the text data into numerical vectors using techniques like Bag-of-Words or TF-IDF.
3. **Model Training**: Using the preprocessed data to train a Naive Bayes model.
4. **Prediction**: Classifying new email messages as spam or ham based on the trained model.
5. **Evaluation**: Assessing the model's performance using accuracy and other metrics.

---

## Technologies Used

- **Python**: The primary programming language used for this project.
- **Jupyter Notebook**: For interactive development and testing of the code.
- **Scikit-learn**: For implementing the Naive Bayes classifier and other machine learning utilities.
- **Pandas**: For data manipulation and preprocessing.
- **Matplotlib/Seaborn**: For data visualization and model evaluation.
- **VSCode**: The code editor used for writing and testing the Python code.
- **Windows 10**: The operating system used for development.

---

## Dataset

- **Source**: The dataset used in this project is available on [Kaggle](https://www.kaggle.com).
- **Structure**: The dataset consists of two columns:
  - **Category**: Contains the label for each email, either "spam" or "ham".
  - **Message**: Contains the actual email text.
- **Size**: The dataset consists of 5,572 entries, with a distribution of 4,825 ham (non-spam) and 747 spam messages.
  
### Data Preprocessing
- Text normalization (lowercasing, removal of stopwords, and punctuation).
- Tokenization and vectorization using techniques like **Bag-of-Words** and **TF-IDF**.

---

## How to Run the Project

### Prerequisites
Before running the project, ensure that you have the following installed:
- Python 3.x
- Jupyter Notebook (or any compatible IDE)
- Required Python libraries:
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

You can install the required libraries using `pip`:
```bash
pip install pandas scikit-learn matplotlib seaborn
```

### Running the Code
1. Clone the repository:
   ```bash
   https://github.com/Hammadarshad026/Artificial-intelligence-project-NB-Mail-Classifier.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Artificial-intelligence-project-NB-Mail-Classifier
   ```
3. Open the Jupyter notebook:
   ```bash
   jupyter notebook Email-classifer.ipynb
   ```
4. Run the notebook cells sequentially to execute the code.

---

## File Structure

The project contains the following files and folders:
- **Email-classifer.ipynb**: The main Jupyter notebook file containing the project code.
- **dataset.csv**: The email dataset used for training the model (you can upload the dataset from Kaggle and name it as `dataset.csv`).
- **README.md**: This file.

---

## Model Explanation

### Naive Bayes Algorithm
The Naive Bayes classifier is based on Bayes' Theorem and assumes that the presence of a word in an email is independent of the presence of other words. The model is trained by calculating the likelihood of each class (spam or ham) given the words in the email, and it predicts the class that has the highest probability.

### Steps:
1. **Data Preprocessing**: The email text is cleaned and tokenized into words. Stop words and punctuation are removed.
2. **Feature Extraction**: The text data is converted into numerical features using the Bag-of-Words model or TF-IDF.
3. **Model Training**: The Naive Bayes classifier is trained on the processed data, where the model learns to distinguish spam from ham.
4. **Prediction**: Once trained, the model can classify new, unseen emails into either spam or ham.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


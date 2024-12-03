# Email Classification using Naive Bayes

## Overview
This project is designed to classify emails as either **spam** or **ham** (not spam). It uses a **Naive Bayes** model trained on a dataset of email messages. The system predicts whether an input email is spam or legitimate based on the content.  

Additionally, it includes a fun and interactive user interface in the command line using ASCII art and colors to display results.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How the System Works](#how-the-system-works)
  - [File Descriptions](#file-descriptions)
  - [Model Usage](#model-usage)
- [How to Run the Project](#how-to-run-the-project)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features
- **Text Classification**: Classifies emails into spam or ham categories using a trained Naive Bayes model.
- **Preprocessing**: A `text_formatter.py` script ensures input text is clean and formatted properly for analysis.
- **Interactive Output**: Displays results using visually appealing ASCII art and colored text.
- **User-Friendly Design**: Straightforward and easy-to-use command-line interface.

---

## Technologies Used
- **Python**: Programming language for building and implementing the system.
- **Scikit-learn**: For training and using the Naive Bayes classification model.
- **pandas**: For handling and preprocessing the dataset.
- **pickle**: To save and load the trained model and vectorizer.
- **pyfiglet**: For creating ASCII art to display interactive outputs.
- **termcolor**: For adding color to the terminal outputs.
- **Jupyter Notebook**: For developing and training the model.
- **Windows 10**: Operating system for development.

---

## How the System Works

### File Descriptions
1. **`Email-classifer.ipynb`**:
   - A Jupyter Notebook that contains code for training the Naive Bayes model.
   - Produces the `trained_model.pkl` and `vectorizer.pkl` files, which are used later for predictions.

2. **`text_formater.py`**:
   - Contains the `reformat_text` function that formats and cleans the input email text.
   - Ensures unnecessary whitespace, extra line breaks, and punctuation inconsistencies are resolved.

3. **`model.py`**:
   - A command-line program that:
     - Loads the saved Naive Bayes model and vectorizer.
     - Accepts user input (an email message) and reformats it using `text_formatter.py`.
     - Predicts whether the email is spam or ham.
     - Displays the result using ASCII art and colorful text.

---

### Model Usage

To see how the system works, run **`model.py`** in your terminal. Here's a breakdown of what happens:
1. A welcome banner **`HAMMAD`** is displayed in ASCII art.
2. The user enters an email message.
3. The system processes the input, predicts if it's spam or ham, and displays the result interactively.

## How to Run the Project

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Required libraries:
  ```bash
  pip install pandas scikit-learn pickle pyfiglet termcolor
  ```

### Steps to Run
1. Clone the repository:
   ```bash
   https://github.com/Hammadarshad026/Artificial-intelligence-project-NB-Mail-Classifier.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Artificial-intelligence-project-NB-Mail-Classifier
   ```
3. Ensure the trained model and vectorizer files (`trained_model.pkl` and `vectorizer.pkl`) are in the project folder.
4. Run `model.py`:
   ```bash
   python model.py
   ```

---

## Screenshots
### Input and Output of the System:
![image](https://github.com/user-attachments/assets/8c34c25c-ec09-4967-8302-a7131a956c44)



## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

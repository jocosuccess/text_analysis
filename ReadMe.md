# TextualAnalysis

## Overview

This project is to analysis text files.

After reading the text from the text files in the directory, this project processes the text by removing meaningless sentences.
Then this counts the loughran words from the text preprocessed according to the Loughran-McDonald Sentiment Word Lists.xlsx.
Finally, this estimates the Fog and Kincaid index of text.

## Project Structure
- src

    The part to analyze the text

- input_txtfile

    The text files for analysis
    
- output_txtfile

    The excel file to save the result
    
- utils
    
    The file manager(import the result into the excel file) and Loughran-McDonald Sentiment Word Lists

- main

    The main execution file

- requirements.txt

    All the libraries for this project

## Project Installation

- Environment

    Ubuntu 18.04, Python 3.6

- Dependency Installation
    
    ```
        pip3 install -r requirements.txt 
    ```    

    The main necessary dependencies are textstat, spacy, Tokenizer, xlsxwriter, openpyxl.
    
    ### Install en_core_web_sm dependencies
        
            o windows 10
                
                $ python -m install spacy download en
            
            o ubuntu 18.04
            
                $ python -m install spacy download en_core_web_sm 
    
## Project Execution

- In terminal, please run the following command in this project directory.

    ```
        python3 main.py
    ```
    
- output

    In terminal, text files to analysis are shown.
    The analysis result is saved in the output_excelfile directory.
    
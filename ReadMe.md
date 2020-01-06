## Description

This project is to analysis text files.

After reading text from text files in directory, project processes text by removing meaningless sentences.
Then this calculates loughran words from text preprocessed according to Loughran-McDonald Sentiment Word Lists.xlsx.
Finally, this estimates Fog and Kincaid index of text.

## Project Structure
-application directory:

python file

-input_txtfile

text files directory to need analysis
    
-output_txtfile

Excel file directory to show result
    
-utils
    
python files & Loughran-McDonald Sentiment Word Lists.xlsx.

-main.py

python file to execute project

-requirements.txt

libraries necessary for executing project

## Project Settings

-Setting up python

python version is above 3.5

-Setting python interpreter into project

File/Settings(Ctrl+Alt+s)/Project/Project Interpreter

-Installing libraries

In terminal, input following command line.

    pip install <library name>
    
Library names are in requirements.txt

The main necessary libraries are textstat, spacy, Tokenizer, ntpath, xlsxwriter, openpyxl, en_core_web_sm.
    
## Run Project

Run main.py

    python main.py
    
In terminal, text files to analysis are shown.
Project result is saved in output_excelfile directory.

## install additional dependencies

- en-core-web-sm

    o windows 10
        
        $ python -m install spacy download en
    
    o ubuntu 16.04.05
    
        $ python -m install spacy download en_core_web_sm 
    
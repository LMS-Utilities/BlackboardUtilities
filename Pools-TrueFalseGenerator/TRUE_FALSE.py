"""
This script formats "TRUE_FALSE" questions for Blackboard.

It produces a TSV file that you can upload to a Blackboard pool.

https://help.blackboard.com/Learn/Instructor/Tests_Pools_Surveys/Reuse_Questions/Upload_Questions
"""

import random, csv, math
random.seed(200202) # <yr><sem>

# Location to write the question pool (use an extension .txt)
OUTPUT_FILE = r'TRUE_FALSE.txt'

# The number of questions to generate
NUMBER_QUESTIONS = 50

def htmlFormatCode(txt):
    """Generate HTML for formatting "code"

    Args:
        txt:
            String. The content to codify.
            
    Returns:
        String. HTML-formatted.
    """
    
    return f'<span style="border: 1px solid grey; border-radius: 5px; padding: 3px; font-family: Courier New;">{txt}</span>'


def html2dArrayToTable(twoDimensionalArray, firstRowBold=True, firstColumnBold=False):
    """Generate the FIB_PLUS format

    Args:
        twoDimensionalArray:
            A list of lists.
            The first dimension correlates with a row.
            The second dimension correlates with a column.
        
        firstRowBold:
            If true, the contents of the first row will be wrapped in <b>
            
        firstColumnBold:
            If true, the contents of the first column will be wrapped in <b>
            
    Returns:
        String. HTML-formatted table.
    """
    
    html = '<table style="border: 1px solid #cdcdcd; padding: 3px; border-spacing: 0px; margin-top: 2em; margin-bottom: 2em" cellpadding="5em">'
    for nbRow in range(0, len(twoDimensionalArray)):
        row = twoDimensionalArray[nbRow]
        
        if nbRow == 0 and firstRowBold:
            row = [f'<b>{col}</b>' for col in row]
            
        for nbCol in range(0, len(row)):
            if nbCol == 0 and firstColumnBold and nbRow != 0:
                row[0] = f'<b>{row[0]}</b>'
        
        cols = ''.join([f'<td>{x}</td>' for x in row])
        html += f'<tr>{cols}</tr>'
    html += '</table>'
    return html


def bbTrueFalseFormat(txtQuestion, isTrueTheCorrectAnswer=True):
    """
    Generate the FIB_PLUS format

    Args:
        txtQuestion: 
            The formatted question (HTML is allowed, linebreaks are not).
            
        twoDimAnswers: 
            A list of lists. 
            The first dimension corresponds to each response box. 
            The second dimension is the list of acceptable answers.
            
    Returns:
        String. TSV formatted.
    """
    
    # the correct answer is...
    # (we'll manually convert bool to str here, just in case...)
    answer = "true" if isTrueTheCorrectAnswer else "false"
    
    # start formatting the FIB_PLUS question
    bbItem = f'TF\t{txtQuestion}\t{answer}\n'
  
    
    return bbItem


def generateQuestionPool():
    """Generates the question pool"""
    with open(OUTPUT_FILE, 'w+') as f:
        for i in range(1, NUMBER_QUESTIONS+1):
            
            dataset = htmlFormatCode(f"reads_{i:03}_R1.fastq.tgz")
            
            question = f"<b>You have been allocated the dataset {dataset}</b><br><br>Do not proceed until you have downloaded this file.<br><br>Click True when you're ready."

            f.write(bbTrueFalseFormat(question))
            print(bbTrueFalseFormat(question))

if __name__ == "__main__":
    generateQuestionPool()
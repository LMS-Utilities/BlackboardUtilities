"""
This script formats "fill in multiple blanks" questions for Blackboard.

It produces a TSV file that you can upload to a Blackboard pool.

From the Blackboard documentation: 
    FIB_PLUS TAB question text TAB variable1 TAB answer1 TAB answer2 TAB TAB variable2 TAB answer3

    The format consists of a list of variable-answers where each variable-answer is composed of the 
    variable name and a list of correct answers for that variable. Variable-answers are delimited 
    by an empty field.

    The maximum number of variables is 10.
https://help.blackboard.com/Learn/Instructor/Tests_Pools_Surveys/Reuse_Questions/Upload_Questions
"""

import random, csv, math
random.seed(200202) # <yr><sem>

# Location to write the question pool (use an extension .txt)
OUTPUT_FILE = r'FIB_PLUS.txt'

# The number of questions to generate
NUMBER_QUESTIONS = 25

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


def bbFibPlusFormat(txtQuestion, twoDimAnswers):
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
    
    alphabet = list(map(chr, range(65, 90)))
    
    # make sure there are no linebreaks in the question
    txtQuestion = txtQuestion.replace('\n', '<br>')
    
    # how many responses are there in the question?
    numResponses = len(twoDimAnswers)
    
    # start formatting the FIB_PLUS question
    bbItem = f'FIB_PLUS\t{txtQuestion}\t'
    
    # check that the Blackboard response tag exists for each
    # it is formatted as: [A], [B], [C] etc
    for i in range(numResponses):
        assert(f'[{alphabet[i]}]' in txtQuestion)
        
        bbItem += f'{alphabet[i]}\t'
        
        bbItem += '\t'.join(map(str, twoDimAnswers[i]))
        
        bbItem += '\t\t'
    
    bbItem += '\n'
    
    return bbItem


def generateQuestionPool():
    """Generates the question pool"""
    with open(OUTPUT_FILE, 'w+') as f:
        for i in range(NUMBER_QUESTIONS):
            spellings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                         'seventeen', 'eighteen', 'nineteen', 'twenty']
            
            nums = random.sample(range(1, 20), 4)
            
            htmlNums = [
                htmlFormatCode(str(x)) 
                for x in nums
            ]
            
            answers = [
                [spellings[x-1]]
                for x in nums
            ]
            
            htmlTable = html2dArrayToTable(
                [
                    ['Number', 'Response'],
                    [htmlNums[0], '[A]'],
                    [htmlNums[1], '[B]'],
                    [htmlNums[2], '[C]'],
                    [htmlNums[3], '[D]'],
                ]
            )
            
            question = f'Provide the English spelling of the numbers in the table below.<br><br>{htmlTable}'

            f.write(bbFibPlusFormat(question, answers))
            print(bbFibPlusFormat(question, answers))

if __name__ == "__main__":
    generateQuestionPool()
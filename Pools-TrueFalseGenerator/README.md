# Blackboard - Generate bulk true/false questions for a pool

## Context

You may wish to create a question pool of true/false questions, with each question having some variation.

The process of making the variations and calculating the new answers is a tedious task, so instead, here is a tool which will assist in automating the process.


## Solution

The tool allows you to specify the question text and the correct answer.

HTML is supported. There is a method for converting a 2-dimensional Python list to a HTML table, and another for prettifying a string as code.

This tool assists you in constructing the tab-separated values (TSV) file for Blackboard (read [here](https://help.blackboard.com/Learn/Instructor/Tests_Pools_Surveys/Reuse_Questions/Upload_Questions) about the format and how to upload).

The Blackboard convention of using `[A]`, `[B]`, `[C]`, etc. to indicate where the blank should be is still used.


## How to

1. Clone the repo to your machine

   `git clone https://github.com/LMS-Utilities/BlackboardUtilities.git` or click [here](https://github.com/LMS-Utilities/BlackboardUtilities/archive/master.zip)

2. Ensure that you have [Python 3](https://www.python.org/downloads/) installed

3. Navigate to the `Pools-TrueFalseGenerator` directory

4. Modify the contents of the `TRUE_FALSE.py` script. 
   
   There are settings at the top and a method `generateQuestionPool` at the bottom. 
   
   You need some skill in Python programming for this.
   


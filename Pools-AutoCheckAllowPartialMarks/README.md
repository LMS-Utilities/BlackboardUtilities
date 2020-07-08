# Blackboard - Auto-check the *Allow partial marks* option

## Context

When performing a bulk-upload of questions into a question Pool (read [here](https://help.blackboard.com/Learn/Instructor/Tests_Pools_Surveys/Reuse_Questions/Upload_Questions) how to do this), it is not possible to enable *Allow partial marks*. This may be desired for questions of type *Fill in Multiple Blanks*, where you wish to award marks for those "blanks" that the student answered correctly. Without enabling *allow partial marks*, the student will receive zero for the entire question if any of their responses are incorrect.



## Solution

In this repository, there is a Jupyter notebook which uses the Selenium ([docs](https://selenium-python.readthedocs.io/)) library to auto-check the *Allow partial marks* option for questions in a Pool.

Jupyter allows for an interactive Python session, which is useful in the case something goes wrong.

Selenium is an automated testing tool which uses a WebDriver to interact with web pages. In this case, I use Selenium to read the table of questions for a given pool and auto-check the *allow partial marks* option.



## How to

1. Clone the repo to your machine

   `git clone https://github.com/LMS-Utilities/BlackboardUtilities.git` or click [here](https://github.com/LMS-Utilities/BlackboardUtilities/archive/master.zip)

2. Ensure that you have [Python 3](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/) installed

3. Navigate to the `Pools-AutoCheckAllowPartialMarks` directory

4. Download the ChromeDriver for Selenium, [here](https://chromedriver.chromium.org/).

   Extract the contents of the ZIP-archive into the `Pools-AutoCheckAllowPartialMarks` directory.

5. A Python dependency list exists. Use Pip to install the dependencies.

   On Windows (with Windows Python Launcher installed):

   ```
   py -3 -m venv .venv
   .venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```

   On Unix:

   ```
   py -3 -m venv .venv
   source .venv/bin/activat
   epip install -r requirements.txt
   ```


6. Run Jupyter and launch the notebook

   ```
   jupyter notebook
   ```

7. Run the first cell to import the needed libraries

8. Replace `___YOUR_BLACKBOARD_URL___` and run the cell. 

   If this is successful, an instance of Google Chrome will launch. Authenticate into Blackboard and navigate to your question pool. Make sure that you can see the table of questions in this Chrome browser.

9. Run the third cell. You should see the Chrome browser navigating through the question editor for each question in the table. The *allow partial marks* option will be ticked.

10. If you add dependencies to the Pip environment, make sure you update the `requirements.txt` file

    ```py
    pip freeze > requirements.txt
    ```

    

## Limitations

This only works for pools with 25 questions (or whatever the default pagination size is for your install of Blackboard).

There is some commented-out code that clicks the 'Show All' button to expand the questions table, but, it seems to stop things from working...
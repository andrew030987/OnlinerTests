Inside this repo is a script that automates 10 test cases to test onliner's basket (www.onliner.by). Script is called test_suite_onliner.py. File with test cases you may find in docs/ folder. 

Here is the instruction on how to launch the script:

1. Download Python3 installation file from official site. 
If you already have Pyhton installed please make sure you are using version 3.6 or higher. Update your Python in case you have older version. Important! During installation make sure you have chosen Add Python 3.x to PATH option.

2. Download ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads.
Make sure you download the correct version for your browser. Create a new directory called chromedriver on C: and unpack downloaded chromedriver.exe file to this directory (C:\chromedriver). Add C:\chromedriver dir to your PATH system variable. You may check how to do it for different Windows versions here: 
https://www.computerhope.com/issues/ch000549.htm. 

3. Open cmd terminal.
You may create a separate virtual environment for this step.
Type: "pip install selenium" and press enter. This will install selenium library.
Type: "pip install pytest==5.1.1" and press enter. This will install pytest library.

4. To start execution of tests type "pytest -s -v --tb=line src/test_suite_onliner.py" from project directory and press enter in terminal. It is recommended to close all other programs and browsers on your computer before executing the test suite. 

5. After tests were executed, a text file called "report.txt" has been created in scr/ folder. It shows if all of the tests passed successfully.

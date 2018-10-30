# About
This repository is created for submission towards qualification to Insight Data Engineering Fellowship program. I have included 4 folders and 1 shell script. Below I have described content of each folder. To checkout the problem statement and sample input-output please visit [here](https://github.com/InsightDataScience/h1b_statistics)

# input
Right now this folder contains a blank CSV file. To create the hirarchy as per guideline. Sample input is available in [insight_testsuite] (README.md#insight_testsuite). About input, Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). 
For your convenience we converted the Excel files into a semicolon separated (";") format and placed them into this Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing). However, do not feel limited to test your code on only the files we've provided on the Google drive
**Note:** Each year of data can have different columns. Check **File Structure** docs before development. 

# insight_testsuite
This folder contain test cases for the script. Though, it has only one test case for now as provided by Insight. My tested files are larger and hence not included here. The shell script in this folder check for repo structure.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 
    
On a failed test, the output of `run_tests.sh` should look like:

    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed

On success:

    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed
  
# output
In this folder, script will store the outputs for the data from input folder. This folder contain 2 .txt files with title: top_10_occupations.txt & top_10_states.txt

# src
This folder contain my python script that produce the txt file for given input csv data. In the python script I have used two function. One for calculating top 10 most frequent words in a given list and second that process the csv and compile the txt output.

**Please feel free to ask questions at: [himanshuajmera8@gmail.com](himanshuajmera8@gmail.com)**

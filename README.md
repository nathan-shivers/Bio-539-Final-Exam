# Bio-539-Final-Exam
This repository conatins code and example data for a script to compute the linguistic complexity of a sequence of nucleic acids from the terminal. 

## Getting Started
These instructions will get you a copy of the script and how to use it.

### Prerequisites
This script requires the installation of ```Python 3```. 

### Installing
Clone the repository and change the directory of the terminal to the location of the cloned repository. Then run this command on the terminal to run the script.
```$python Final_Exam.py Test_file.txt```

The linguistic complexity of each sequence for Test_file.txt should be outputed on the terminal. 
Additional nucleic acids sequence can be put in place of Test_file.txt as long as each sequence has its own line.

### Testing
An additonal ```Pystest``` script was included in the repositort to test the functions created in the main script. 
To run this script, have the directory of the terminal to the location of the cloned repository and run this command.
```$pytest Pytest_Final_Exam.py```
Pytest will be run and report if all the functions passed the conditional tests or if there were errors.

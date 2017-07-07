Hey there! Here is the new version of the code for the AXA data challenge and guess what! IT WORKS FINE!!

In this file you'll find:   - set up requirements
                            - a detail of each class
                            - the steps to follow in order to make a prediction

__________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________

SET UP REQUIREMENTS:
After cloning the repo, you need to put the original "train_2011_2012_2013.csv" in the data/ folder. You also need to make sure
that the original "submission.txt" (downloaded on moodle) file is in this folder as well and under the name "submission_original.txt"

__________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________

DETAIL OF CLASSES:
date.py is the original date class (written by P. Hennebert himself). Nothing changed.

change_submission_date.py has two functions in order to change the format of a submission file (from date to timestamp and
the other way round).

build_train_csv.py takes the original csv in argument and writes a file called 'train.csv'. Only the lines about an interesting
ASS_ASSIGNMENT are kept. For each line (and subsequently for each date) we keep 'ASS_ASSIGNEMENT', 'CSPL_RECEIVED_CALLS', HOUR and we
add the necessary columns to binarize the attributes 'WEEKDAY' and 'MONTH'.

build_sub_csv.py build a csv from the file 'submission_original.csv'. In this csv, the columns are DATE, ASS_ASSIGNMENT, prediction,
hour, and the attributes 'month' and 'weekday' binarized.

axa.py is the main file. In this file the main function loads the 'train.csv' file. groups the lines by date and ass_assignment
and then does the prediction for all the dates. In the process some temporary csv are created but the final prediction is in the
file 'prediction_final.txt'.

__________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________

STEPS TO MAKE A PREDICTION:
Here is the order of the files to run in order to make a prediction:
- build_sub_csv.py
- build_train_csv.py
- axa.py

The final prediction is in 'data/prediction_final.txt'

In the submitted version, the RandomForestRegressor is used and dilatation factor is 1,6.

#!/usr/bin/env python3
from pathlib import Path
import csv, re

def read_covid_cases():
    # dictionary of states to average cases
    states = {}

    paths = Path('US_COVID_CASES_AS_OF_2021_10_31').glob('*.csv')
    for path in paths:
        # because path is object not string
        file_path = str(path)
        # Do thing with the path
        #print(file_path)

        
        with open(file_path, newline='') as csvfile:
            # parse state from filename
            stateSearch = re.search(".*ST__(.*)_530", csvfile.name)
            state = stateSearch.group(1)
            state = state.replace("_", " ")


            spamreader = csv.reader(csvfile, delimiter=',')
            # Skips the first row which is the header
            # YYYYMMDD,NewCases,MovingAvgOfCases,NewDeaths,AvgNewDeaths
            next(spamreader)
            first_row = next(spamreader)
            case_avg = first_row[1]

            # store average cases per state
            states[state] = case_avg
    
    return states

# read in covid cases from csv files
states = read_covid_cases()
#print(states)

# write csv data
with open('my-data-vals.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['state', 'value'])
    for key, value in states.items():
        spamwriter.writerow([key, value])


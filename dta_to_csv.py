import pandas as pd # converting files
import sys # get parameters
import os # get filename

print('Enter the .dta file name:')

dta_file = input()
data = pd.io.stata.read_stata(dta_file)

csv_file = os.path.splitext(dta_file)[0] + '.csv'
data.to_csv(csv_file)
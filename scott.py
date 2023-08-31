import os
import pwd
import pandas as pd


df = pd.read_csv('../characters.csv')

location = os.path.abspath(os.getcwd())


df['Gender'] = ['Male', 'Female', 'Male', 'Female']

print('I am in ' + location)
print(df)
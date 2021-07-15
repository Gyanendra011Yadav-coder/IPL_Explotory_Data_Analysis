import numpy as np
import pandas as pd
import matplotlib as plt

#READING THE FILE, BY PROVIDING THE ADDRESS OF THE FILE IN THE SYSTEM
read_data=pd.read_csv('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Data Sets For Analysis\\IPL DATA\\matches.csv')
#USING THIS pd.set_set_option, WE ARE JUST MAKING THE ALL ROWS AND COLUMNS PRINT COMPLETLY
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#PRINTING THE DATA OF THE CSV FILE
print(read_data.head(2))


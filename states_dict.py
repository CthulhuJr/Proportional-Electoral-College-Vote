#use with electdfcopy.py, trying to apply 

import numpy as np 
import pandas as pd

pd.set_option('display.max_rows', None)

states727680 = {
'California': 45,
'Texas': 26,
'Florida': 17,
'New York': 41,
'Illinois': 26,
'Pennsylvania':	27,
'Ohio':	25,
'Georgia': 12,
'Michigan':	21,
'North Carolina': 13,
'New Jersey': 17,
'Virginia': 12,
'Arizona': 6,
'Tennessee':10,
'Indiana': 13,
'Massachusetts': 14,
'Washington': 9,
'Minnesota': 10,
'Missouri': 12,
'Wisconsin': 11,
'Maryland': 10,
'Colorado': 7,
'Alabama': 9,
'South Carolina': 8,
'Kentucky': 9,
'Oregon': 6,
'Oklahoma': 8,
'Connecticut': 8,
'Nevada': 3,
'Utah': 4,
'Kansas': 7,
'Iowa': 8,
'Arkansas': 6,
'Louisiana': 10,
'Mississippi': 7,
'New Mexico': 4,
'Nebraska': 5,
'West Virginia': 6,
'Idaho': 4,
'Rhode Island': 4,
'New Hampshire': 4,
'Maine': 4,
'Hawaii': 4,
'Montana': 4,
'Wyoming': 3,
'South Dakota': 4,
'North Dakota':	3,
'DISTRICT OF COLUMBIA': 3,
'Delaware':	3,
'Vermont': 3,
'Alaska': 3}
statevotes727680 = {k.upper():v for k,v in states727680.items()}
statevotes72 = pd.DataFrame.from_dict(statevotes727680, orient='index', columns=['electoral_votes'])
statevotes72['year'] = 1972
statevotes76 = statevotes72.copy()
statevotes80 = statevotes72.copy()
statevotes76['year'] = 1976
statevotes80['year'] = 1980

states8488 = {
'California': 47,
'Texas': 29,
'Florida': 21,
'New York': 36,
'Illinois': 24,
'Pennsylvania':	25,
'Ohio':	23,
'Georgia': 12,
'Michigan':	20,
'North Carolina': 13,
'New Jersey': 16,
'Virginia': 12,
'Arizona': 7,
'Tennessee':11,
'Indiana': 12,
'Massachusetts': 13,
'Washington': 10,
'Minnesota': 10,
'Missouri': 11,
'Wisconsin': 11,
'Maryland': 10,
'Colorado': 8,
'Alabama': 9,
'South Carolina': 8,
'Kentucky': 9,
'Oregon': 7,
'Oklahoma': 8,
'Connecticut': 8,
'Nevada': 4,
'Utah': 5,
'Kansas': 7,
'Iowa': 8,
'Arkansas': 6,
'Louisiana': 10,
'Mississippi': 7,
'New Mexico': 5,
'Nebraska': 5,
'West Virginia': 6,
'Idaho': 4,
'Rhode Island': 4,
'New Hampshire': 4,
'Maine': 4,
'Hawaii': 4,
'Montana': 4,
'Wyoming': 3,
'South Dakota': 3,
'North Dakota':	3,
'DISTRICT OF COLUMBIA': 3,
'Delaware':	3,
'Vermont': 3,
'Alaska': 3}
statevotes8488 = {k.upper():v for k,v in states8488.items()}
statevotes84 = pd.DataFrame.from_dict(statevotes8488, orient='index', columns=['electoral_votes'])
statevotes84['year'] = 1984
statevotes88 = statevotes84.copy()
statevotes88['year'] = 1988


states929600 = {
'California': 54,
'Texas': 32,
'Florida': 25,
'New York': 33,
'Illinois': 22,
'Pennsylvania':	23,
'Ohio':	21,
'Georgia': 13,
'Michigan':	18,
'North Carolina': 14,
'New Jersey': 15,
'Virginia': 13,
'Arizona': 8,
'Tennessee':11,
'Indiana': 12,
'Massachusetts': 12,
'Washington': 11,
'Minnesota': 10,
'Missouri': 11,
'Wisconsin': 11,
'Maryland': 10,
'Colorado': 8,
'Alabama': 9,
'South Carolina': 8,
'Kentucky': 8,
'Oregon': 7,
'Oklahoma': 8,
'Connecticut': 8,
'Nevada': 4,
'Utah': 5,
'Kansas': 6,
'Iowa': 7,
'Arkansas': 6,
'Louisiana': 9,
'Mississippi': 7,
'New Mexico': 5,
'Nebraska': 5,
'West Virginia': 5,
'Idaho': 4,
'Rhode Island': 4,
'New Hampshire': 4,
'Maine': 4,
'Hawaii': 4,
'Montana': 3,
'Wyoming': 3,
'South Dakota': 3,
'North Dakota':	3,
'DISTRICT OF COLUMBIA': 3,
'Delaware':	3,
'Vermont': 3,
'Alaska': 3}
statevotes929600 = {k.upper():v for k,v in states929600.items()}
statevotes92 = pd.DataFrame.from_dict(statevotes929600, orient='index', columns=['electoral_votes'])
statevotes92['year'] = 1992
statevotes96 = statevotes92.copy()
statevotes00 = statevotes92.copy()
statevotes96['year'] = 1996
statevotes00['year'] = 2000


states0408 = {
'California': 55,
'Texas': 34,
'Florida': 27,
'New York': 31,
'Illinois': 21,
'Pennsylvania':	21,
'Ohio':	20,
'Georgia': 15,
'Michigan':	17,
'North Carolina': 15,
'New Jersey': 15,
'Virginia': 13,
'Arizona': 10,
'Tennessee':11,
'Indiana': 11,
'Massachusetts': 12,
'Washington': 11,
'Minnesota': 10,
'Missouri': 11,
'Wisconsin': 10,
'Maryland': 10,
'Colorado': 9,
'Alabama': 9,
'South Carolina': 8,
'Kentucky': 8,
'Oregon': 7,
'Oklahoma': 7,
'Connecticut': 7,
'Nevada': 5,
'Utah': 5,
'Kansas': 6,
'Iowa': 7,
'Arkansas': 6,
'Louisiana': 9,
'Mississippi': 6,
'New Mexico': 5,
'Nebraska': 5,
'West Virginia': 5,
'Idaho': 4,
'Rhode Island': 4,
'New Hampshire': 4,
'Maine': 4,
'Hawaii': 4,
'Montana': 3,
'Wyoming': 3,
'South Dakota': 3,
'North Dakota':	3,
'DISTRICT OF COLUMBIA': 3,
'Delaware':	3,
'Vermont': 3,
'Alaska': 3}
statevotes0408 = {k.upper():v for k,v in states0408.items()}
statevotes04 = pd.DataFrame.from_dict(statevotes0408, orient='index', columns=['electoral_votes'])
statevotes04['year'] = 2004
statevotes08 = statevotes04.copy()
statevotes08['year'] = 2008

states121620 = {
'California': 55,
'Texas': 38,
'Florida': 29,
'New York': 29,
'Illinois': 20,
'Pennsylvania':	20,
'Ohio':	18,
'Georgia': 16,
'Michigan':	16,
'North Carolina': 15,
'New Jersey': 14,
'Virginia': 13,
'Arizona': 11,
'Tennessee':11,
'Indiana': 11,
'Massachusetts': 11,
'Washington': 10,
'Minnesota': 10,
'Missouri': 10,
'Wisconsin': 10,
'Maryland': 10,
'Colorado': 9,
'Alabama': 9,
'South Carolina': 9,
'Kentucky': 8,
'Oregon': 7,
'Oklahoma': 7,
'Connecticut': 7,
'Nevada': 6,
'Utah': 6,
'Kansas': 6,
'Iowa': 6,
'Arkansas': 6,
'Louisiana': 6,
'Mississippi': 6,
'New Mexico': 5,
'Nebraska': 5,
'West Virginia': 5,
'Idaho': 4,
'Rhode Island': 4,
'New Hampshire': 4,
'Maine': 4,
'Hawaii': 4,
'Montana': 3,
'Wyoming': 3,
'South Dakota': 3,
'North Dakota':	3,
'DISTRICT OF COLUMBIA': 3,
'Delaware':	3,
'Vermont': 3,
'Alaska': 3}

statevotes121620 = {k.upper():v for k,v in states121620.items()}
statevotes12 = pd.DataFrame.from_dict(statevotes121620, orient='index', columns=['electoral_votes'])
statevotes12['year'] = 2012
statevotes16 = statevotes12.copy()
statevotes20 = statevotes12.copy()
statevotes16['year'] = 2016
statevotes20['year'] = 2020

#statevotes12.reset_index(inplace=True)
#statevotes12 = statevotes12.rename(columns = {'index':'state'})
#statevotes12 = statevotes12.set_index('state')

#print(statevotes12)



statevotes = [statevotes12, statevotes16, statevotes20, statevotes04, statevotes08, statevotes92, statevotes96, statevotes00, statevotes84, statevotes88, statevotes72, statevotes76, statevotes80]

statevotesdf = pd.concat(statevotes)
statevotesdf['year'].astype(str)

statevotesdf.reset_index(inplace=True)
statevotesdf = statevotesdf.rename(columns = {'index':'state'})
statevotesdf = statevotesdf.set_index('year')

#print(statevotesdf)
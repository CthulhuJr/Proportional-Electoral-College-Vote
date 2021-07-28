#sets up the dataframe and processes all the results to export to a cleaned-up dataframe

import numpy as np 
import pandas as pd
from states_dict import statevotesdf

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

electdf = pd.read_csv('election data.csv', index_col=0)
electdf = electdf.drop(columns = ['state_fips', 'state_po','state_cen', 'state_ic', 'office', 'version', 'notes', 'party_simplified', 'writein']) #deletes superfluous columns
electdf = electdf.fillna('WRITE-IN')
electdf = electdf[electdf.candidate != 'WRITE-IN']								#delete rows with various write-in and incomplete votes
electdf = electdf[electdf.candidate != 'OTHER']
electdf = electdf[electdf.candidate != 'BLANK VOTE/SCATTERING']
electdf = electdf[electdf.candidate != 'NOT DESIGNATED']

electdf.loc[:, 'percvotes'] = (electdf['candidatevotes']/electdf['totalvotes'] * 100)

electdf['state'] = electdf['state'].str.upper()									#adjusts state names to match dictionary
electdf = pd.merge(electdf, statevotesdf, how='left', on=['year', 'state'])

electdf['perc_e_votes'] = (electdf['electoral_votes'] * (electdf['percvotes']/100))
electdf['vote_frac'] = electdf['perc_e_votes'] % 1
electdf['vote_int'] = electdf['perc_e_votes'].astype(int)

results = {}
grouped = electdf.groupby(["year", "state"])									#shows breakdown by each state for each year
for key, group in grouped:
	year, state = key
	group['vote_remaining'] = group['electoral_votes'] - group['vote_int'].sum()
	remaining = group['vote_remaining'].iloc[0]
	top_fracs = group['vote_frac'].nlargest(remaining)
	group['total'] = (group['vote_frac'].isin(top_fracs)).astype(int) + group['vote_int'] 
	if year not in results:
		results[year] = {} 											#filters out candidates without votes
	for candidate, evotes in zip(group['candidate'], group['total']):
		if candidate not in results[year] and evotes:
			results[year][candidate] = 0
		if evotes:
			results[year][candidate] += evotes
			

electdf.to_csv("electoral_votes_results.csv")

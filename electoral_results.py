import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

electdf = pd.read_csv('electoral_votes_results.csv', index_col=0)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)



results = {}
grouped = electdf.groupby(["year", "state"])															#shows breakdown by each state for each year
for key, group in grouped:
	year, state = key
	group['vote_remaining'] = group['electoral_votes'] - group['vote_int'].sum()
	remaining = group['vote_remaining'].iloc[0]
	top_fracs = group['vote_frac'].nlargest(remaining)
	group['total'] = (group['vote_frac'].isin(top_fracs)).astype(int) + group['vote_int'] 
	if year not in results:
		results[year] = {} 															#filters out candidates without votes
	for candidate, evotes in zip(group['candidate'], group['total']):
		if candidate not in results[year] and evotes:
			results[year][candidate] = 0
		if evotes:
			results[year][candidate] += evotes


print(results)
# Proportional-Electoral-College-Vote
This project explores the results of a proportional electoral college vote for Presidential elections going back to 1976.

Electoral data obtained from the [Harvard Dataverse.](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX)

The purpose of this project is to determine the results of Presidential elections if the electoral college votes were given out as a proportion of votes cast rather than as a winner-take-all system as exists currently.

Run ```electdf.py``` file first along with the ```states_dict.py``` to process the 1976-2020-president.csv file. 

### Process

First I set the index column to the ```'year'``` for ease of use. I then dropped several columns that were either superflous or unnecessary to the analysis. 
Second I deleted all the Write-In and blank votes. Since my methodology involves allocating the votes proportionally, it does not make sense to ever allocate any electoral votes to the write-in candidate. The write-in candidate entry represents several actual candidates, so any votes allocated to that entry would be inaccurate. (line 12-17 ```electdf.py```)
I then added a column to calculate the percent vote each candidate got. (line 19)

To add the state electoral votes, I merged a dataframe of the state electoral votes to the main dataframe. I used left ```merge``` because I wanted to keep all the data from the left dataframe (in this case ```electdf.py```) and merged on the columns ```'year'``` and ```'state'``` so that it kept those two columns together, which is crucial since the electoral votes for each state changes over the years. I also converted all the entries in the ```'state'``` to uppercase using the ```str.upper``` method to standardize the fields before the merge so there there was no issues. I had problems at first when I used ```capitalize``` because the multi-word states (like 'New Hampshire') didn't process correctly ('New Hampshire' became 'New hampshire'). (lines 21-22)

I then calculated the percent of electoral votes that each candidate received per state. When doing this I split off the whole number (```'vote_int'```) and the remainding fraction (```'vote_frac'```) for use later on. (line 24-26)

After that I needed to allocate any remaining electoral votes. I allocated these to the highest fractional votes, then the next highest, and so on, until no more remaining electoral votes were remaining. To do this, I grouped each state by year using ```groupby```. I then looped over each group (state by year) and found the candidates with the highest fractional remainders using ```nlargest``` on the ```vote_frac``` column. This allowed me to allocate the remaining electoral votes to the candidates with the highest fractional votes. I put these results into a dictionary for ease of access.

After this I exported the processed dataframe to a csv file for ease of viewing.

### Conclusions

Before starting the actual analysis and just looking at the data, my hypothesis would be that none of the elections would be overturned and that the gap of electoral votes would narrow in all races. I also hypothesized that third party candidates would capture some electoral votes. 

The advantages of this system are several. First, it allows third party candidates a chance to get some electoral votes. The proportional system makes voting for a third party much less of a "throwaway" vote. While there is still a long way to go before a third party is a legitimate threat to the two party system, the proportional vote makes it a much more likely scenario. 

Secondly, it gives a voice to the minority party in a state. If a state goes 51% towards one party, all those votes go to that party's candidate. Thus the minority party, in this case 49% of the votes, are essentially thrown away and meaningless. 





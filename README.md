# Proportional-Electoral-College-Vote
This project explores the results of a proportional electoral college vote for Presidential elections going back to 1976.

Electoral data obtained from the [Harvard Dataverse.](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX)

The purpose of this project is to determine the results of Presidential elections if the electoral college votes were given out as a proportion of votes cast rather than as a winner-take-all system as exists currently.

Run electdf.py file first along with the states_dict.py to process the 1976-2020-president.csv file. 

### Process

First I set the index column to the 'Year' for ease of use. I then dropped several columns that were either superflous or unnecessary to the analysis. 
Second I deleted all the Write-In and blank votes. Since my methodology involves allocating the votes proportionally, it does not make sense to ever allocate any electoral votes to the write-in candidate. The write-in candidate entry represents several actual candidates, so any votes allocated to that entry would be inaccurate.







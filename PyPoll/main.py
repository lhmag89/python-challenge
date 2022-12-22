#import dependencies
import os
import csv
#create relative filepath
csvdata = os.path.join("Resources","election_data.csv")
#read csv file
with open(csvdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #store header row
    header = next(csvreader)

    #convert columns to lists
    ballot = []
    county = []
    candidate = []

    #create lists for results
    uniqueCand = []
    candvotes = []
    candpercent = []
    
    #use for loop to append values to lists
    for row in csvreader:
        ballot.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])
    
    #calculate total number of votes cast
    totalVotes = len(ballot)
    
    #find unique values in list of candidates
    for x in candidate:
        if x in uniqueCand:
            continue
        else:
            uniqueCand.append(x)

    #get and store results for each candidate
    for x in uniqueCand:
        votes = candidate.count(x)
        candvotes.append(votes)
        percent = f'{round(votes/totalVotes*100, 3)}%'
        candpercent.append(percent)
    
    #find winner
    winTally = max(candvotes)
    winIndex = candvotes.index(winTally)
    winner = uniqueCand[1]
    
    #prepare report
    text = f"""
    Election Results
    _____________________________________________________

    Total Votes: {totalVotes}
    _____________________________________________________

    {uniqueCand[0]}: {candpercent[0]} ({candvotes[0]})
    {uniqueCand[1]}: {candpercent[1]} ({candvotes[1]})
    {uniqueCand[2]}: {candpercent[2]} ({candvotes[2]})
    _____________________________________________________

    Winner: {winner}
    _____________________________________________________
    """
    #export results
    print(text)
    file = open('analysis/election_results.txt','w')
    file.write(text)
    file.close()

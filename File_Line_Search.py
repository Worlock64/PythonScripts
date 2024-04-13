def logSearch(fileName):
    fh = open(fileName)
    #Line count will hole the number of lines we find in the text file, line value will hold the values of all the numbers added together.
    lineCount = 0.0
    lineValue = 0.0

    #Read the lines of the file and puts each line into the string lr.  Then strips each line, then looks for "X-DSPAM-Confidence:" When it finds one it then gets finds the 0 and takes the rest of the values of the string and averages their count
    for line in fh:
        lineStriped = line.rstrip()
        if lineStriped.startswith("X-DSPAM-Confidence"):
            valString = lineStriped.find("0")
            valFloat = float(lineStriped[valString:])
            lineCount +=1
        lineValue += valFloat
    
        
    #Check to make sure not dividing my zero
    if lineCount or lineValue == 0:
        print("Your values are empty")
    print("Average spam confidence:", lineValue/lineCount)

def findEmail(filename):
    fh = open(filename)
    senders = {}
    count = 0
    most = ""
    for line in fh:
        if line.startswith("From "):
            lnLst = line.split()
            sender = (lnLst[1])
            if sender in senders:
                senders[sender] = senders.get(sender, 0 ) + 1
            else:
                senders[sender] = 1

    for email in senders:
        if senders.get(email) > count:
            count = senders.get(email)
            most = email
    
    print(most, count)

def findDate(filename):
    fh = open(filename)
    dates = {}
    for line in fh:
        if line.startswith("From "):
            lnLst = line.split()
            time = (lnLst[5])
            hour = time[0:2]
            if hour in dates:
                dates[hour] = dates.get(hour, 0 ) + 1
            else:
                dates[hour] = 1
    
    sortedDates = dict(sorted(dates.items()))
    for x in sortedDates:
        hourKey = x
        hourCnt = sortedDates[x]
        print(hourKey, hourCnt)

#fileName = input("Enter File Name: ")

findDate('mbox-short.txt')
import math

def detect(data, parameters):
    splitData = {}
    varStart = []
    varEnd = []
    #if it is needed to find start and end positions find value is True
    if parameters['find'] == True:
        
        #import required axis for finding start location
        for value in range(0,len(data)):
            varStart.append(math.degrees(data[value].get(parameters['axisStart'])))
            
        for value in range(0,len(data)):
            #find start location based on higher or lower then threshold
            if parameters['luStart'] == '>':
                if varStart[value] > parameters['startThreshold']:
                    startPos = value
                    break
            elif parameters['luStart'] == '<':
                if varStart[value] < parameters['startThreshold']:
                    startPos = value
                    break
            
            #if no start location is found halfway the dataset use position 0 start location
            if value > 0.5 * len(data):
                startPos = 0
                break
            
        #import required axis for finding end location
        for value in range(0,len(data)):
            varEnd.append(math.degrees(data[value].get(parameters['axisEnd'])))
            
        for value in range(len(data)-1,0,-1):
            #find end location based on higher or lower then threshold
            if parameters['luEnd'] == '>':
                if varEnd[value] > parameters['endThreshold']:
                    endPos = value
                    break
            elif parameters['luEnd'] == '<':
                if varEnd[value] < parameters['endThreshold']:
                    endPos = value
                    break
            
            #if no end location is found halfway the dataset use last position as end location
            if value < 0.5 * len(data):
                endPos = len(data)
                break
    
    #if it is not needed to find start and end positions find value is False and use first and last value to split dataset
    elif parameters['find'] == False:
        startPos = 0
        endPos = len(data)
    
    #set markers to split file into multiple datasets
    markers = [0,0,0,0,0,0,0,0,0,0]
    for marker in range(0,len(markers)):
        markers[marker] =  int((marker/10) * (endPos - startPos))
    
    #split dataset
    for marker in range(0,len(markers)):
        splitData[f"E{marker}"]= []
        if marker == 9:
            for value in range(startPos + markers[marker], endPos):
                splitData[f"E{marker}"].append(data[value]) 
        else:
            for value in range(startPos + markers[marker], startPos + markers[marker + 1]):
                    splitData[f"E{marker}"].append(data[value]) 
    return splitData
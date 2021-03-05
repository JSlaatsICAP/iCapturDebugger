import math
import compSensorLim
from scipy import signal
    
def detect(data, parameters):
    detVar = []
    invertedDetVar = []
    time = []
    splitData = {}

    #extract needed axis
    for value in range(0,len(data)):
        detVar.append(math.degrees(data[value].get(parameters['axisDet'])))
        time.append(data[value].get('time'))
        
    #check if used axis reaches sensor limit and compensate if needed
    detVar = compSensorLim.compe(detVar)
                
    #calculate differentiated values of the required axis
    diffDetVar = []
    for value in range(0,len(detVar) - 1):
        diffDetVar.append(detVar[value + 1] - detVar[value])
    
    if parameters['peakTypeDet'] == 'inverted':
        #calculate inverted variable for peak det            
        for value in detVar:
            invertedDetVar.append(value*-1)
        #invert signal to find negative peaks when required
        peaks = signal.find_peaks(invertedDetVar ,prominence = parameters['prominence'])
            
    if parameters['peakTypeDet'] == 'normal':
        #invert signal to find negative peaks when required
        peaks = signal.find_peaks(detVar ,prominence = parameters['prominence'])
        
    for peak in range(0,len(peaks[0])):
        startPos = int()
        endPos = int()
        counter = 0
        
        # if peakNrStart = 0 use the detected peak as start position
        if parameters['peakNrStart'] == 0:
            startPos = peaks[0][peak]
        if parameters['peakNrStart'] != 0:
            # take found negative peak compute to start until positive peak is found and conditions are met
            for value in range(peaks[0][peak],1,-1):
                if parameters['peakTypeStart'] == 'positive':
                    if diffDetVar[value - 1] > 0 and diffDetVar[value] < 0:
                        if abs(detVar[value] - detVar[peaks[0][peak]]) > parameters['minAxisDiffStart'] and abs(peaks[0][peak] - value) > parameters['minTimeDiffStart']:
                            counter = counter + 1
                            #break when required peak is found
                            if counter == parameters['peakNrStart']:
                                startPos = value
                                counter = 0
                                break
                
                #take found peak and compute until negative peak is found and conditions are met
                if parameters['peakTypeStart'] == 'negative':
                    if diffDetVar[value - 1] < 0 and diffDetVar[value] > 0:
                        if abs(detVar[value] - detVar[peaks[0][peak]]) > parameters['minAxisDiffStart'] and abs(peaks[0][peak] - value) > parameters['minTimeDiffStart']:
                            counter = counter + 1
                            #break when required peak is found
                            if counter == parameters['peakNrStart']:
                                startPos = value
                                counter = 0
                                break
        
        # if peakNrStart = 0 use the detected peak as start position
        if parameters['peakNrEnd'] == 0:
            endPos = peaks[0][peak]
        if parameters['peakNrEnd'] != 0:
            for value in range(peaks[0][peak],len(detVar)-2):
                #take found peak and compute until positive peak is found and conditions are met
                if parameters['peakTypeEnd'] == 'positive':
                    if diffDetVar[value] > 0 and diffDetVar[value + 1] < 0:
                        if abs(detVar[value] - detVar[peaks[0][peak]]) > parameters['minAxisDiffEnd'] and abs(peaks[0][peak] - value) > parameters['minTimeDiffEnd']:
                            counter = counter + 1
                            #break when required peak is found
                            if counter == parameters['peakNrEnd']:
                                endPos = value
                                counter = 0
                                break
                        
                #take found peak and compute until negative peak is found and conditions are met
                if parameters['peakTypeEnd'] == 'negative':
                    if diffDetVar[value] < 0 and diffDetVar[value + 1] > 0:
                        if abs(detVar[value] - detVar[peaks[0][peak]]) > parameters['minAxisDiffEnd'] and abs(peaks[0][peak] - value) > parameters['minTimeDiffEnd']:
                            counter = counter + 1
                            #break when required peak is found
                            if counter == parameters['peakNrEnd']:
                                endPos = value
                                counter = 0
                                break

        #if start or end position is not found return empty list
        if bool(startPos) == False or bool(endPos) == False :
            splitData[f'E{peak}'] = []   
            
        #if both start and end positions are met append data as split squat  
        else:
            splitData[f'E{peak}'] = []    
            for value in range(startPos,endPos):
                    splitData[f'E{peak}'].append(data[value]) 
    return splitData
    
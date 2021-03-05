from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'roll',
                  'peakTypeDet':'inverted',
                  'prominence':10,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 5,
                  'minTimeDiffStart' : 40,
                  'peakTypeEnd' : 'positive',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 5,
                  'minTimeDiffEnd' : 40,}

    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch'],
                  'minDiff' : 20,
                  'threshold' : 0.2,
                  'minLen' : 0,
                  'maxLen' : 1000}
    
    result = validate.init(splitData, parameters)
    return result
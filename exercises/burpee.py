from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'roll',
                  'peakTypeDet':'inverted',
                  'prominence':70,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 20,
                  'minTimeDiffStart' : 40,
                  'peakTypeEnd' : 'positive',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 20,
                  'minTimeDiffEnd' : 40,}

    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch'],
                  'minDiff' : 4,
                  'threshold' : 0.1,
                  'minLen' : 10,
                  'maxLen' : 500}
    
    result = validate.init(splitData, parameters)
    return result

from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'roll',
                  'peakTypeDet':'normal',
                  'prominence':5,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 0,
                  'minAxisDiffStart' : 8,
                  'minTimeDiffStart' : 5,
                  'peakTypeEnd' : 'positive',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 8,
                  'minTimeDiffEnd' : 5,}

    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch'],
                  'minDiff' : 5,
                  'threshold' : 0.1,
                  'minLen' : 10,
                  'maxLen' : 500}
    
    result = validate.init(splitData, parameters)
    return result

from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'pitch',
                  'peakTypeDet':'normal',
                  'prominence':60,
                  'peakTypeStart' : 'negative',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 20,
                  'minTimeDiffStart' : 0,
                  'peakTypeEnd' : 'negative',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 20,
                  'minTimeDiffEnd' : 0,}

    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['roll'],
                  'minDiff' : 5,
                  'threshold' : 0.1,
                  'minLen' : 10,
                  'maxLen' : 500}
    
    result = validate.init(splitData, parameters)
    return result

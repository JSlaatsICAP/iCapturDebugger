from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'roll',
                  'peakTypeDet':'normal',
                  'prominence':10,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 0,
                  'minTimeDiffStart' : 0,
                  'peakTypeEnd' : 'positive',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 0,
                  'minTimeDiffEnd' : 0,}

    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch'],
                  'minDiff' : 20,
                  'threshold' : 0.2,
                  'minLen' : 10,
                  'maxLen' : 500}
    
    result = validate.init(splitData, parameters)
    return result
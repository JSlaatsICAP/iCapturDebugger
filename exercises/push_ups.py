from .functions import detectRaw
from .functions import validate

def detect(data):
    
    splitData = {}
    parameters = {'axisDet':'roll',
                  'peakTypeDet':'inverted',
                  'prominence':5,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 5,
                  'minTimeDiffStart' : 10,
                  'peakTypeEnd' : 'positive',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 5,
                  'minTimeDiffEnd' : 10,}

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
  
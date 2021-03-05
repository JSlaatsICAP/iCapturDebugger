from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'pitch',
                  'peakTypeDet':'inverted',
                  'prominence':10,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 10,
                  'minTimeDiffStart' : 20,
                  'peakTypeEnd' : 'positive',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 10,
                  'minTimeDiffEnd' : 20,}
    
    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['roll'],
                  'minDiff' : 5,
                  'threshold' : 0.2,
                  'minLen' : 200,
                  'maxLen' : 1000}
    
    result = validate.init(splitData, parameters)
    return result

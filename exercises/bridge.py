from .functions import detectRaw
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'roll',
                  'peakTypeDet':'normal',
                  'prominence':8,
                  'peakTypeStart' : 'negative',
                  'peakNrStart': 1,
                  'minAxisDiffStart' : 20,
                  'minTimeDiffStart' : 5,
                  'peakTypeEnd' : 'negative',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 20,
                  'minTimeDiffEnd' : 5,}

    splitData = detectRaw.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch'],
                  'minDiff' : 5,
                  'threshold' : 0.1,
                  'minLen' : 10,
                  'maxLen' : 200}
    
    result = validate.init(splitData, parameters)
    return result
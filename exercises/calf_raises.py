from .functions import detectVelo
from .functions import validate

def detect(data):
    splitData = {}
    parameters = {'axisDet':'uAccX',
                  'peakTypeDet':'normal',
                  'prominence':0.5,
                  'peakLoopInterval':1,
                  'peakTypeStart' : 'positive',
                  'peakNrStart': 0,
                  'minAxisDiffStart' : 0,
                  'minTimeDiffStart' : 0,
                  'peakTypeEnd' : 'negative',
                  'peakNrEnd': 1,
                  'minAxisDiffEnd' : 0.02,
                  'minTimeDiffEnd' : 20,}
    
    splitData = detectVelo.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch'],
                  'minDiff' : 5,
                  'threshold' : 0.2,
                  'minLen' : 10,
                  'maxLen' : 500}
    
    result = validate.init(splitData, parameters)
    return result
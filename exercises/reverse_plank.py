from .functions import detectStab
from .functions import validate

def detect(data):
    
    splitData = {}
    parameters = {'find':True,
                  'axisStart':'roll',
                  'startThreshold':-120,
                  'luStart' : '<' ,
                  'axisEnd':'roll',
                  'endThreshold':-120,
                  'luEnd' : '>'}
 
    splitData = detectStab.detect(data, parameters)
    return splitData

def analyse(splitData):  
    parameters = {'axis':['pitch','roll','yaw'],
                  'minDiff' : 10,
                  'threshold' : 0.2,
                  'minLen' : 10,
                  'maxLen' : 500}
    
    result = validate.init(splitData, parameters)
    return result
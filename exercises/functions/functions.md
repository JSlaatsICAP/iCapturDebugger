algoritm service uses 3 dynamic functions for detecting and 1 for validating excercises

# detection
## detectRaw
detectRaw is detection based on peaks it contains the following variables and possible inputs.
It returns a list containing the data of every detected excercise

'axisDet': 'pitch' 'roll' 'yaw'\
axisDet contains the axis that is used for detection

'peakTypeDet': 'inverted' 'normal'\
peakTypeDet defines if negative or positive peaks are being used for primary detection, this can be done over an inverted signal or a normal signal (positive/negative peaks)

'prominence': 'numerical input (0-∞)'\
prominence defines the minimum prominence a peak can have more, link for more information about [peak prominence] (https://www.mathworks.com/help/signal/ug/prominence.html")

'peakTypeStart' : 'positive' 'negative'\
defines if the start of the excercise contains a positive or negative peak

'peakNrStart': 'numerical (no decimals, 0-∞)'\
what peak has to be used for start position counting back from the primary detection peak

'minAxisDiffStart' : 'numerical input (0-∞)'\
minimum absolute difference in degrees the start peak can have

'minTimeDiffStart' : 'numerical input (0-∞)'\
minimum difference in datapoints the start peak can have compared to the primary peak

'peakTypeEnd' : 'positive' 'negative'\
defines if the end of the excercise contains a positive or negative peak

'peakNrEnd': 'numerical (no decimals, 0-∞)'\
what peak has to be used for end position counting upwards from the primary detection peak

'minAxisDiffEnd' : 'numerical input (0-∞)'\
minimum absolute difference in degrees the end peak can have

'minTimeDiffEnd' : 'numerical input (0-∞)'\
minimum difference in datapoints the end peak can have compared to the primary peak

## detectVelo
DetectVelo used the same variables as detectRaw except for axisDet this is caused by the detection being based on velocity
It also returns a list containing the data of every detected excercise

'axisDet': 'uAccX' 'uAccY' 'uAccZ'\
axisDet contains the axis that is used for detection

## detectStab
detectStab is a function designed for undetectable excercises and therefore detect splits up the excercises so stability can be detected over smaller parts 
These are excercises like the plank.
It returns a list of containing 10 parts of the excercise either with detected start and/or end positions or not

'find': True, false\
defines if start and end position have to be found first

'axisStart':'roll', 'pitch', 'yaw'\
defines the variable that is needed for finding the start position

'startThreshold':numerical (0-∞)\
threshold in degrees for finding the start position

'luStart' : '>', '<' \
defines if the start position has to be smaller or greater then the threshold

'axisEnd':'roll', 'pitch', 'yaw'\
defines the variable that is needed for finding the start position

'endThreshold':numerical (0-∞)\
threshold in degrees for finding the end position

'luEnd' :  '>', '<'\
defines if the end position has to be smaller or greater then the threshold

#validation
## validate
validate is used for validation of the excercises and returns a list of 10 values each consisting of a 0 or 1

'axis':'pitch','roll','yaw'\
axis defines the variable or variables used for validation, the input can be either a singular axis or multiple

'minDiff' : numerical (0-∞)\
the minimum absolute difference the variables can have compared to the average before being defines in error

'threshold' : numerical (0-1)\
amount of errors allowed within an excercise this is being entered as an percentage modifier f.e. the input 0.1 is 10% of the excercise in error

'minLen' : numerical (0-∞)\
the minimum length an excercise can have

'maxLen' : numerical (0-∞)\
the maximum length an excercise can have

# other functions

## compSensorLim
compSensorLim detects if the maximum or minimum value of the orientation has been reached.
If so it compensates these values to what it should be in absolute difference compared to the other values

the input is a list of the orientation data
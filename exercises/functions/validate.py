import math
import compSensorLim

def init(splitData, parameters):
    val = []
    result = {}

    for excercise in range(0,len(splitData)):

        #if dataset is not empty continue to validate
        if not splitData[f'E{excercise}'] == []:

            #compare exercise length compared to avg length of detected exercises
            if len(splitData[f'E{excercise}']) < parameters['minLen']:
                result[f'E{excercise}'] = 0
                continue

            if len(splitData[f'E{excercise}']) > parameters['maxLen']:
                result[f'E{excercise}'] = 0
                continue 
            
            counter = 0
            dat = splitData[f"E{excercise}"]
            pitch = []
            roll =[]
            yaw = []    
            
            #import needed axis
            for value in range(0,len(dat)):
                pitch.append(math.degrees(dat[value].get('pitch')))
                roll.append(math.degrees(dat[value].get('roll')))
                yaw.append(math.degrees(dat[value].get('yaw')))

            pitch = compSensorLim.compe(pitch)
            roll = compSensorLim.compe(roll)
            yaw = compSensorLim.compe(yaw)

            #calculate averages
            resP = sum(pitch) / len(pitch)
            resR = sum(roll) / len(roll)
            resY = sum(yaw) / len(yaw)
            
            #if any value differs more then 10 degrees from the average count it as error
            if 'pitch' in parameters['axis']:
                for value in range(0,len(pitch)):
                    if abs(abs(pitch[value])-abs(resP)) > parameters['minDiff']:
                        counter = counter + 1
                        
            if 'roll' in parameters['axis']:
                for value in range(0,len(pitch)):
                    if abs(abs(roll[value])-abs(resR)) > parameters['minDiff']:
                        counter = counter + 1

            if 'yaw' in parameters['axis']:
                for value in range(0,len(pitch)):
                    if abs(abs(yaw[value])-abs(resY)) > parameters['minDiff']:
                        counter = counter + 1                        
            
            #if more then X amount is in error return 0
            if counter > parameters['threshold'] * (len(pitch)):
                val = 0
            else:
                val = 1
            
            result[f"E{excercise}"]= val

        #when list empty return 0
        if splitData[f'E{excercise}'] == []:
            result[f'E{excercise}'] = 0

    return result
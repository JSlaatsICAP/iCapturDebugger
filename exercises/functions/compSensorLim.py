def compe(detVar):
    #check if used axis reaches sensor limit
    ul = 0
    ll = 0
    for value in detVar:
        if value > 176:
            ul = 1
        if value < -176:
            ll = 1

    #if either the value 170 and -170 has been measured assume sensor limit has been reached and compensate for it      
    if ul == 1 or ll == 1:
        for value in range(0,len(detVar)):
            if detVar[value] < 0:
                offset = []
                offset = - 180 - detVar[value]
                detVar[value] = 180 - offset
    return detVar
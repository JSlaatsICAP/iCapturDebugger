import json
import matplotlib.pyplot as plt 
import math
import compSensorLim

filename = input('enter filename\n')

with open(filename) as input_file:
        data = json.load(input_file)

plttr = input('do you want to plot a single variable or multiple? (single or multiple)\n')

if plttr == 'single':
    
    #enter Y values (X values will always be time)
    variable = input ('enter what variable to plot  (accX-Y-Z, gyroX-Y-Z, uAccX-Y-Z, pitch - roll - yaw, case sensitive)\n')
    
    x = []
    y = []
    
    for value in range(0,len(data)):
        y.append(math.degrees(data[value].get(variable)))
        x.append(data[value].get('time'))
        
    # plotting the points  
    plt.plot(x, y, color='green', linewidth = 1, 
             marker='', markerfacecolor='blue', markersize=12) 
      
    # setting x and y axis range 
    plt.ylim(-180,180) 
    plt.xlim(1,x[len(x) - 1]) 
      
    # naming the x axis 
    plt.xlabel('time (s)') 
    # naming the y axis 
    plt.ylabel(variable) 
    # function to show the plot 
    plt.show() 
    
if plttr == 'multiple':
    
    #enter Y values (X values will always be time)
    variable = input ('enter what variable to plot  (acc, gyro, uAcc, orientation)\n')
    
    # function to import values
    def create_plot(variable): 
        y1 = []
        y2 = []
        y3 = []
        x = []
        
        for value in range(0,len(data)):
        
            # setting the y-axis values 
            if variable == 'acc': 
                y1.append(math.degrees(data[value].get('accX')))
                y2.append(math.degrees(data[value].get('accY')))
                y3.append(math.degrees(data[value].get('accZ')))
            elif variable == 'gyro': 
                y1.append(math.degrees(data[value].get('gyroX')))
                y2.append(math.degrees(data[value].get('gyroY')))
                y3.append(math.degrees(data[value].get('gyroZ')))
            elif variable == 'uAcc': 
                y1.append(math.degrees(data[value].get('uAccX')))
                y2.append(math.degrees(data[value].get('uAccY')))
                y3.append(math.degrees(data[value].get('uAccZ')))
            elif variable == 'orientation': 
                y1.append(math.degrees(data[value].get('pitch')))
                y2.append(math.degrees(data[value].get('roll')))
                y3.append(math.degrees(data[value].get('yaw')))
                y1 = compSensorLim.compe(y1)
                y2 = compSensorLim.compe(y2)
                y3 = compSensorLim.compe(y3)
                
            x.append(data[value].get('time'))
                  
        return(x, y1, y2, y3) 
    
    
    # create a figure 
    fig = plt.figure() 
      
    # define subplots and their positions in figure 
    plt1 = fig.add_subplot(311) 
    plt2 = fig.add_subplot(312) 
    plt3 = fig.add_subplot(313) 
    
    # plotting points on each subplot 
    if variable == 'acc': 
        x, y1, y2, y3 = create_plot('acc') 
        plt1.plot(x, y1, color ='r') 
        plt1.set_title('accX')
        plt2.plot(x, y2, color ='r') 
        plt2.set_title('accY') 
        plt3.plot(x, y3, color ='r') 
        plt3.set_title('accZ') 
    elif variable == 'gyro': 
        x, y1, y2, y3 = create_plot('gyro') 
        plt1.plot(x, y1, color ='r') 
        plt1.set_title('gyroX')
        plt2.plot(x, y2, color ='r') 
        plt2.set_title('gyroY') 
        plt3.plot(x, y3, color ='r') 
        plt3.set_title('gyroZ') 
    elif variable == 'uAcc': 
        x, y1, y2, y3 = create_plot('uAcc') 
        plt1.plot(x, y1, color ='r') 
        plt1.set_title('uAccX')
        plt2.plot(x, y2, color ='r') 
        plt2.set_title('uAccY') 
        plt3.plot(x, y3, color ='r') 
        plt3.set_title('uAccZ') 
    elif variable == 'orientation': 
        x, y1, y2, y3 = create_plot('orientation') 
        plt1.plot(x, y1, color ='r') 
        plt1.set_title('pitch')
        plt2.plot(x, y2, color ='r') 
        plt2.set_title('roll') 
        plt3.plot(x, y3, color ='r') 
        plt3.set_title('yaw') 

    # adjusting space between subplots 
    fig.subplots_adjust(hspace=1,wspace=1) 
      
    # function to show the plot 
    plt.show()

'''Project comment goes here'''

import pylab as py
import csv

MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

def open_file():
    "Insert DocString here."
    pass # insert your code here    

def read_file(fp):
    "Insert DocString here."
    pass # insert your code here    
        
def get_damage_data(data, year):
    "Insert DocString here."
    pass # insert your code here    

def get_quake_data(data, year):
    "Insert DocString here."
    pass # insert your code here    

def summary_statistics(data, year_start, year_end):
    "Insert DocString here."
    pass # insert your code here    

def display_damage_data(L, year):
    "Insert DocString here."
    pass # insert your code here        
        
def display_quake_data(L, year):
    "Insert DocString here."
    pass # insert your code here    

def display_summary(quakes, costs, casualties):
    "Insert DocString here."
    pass # insert your code here    

def plot_intensity_map(year, quake_data):
    '''
        This function plots the map of the earthquake locations for the
        selected year. This function is provided in the skeleton code.
        
        Parameters:
            year (string): The year key for the data to plot
            size (int): Number of earthquakes that occured in the selected year
            
            coordinates (list): List of (latitude,longitude) coordinates for
                                the trajectory of each earthquake that occured
                                in the selected year.
                                
        Returns: None
    '''
    
    
    # The the RGB list of the background image.
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude,max_longitude))
    py.ylim((-max_latitude,max_latitude))
    
    
    # build the x,y coordinates map
    lst = list(zip(*quake_data))
    lat,lon,mag = lst[3],lst[4],lst[1] 
    
    area = ([(1.0 * p) ** 2 for p in mag ])
    
    
    # plot the scatter plot
    scatter = py.scatter(lon,lat,s=area, c=mag, cmap='seismic')    
    py.colorbar(scatter)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Earthquake Magnitude points for {}".format(year))
    py.show() # show the full map

def plot_bar(L, title, x_label, y_label):
    '''
        This function receives a list of x,y values.
        
        Parameters
            L (list): 
            title (str):
            x_label (str):
            y_label (str):
                
        Returns
            None
    '''
    
    #count the earthquakes per month
    total = [0]*12
    for i in L:
        total[i[0]-1] += 1
    
    
    py.title(title)
    py.xlabel(x_label)
    py.ylabel(y_label)
    py.xticks(range(12),MONTHS)
    py.bar(range(12), total)
    py.show()

def plot_line(L, title, x_label, y_label):
    '''
        This function receives a list of x,y values.
        
        Parameters
            L (list): 
            title (str):
            x_label (str):
            y_label (str):
        
        Returns
            None
    '''
    res = list(zip(*L))
    
    py.title(title)
    py.xlabel(x_label)
    py.ylabel(y_label)
    py.xticks(range(len(res[0])),[str(r) for r in res[0]], rotation=90)
    py.plot(range(len(res[0])),res[1], marker="o")
    
    py.show()

def plot_pie(L, title):
    '''
        This function receives a list of x,y values.
        
        Parameters
            L (list): 
            title (str):
                
        Returns
            None
    '''
    #            L[2].append((y,(deaths,missing,injured)))
    deaths = sum([t[0] for y,t in L])
    missing = sum([t[1] for y,t in L])
    injured = sum([t[2] for y,t in L])
    total = deaths + missing + injured
    d = deaths/total
    m = missing/total
    i = injured/total
    L = [["deaths",d],["missing",m],["injuries",i]]

    res = list(zip(*L))
    
    py.title(title)
    py.pie(res[1],labels=res[0],autopct='%.1f%%') 
    py.show()

    
def main():    
    '''
        This program will show damages caused by an earthquakes in a year.
        Also, it will plot the intensity of all earthquakes observed in a year.
    
    '''
    
    MENU = '''\nEarthquake data software
        
        1) Visualize damage data for a single year
        2) Visualize earthquakes magnitudes for a single year
        3) Visualize number of earthquake and their damages within a range of years
        4) Exit the program
    
        Enter a command: '''
        
    pass # insert your code here    
   
    print("\nThank you for using this program!")


if __name__ == "__main__":
    main()

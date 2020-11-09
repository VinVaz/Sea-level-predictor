import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    # Create an extended line to predict the sea level of year 2050
    year_extended_1 = np.arange(1880, 2050, 1)
    
    y1 = ( intercept + slope * year_extended_1 )[:, np.newaxis]
    x1 = year_extended_1[:, np.newaxis]
    ax.plot(x1, y1, color='#10ff15')
    
    # Create second line of best fit
    df = df[df['Year'] >= 2000]
    year_extended_2 = np.arange(2000, 2050, 1)

    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    y2 = ( intercept + slope * year_extended_2 )[:, np.newaxis]
    x2 = year_extended_2[:, np.newaxis]
    ax.plot(x2, y2, color='#ff25a6')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    
    return plt.gca()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv("epa-sea-level.csv", sep=",")

    # Create scatter plot
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"],s = 2)

    # Create first line of best fit
    a=linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    m=a[0]
    b=a[1]
    x=df["Year"]
    years=[]
    cs=[]
    for i in range(1880,2051):
     years.append(i)
     cs.append((m*i+b))
    plt.plot(years, cs, c = 'r')

    # Create second line of best fit
    a2=linregress(df[(df["Year"]>1999)]["Year"], df[(df["Year"]>1999)]["CSIRO Adjusted Sea Level"])
    m2=a[0]
    b2=a[1]
    years2=[]
    cs2=[]
    for i in range(2000,2051):
     years2.append(i)
     cs2.append((m2*i+b2)) 

    # Add labels and title
    plt.figure(figsize=(14,9))
    plt.scatter(x,df["CSIRO Adjusted Sea Level"], s = 5)
    plt.plot(years, cs, c = 'r')
    plt.plot(years2, cs2, '--',c = 'g')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
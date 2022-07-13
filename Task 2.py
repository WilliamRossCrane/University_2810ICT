#-- TASK 2 --#

# Install into Console: pip install mysql-connector-python
# Install into Console: conda install matplotlib

# Imported to Connect to SQL Database
import sqlite3
# Imported to Plot the Graph
import matplotlib.pyplot as plt
# Imported for Dates
import matplotlib.dates as mdates
# Imported for Styling
from matplotlib import style
# Replicates Styling from FiveThirtyEight.com
style.use('fivethirtyeight')
# Connects to Database name climate.db
conn = sqlite3.connect(r"climate.db")
# Allows Querys to be Fetched from the Database
c = conn.cursor()
# Graph Parameter Function
def graph_data():
    # Specifys Areas of the Graph to Fetch
    c.execute('SELECT Year, CO2, Temperature FROM ClimateData')
    # Fetches Data from Requested Variable 
    data = c.fetchall()
    # Arrays for the Three Columns 
    dates = []
    co2 = []
    temp = []
    # Loops through fetched data and adds it to an Array, based on row
    for row in data:
        dates.append(row[0])
        co2.append(row[1])
        temp.append(row[2])
 #Graph Styling
    # Creates New Figure
    fig = plt.figure()
    # Grid Parametres encoded as a Single Integer 
    ax1 = fig.add_subplot(111)
    # Title of the Graph 
    ax1.set_title("Table: Climate Data")
    # Date Label of the X Axis
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
    # Name Label of the Y Axis
    ax1.set_ylabel("CO2")
    # Sets Date, Colour and Label
    ax1.plot_date(dates, co2, '-', label="CO2", color='r')
    # Allows multiple plots in a single figure 
    ax2 = ax1.twinx()
    # Label for Plot Two
    ax2.set_ylabel("Temp")
    # Sets Date, Colour and Label
    ax2.plot_date(dates, temp, '-', label="Temperature", color='g')
    # Rotates Dates, So no Overlap Occurs
    fig.autofmt_xdate(rotation=60)
    # Automatically Adjusts the Plot so that the Subplot fits into the Graph
    fig.tight_layout()
    # Configures the Grid
    ax1.grid(True)
    # Positions the Plots inside the Frame
    ax1.legend(loc='best', framealpha=0.5)
    ax2.legend(loc='best', framealpha=0.5)
    # Saves the Graph as a PNG
    plt.savefig("figure.png")
# Displays Graph
graph_data()
# Closes Connection to the Database
c.close
conn.close()

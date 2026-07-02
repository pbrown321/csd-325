import csv, sys
from datetime import datetime

from matplotlib import pyplot as plt

#ptb edit adding note explaining our program
print('''Welcome to the Sitka Weather Graphing Tool.  Our database contains the high and
      low temperatures for Sitka Alaska for 2018.  You may graph either the high or low
      temperatures to visualize the deviation over time.
      ''')

#PTB Adding ability for user to input whether they want to graph high, low temp or exit
#utilizing bet loop from CHOHAN.PY by Al Sweigert 
#at https://nostarch.com/big-book-small-python-projects

# Input high low or exit:
while True:
    print('Would you like to graph the HIGH or LOW temperatures? (or EXIT)')
    temp = input('<: ').upper()  
    if temp == 'EXIT':
        print('Thank you, have a nice day!')
        sys.exit()
    elif temp != 'HIGH' and temp != 'LOW':
        print('Please enter HIGH or LOW.')
    else:
        # This is a valid entry.
        print(f'Graphing the {temp} temperatures for Sitka.')
            


        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and high temperatures from this file.
            dates, highs, lows = [], [], [] #ptb adding list to store low figures
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)
                low = int(row[6]) #PTB edit adding low section and adding to low list
                lows.append(low)

        # Plot the user input temperatures.
        #plt.style.use('seaborn')
        
        if temp == 'HIGH':  #ptb edit adding if loop for high or low
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

            # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
        else:
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')

            # Format plot.
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

#ptb edit adding another loop which allows the user to continue graphing or exit
#if Y is entered the loop will exit and go back to the beginning 
#if N is entered we exit and print exit message
        print('Would you like to create another graph? Enter Y or N.')
        while True:
            response = input('<: ').upper()
            if response == 'N':
                print('Thank you, have a nice day!')
                sys.exit()
            elif response == 'Y':
                break  
            else:
                print('Please enter Y or N.')
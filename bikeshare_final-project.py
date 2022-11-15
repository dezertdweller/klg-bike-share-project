from importlib.resources import path
import time
import pandas as pd
import numpy as np
import sys
from tabulate import tabulate


# Note: you will need to replace the path with where you save the .csv data files for the three cities.
CITY_DATA = { 'chicago': '~/data-files/bikeshare/chicago.csv',
              'new york city': '~/data-files/bikeshare/new_york_city.csv',
              'washington': '~/data-files/bikeshare/washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all months']
WEEK_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
yes_list = ['Yes', 'yes', 'y']
no_list = ['No', 'no', 'n']

def continue_prompt():
    """
    prompt user if they would like to continue through various statistical analysis processes
    """

    print()
    print('We are now going to display some more statistics.')

    while True:  
        response = input ('Would you like to continue? Yes or No: ')
        if response.lower() in yes_list:
            print()
            print('Okay, we will move on to the next section!')
            break
        elif response.lower() in no_list:
            print()
            print('Okay, you will now be exiting the program. Goodbye!')
            sys.exit()
            break
        else:
            print()
            print('That was not a valid entry. Please enter yes or no.')
            continue 


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US Bike Share data!')
    print()
    print('We will be looking at city-level data for you specified time period.')
    print()
    print('You\'ll be able to view raw data, time stats, station stats, trip duration, and user information.')
    print()
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input('Which city you would like to view data for: Chicago, New York City, or Washington? ')

            if city.lower().strip() in CITY_DATA:
                print()
                city = city.lower().strip()
                print(('Great! Let\'s look at the data for {}.').format(city.title()))
                break
            elif city not in CITY_DATA:
                print()
                print('{} is not a valid entry. Please enter either Chicago, New York City, or Washington.'.format(city.title()))
                print()
                continue
        
    # get user input for month (all, january, february, ... , june)
    print()
    print("You can filter the data by month. You can choose from the following: January, February, March, April, May, June, or all months.")
   
    while True: 
        month = input('Which month would you like to filter the data by? ')
        if month.lower().strip() in MONTH_DATA:
            month = month.lower().strip()
            break
        elif month.lower().strip() == 'all':
            month = 'all months' 
            break
        else:
            print()
            print('That is not a valid entry. Please select one of the month options available.')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print()
    print('You can filter the data by day. You can choose from the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all.')
    while True: 
        day = input('Which day would you like to filter the data by? ')
        if day.lower().strip() in WEEK_DATA:
            day = day.lower().strip()
            
            print()
            print('Thank you for selecting your filters. We are now going to display some relevant data summaries.')
            break
        else:
            print()
            print('That is not a valid entry. Please select one of the day options available.')
            continue
    
    # asks user if they want to continue to the statistical analysis.
    while True:
        response = input ('Would you like to continue? Yes or No: ')
        if response.lower() in yes_list:
            print()
            print('Okay, we will move on to the next section!')
            break
        elif response.lower() in no_list:
            print()
            print('You have chosen to exit the program. Goodbye!')
            sys.exit()
        else:
            print()
            print('That is not a valid entry. Please enter yes or no. ')
            continue

    print('\n')
    print()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # coverting Start Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month 
    if month != 'all months':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def raw_data(df):
    """
    Prompts user to determine if they would like to see some raw data for the selected city
    """
    see_data = True 

    #prompt user if they would like to see raw data
    while (see_data):
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        keep_asking = True
        
        if view_data in yes_list:    
            print(tabulate(df.iloc[start_loc:start_loc + 5], headers ='keys'))

            #asks user if they would like to continue seeing 5 rows of data at a time
            while (keep_asking):
                start_loc += 5
                view_display = input("Do you wish to continue viewing 5 additional rows of data?: ").lower()
                if view_display in yes_list:
                    print(tabulate(df.iloc[start_loc:start_loc + 5], headers ='keys'))
                    continue
                elif view_display in no_list:
                    keep_asking = False
                    print()
                    print('Okay, you will now move on to the next section!')
                    see_data = False
                    break
                else:
                    print()
                    print('That was not a valid entry. Please enter yes or no. ')
                    continue
        
        elif view_data in no_list:
            print()
            print('Okay, we will move on to the next section!')
            break
        
        else:
           print()
           print('That is not a valid entry. Please enter yes or no. ')
           continue 

def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.
    """
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month != 'all months':
        print()
        print('You filtered the data by {}, so we can\'t show most common month.'.format(month.title()))
    else:   
        common_month = df['month'].mode()[0]
        print()
        print('The most common month for bikeshare use was: ', common_month)

        
    # display the most common day of week
    if day != 'all':
        print()
        print('You filtered by {}, so we can\'t show you the most common day.'.format(day.title()))
    else:
        common_day = df['day_of_week'].mode()[0]
        print()
        print('The most common day of the week for bikeshare use during {} was: '.format(month.title()), common_day)
     
     # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print()
    print('The most common start hour for bikeshare use was: ', common_hour)

    #prompt user if they would like to continue
    continue_prompt()

    #test to make sure hour is filtering correctly: run this code print(df.groupby(['hour'])['hour'].count())
    print('\n')
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print()
    print('The most common start station is for your selection of month and day is ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print()
    print('The most common end station is for your selection of month and day is ', common_end_station)

    # display most frequent combination of start station and end station trip
    common_combo = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending = False).head(1)

    print()
    print('The most frequent combination of start station and end station for your selection of month and day is \n', common_combo)
    print()

    # display a table of the least common combinatino of stations if the user accepts
    while True:
        least_common = input ('Would you like to see the top 20 (if available) least frequent Start and End Station combinations? Yes or No: ')
    
        if least_common.lower() in yes_list:
            least_common_combo = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending = True).head(20)
            print()
            print('The top 20 least frequent combination of start stations and end stations for your selection of month and day are \n', least_common_combo)  
            continue_prompt()

        elif least_common.lower() in no_list:
            print()
            print('Okay, we will move on to the next section!')
            break
        
        else:
            print()
            print('That was not a valid entry. Please enter yes or no.')
            continue 
            

    print('\n')
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def convert(seconds):
    """
    Converts seconds into a more user-friendly time measurement. 
    """    
    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d days, %d hours, %02d minutes, and %02d seconds" % (days, hours, minutes, seconds)

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    sum_time = df['Trip Duration'].sum()
    print('The total travel time in seconds was ',sum_time,'.')       
    total_travel_time = convert(sum_time)
    
    print('The total travel time for the period you selected was {}.'.format(total_travel_time))

    # display mean travel time
   
    mean_time = df['Trip Duration'].mean()

    print()
    print('The mean travel time in seconds was ',mean_time,'.')       
    mean_travel_time = convert(mean_time)
    
    print('The mean travel time for the period you selected was {}.'.format(mean_travel_time))

    print()
    continue_prompt()
    
    print('\n')
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """
    Displays statistics on bikeshare users.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
   
    user_count = df.groupby(['User Type'])['User Type'].count()
    print()
    print('The table below will demonstrate the counts by User Type: \n', user_count)

    # Display counts of gender
   
    while True:
        if 'Gender' in df.columns:
            gender_count = df.groupby(['Gender'])['Gender'].count()
            print()
            print('The table below will demonstrate the counts by Gender: \n', gender_count)
            break
        else: 
            print()
            print('Sorry, but we do not have any gender data for Washington, so we cannot show you counts by gender.')
            break
    
    # Display counts of null gender values
    
    while True: 
        if 'Gender' in df.columns:
            gender_null_count = df['Gender'].isnull().count()
            print()
            print('There are {} counts of null Gender data.'.format(gender_null_count))
            break
        else: 
            print()
            print('Sorry, but we do not have any gender data for Washington, so we cannot show you null gender data.')
            break 

    # Display earliest, most recent, and most common year of birth
    while True:
        if 'Birth Year' in df.columns:
            earliest_year = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].mode()[0]
            print()
            print('The earliest birth year of users for this time period is: ', earliest_year)
            print()
            print('The most recent birth year of users for this time period is: ', most_recent)
            print()
            print('The most common birth year of users for this time period is: ', most_common)
            break
        else: 
            print()
            print('Sorry, but we do not have any birth year data for Washington.')
            break
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        try:    
            city, month, day = get_filters()
            df = load_data(city, month, day)
        
            raw_data(df)
            time_stats(df, month, day)                
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            print('\nThank you for your interest in the Bike Share Data!\n')
            print()
            while True:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() in yes_list:
                    break
                    main()
                elif restart.lower() in no_list:
                    print()
                    print('Goodbye!')
                    sys.exit()
                else:
                    print()
                    print('That was not a valid entry. Please enter yes or no.')
                    continue 
                
        except KeyboardInterrupt:
            print()
            print("You've chosen to leave the program. Goodbye! \n")
            sys.exit()

if __name__ == "__main__":
	main()


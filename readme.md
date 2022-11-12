# Katia's Bike Share Data Project

## About This Project

Hello! Welcome to my Bike Share Python Project. 

This project was created to meet completion requirements for my 
Udacity [Programming for Data Science with Python](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104) course. 

Through this course, I learned basics of Python programming and how to create a program that could conduct some descriptive statistical analysis of US Bike Share data. This program prompts the user with some questions about the following:
* which city they want to filter data for
* which month they want to filter data for
* which day they want to filter data for 

The program also checks for whether the user wants to continue through the various statistical analysis checkpoints.

I hope you enjoy the project and get to learn some fun facts about US Bike Share data!

# About the Datasets

The datasets provided by Motivate, a bike share system provider in the US, contains randomly selected data for the first six months of 2017 for all three cities. The data files for all three cities contain the same core six columns:

* Start Time
* End Time
* Trip Duration
* Start Station
* End Station
* User Type

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

## Software Requirements

To run this program, you will need to access your command line interface and python. Steps to run the program:
1. Clone the bikeshare_final-project.py file to a local repository.
2. Save the data files to your repository.
3. Run the program.

## Files You Will Need to Download

You'll first need to go [here](https://www.kaggle.com/code/deepak525/us-bike-share-analysis/data) to download the .csv files for Chicago, New York, and Washington to run this program on your machine. Make sure to save these files in the same directory as the .py file.

## Credits and Resources

Below are the sites I referred to in writing my script for the Bike Share data.

1. Substituting a blank value with an integer. [%d opeartor][1]
[1]: https://www.geeksforgeeks.org/difference-between-s-and-d-in-python-string/

2. Converting seconds into a more user-frindly time output. [Time Conversion][2]
[2]: https://www.w3resource.com/python-exercises/python-basic-exercise-65.php

3. Calcuating the most frequent combination of values in a DataFrame. [Frequent Combo][3]
[3]: https://stackoverflow.com/questions/63229237/finding-the-most-frequent-combination-in-dataframe

4. Converting date to a date-time series. [Datetime][4]
[4]: https://stackoverflow.com/questions/60131336/datetime-series-property

5. Identifying the day of the week with pandas. [Weekday][5]
[5]: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html

6. Finding the first row(s) of a dataframe. [head()][6]
[6]: https://www.geeksforgeeks.org/how-to-get-first-row-of-pandas-dataframe/

7. Exiting a python program. [Exit][7]
https://learnpython.com/blog/end-python-script/

8. Identifying isnull values. [Isnull][8]
[8]: https://stackoverflow.com/questions/62442411/how-can-i-get-df-isnull-for-a-single-column-of-a-dataframe

9. Verifying a column's existence. [Verify column][9]
[9]: https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas


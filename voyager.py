"""File: voyager.py
Date completed: 01/15/2023
Description: This program prompts the user for an integer indicating the
number of days since September 25th, 2009. It then computes and returns
the distance of Voyager 1 from the sun in miles, kilometers, AU, and the
round-trip time in hours for radio communication.
"""
# import datetime module
import datetime

# assign all variables for conversions
start_miles = 16637000000
travel_speed_mph = 38241
miles_to_km = 1.609344
miles_to_au = 92955887.6
# radio communication conversion takes more steps to go from m/s to mi/hr
meters_to_miles = 1609.34
seconds_to_hours = 3600
speed_of_light = 299792458

# collect input, then type cast to integer
num_of_days = input("How many days has it been since September 25th, 2009? ")
num_of_days = int(num_of_days)

# calculate current date
start_date = datetime.date(2009, 9, 25)
end_date = start_date + datetime.timedelta(days=num_of_days)

# compute miles
end_miles = start_miles + travel_speed_mph * num_of_days

# compute kilometers
end_kilometers = end_miles * miles_to_km

# compute au
end_au = end_miles / miles_to_au

# compute radio communication time
meters_per_hour = speed_of_light / seconds_to_hours
radio_mph = meters_per_hour / meters_to_miles 
radio_time = end_miles / radio_mph

# print results
print("As of ",end_date,"the Voyager I Spacecraft is:\n\n",
    end_miles,"MILES away from the sun.\n",
    end_kilometers,"KILOMETERS away from the sun.\n",
    end_au,"ASTRONOMICAL UNITS (AU) away from the sun.\n",
    "Round-trip radio communication would take",radio_time,"hours.")
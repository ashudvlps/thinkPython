'''
1. How many seconds are there in 42 minutes 42 seconds?
'''
sec = 42*60+42
print(str(sec)+' seconds')

'''
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers
in a mile.
'''
miles = 10/1.61
print(str(round(miles, 2))+' Miles')

'''
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
pace (time per mile in minutes and seconds)? What is your average speed in miles
per hour?
'''
pace_in_min = int(sec/miles)/60
rem_pace_in_sec = int(sec/miles)-pace_in_min*60
print(str(pace_in_min)+' Min '+str(rem_pace_in_sec)+' sec')
print(str(miles*3600/sec)+' Miles/Hour')

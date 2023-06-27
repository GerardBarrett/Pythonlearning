def nl(): #new line cos of laziness to type the print new line command. Trick picked up from the TCM course.
	print('\n')
# Using the input command to ask a question and store the result in the variable. You use this a lot.

#TIME TAKEN
run = input("How many minutes do you want to run for per set? ")      # Length of run in set
walk = input("How many minutes do you want as a walking break? ")     # Length of walk in set
sets = input("How many sets? ")                                       # How many sets user wishes to do

running = float(run) * float(sets)      # How many minutes walking the user will complete across all the sets.
#print(running) - I find it useful to test what has been stored in variables by printing the output. Commented out for now.
walking = float(walk) * float(sets)     # How many minutes walking the user will complete across all the sets.

print("You will run for " + str(running) + " minutes and walk for "+ str(walking) + " minutes") # Disclose how long the running and walking will be.
nl() # space out the output.

# DISTANCE COVERED
run_pace = input("How fast do you run a mile? Enter pace in MM:SS ").split() # Take an input for the pace the user currently runs.
for time in run_pace:
      min, sec = [int(i) for i in time.split(":")]     # Action the split. So the split will be actioned on the :
                                                       # If you wanted to add in a time for hours, you can use it as hour, min, sec but you must ensure there are enough arguments.

running_total_seconds = ((int(min) * 60) + int(sec))   # convert the time to seconds for easy calculations later on.

walk_pace = input("How fast do you walk a mile? Enter pace in MM:SS ").split() # Take an input for the pace the user currently walk.
for time in walk_pace:
     min, sec = [int(i) for i in time.split(":")]
walking_total_seconds = ((int(min) * 60) + int(sec))

distance_running = float(running)*60 / float(running_total_seconds)   # Calculate the distance ran
distance_walking = float(walking)*60 / float(walking_total_seconds)   # Calculate the distance walked

print("During your session you will cover " + str(round(distance_running + distance_walking, 2)) + " miles") # output the distance covered by user. the round command is used to limit the distance to 2 decimal places.
nl()

# PACE CALCULATION
distance = input("In miles, how far would you like to run? ") # Obtain the desired distance.

print("How quickly would you like to run? ") # Ask the question of how quickly they wish to complete this distance.
desired_time = input("Enter times in HH:MM:SS\n").split() # store the desired time as a variable.
for time in desired_time:
     hour, min, sec = [int(i) for i in time.split(":")]
##sets = input("How many walking breaks would you like? ")       # v0.2 will look to add in walking breaks so a user can work out how many breaks they can afford to add.
total_seconds = (int(hour) * 3600) + (int(min) * 60) + int(sec)  # Get the desired time in seconds.
seconds_per_mile = float(total_seconds) / float(distance)        # Get the rate needed in seconds.
#print(seconds_per_mile)
minutes_per_mile = int(seconds_per_mile / 60)                    # Get the rate in minutes. Note this is an integer rather than float so will return a whole digit.
#print(minutes_per_mile)
seconds_remainder = int(seconds_per_mile - (minutes_per_mile * 60))   # Find the remaining seconds in the pace requirement.
#print(seconds_remainder)
print ('To complete in this time you need an average pace {}:{:02d} minutes per mile'.format(minutes_per_mile, seconds_remainder)) # Output the pace using the {} and {:02d}. The placement is decided by the .format having minutes_per_mile first and the seconds_remainder afterwards. 
# The :02d denotes that there will need to be two digits returned for seconds per mile.

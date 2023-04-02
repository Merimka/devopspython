# A Devops engineer needs to manitor the remaining time for a
# long- running task on a server. They have the total time the task
# takes in hours, minutes, and seconds, and they know the time that
# has already passed. They want to calculate the remaining time for
# the task to complete.


# Step 1 : Define the problem inputs.

#Total time for the task (hours,minutes,seconds)
total_hours = 5
total_minutes = 25
total_second = 15 

passed_hours = 2
passed_minutes = 45
passed_second = 30

# Hint -> It's easier to work with a single unit of time
#3600 second in hours (60*60) 
# converted to second minute and hours
total_time_in_second = total_hours * 3600 + total_minutes * 60 + total_second

passes_time_in_sec = passed_hours * 3600 + passed_minutes * 60 + passed_second

# This will give us the remaining time in second.
remaining_total_seconds = total_time_in_second - passes_time_in_sec 


# Our goal is to convert remaining second in minutes hours and second
# How many hours we have in the remaining_seconds

remaining_hours = remaining_total_seconds //3600
remaining_minutes = remaining_total_seconds % 3600 // 60
remaining_seconds =  remaining_total_seconds % 60
print(remaining_hours)
print(remaining_minutes)
print(remaining_seconds)









import math

# Method to calculate the time in terms of hours, minutes and seconds


def calculate_time(time):
    decimal, whole = math.modf(time / 60)
    seconds = decimal * 60

    whole /= 60

    dec, who = math.modf(whole)
    minutes = dec * 60
    hour = who
    return hour, minutes, seconds


# Prompt the user to enter distance in km
km = int(input("How many kilometer? "))
# Prompt the user to enter starting time in seconds
starting_time = int(input("Starting time: "))
# Prompt the user to enter decrement of seconds per km
decrement = int(input("Decrement of seconds per km: "))

# Initialized min_speed and max_speed variable
min_speed = ""
max_speed = ""

sum = starting_time
result = starting_time
for i in range(km - 1):
    result -= decrement
    sum += result
    if i == (km - 2):
        max_hour, max_minutes, max_seconds = calculate_time(result)
        if max_seconds > 9:
            max_speed = "{}:{}".format(int(max_minutes), int(max_seconds))
        else:
            max_speed = "{}:0{}".format(int(max_minutes), int(max_seconds))

hour, minutes, seconds = calculate_time(sum)
print("Time spend running: {}h:{}m:{}s\n".format(
    int(hour), int(minutes), int(seconds)))

# Calculate the minimum and maximum estimated speed
min_hour, min_minutes, min_seconds = calculate_time(starting_time)
if min_seconds > 9:
    min_speed = "{}:{}".format(int(min_minutes), int(min_seconds))
else:
    min_speed = "{}:0{}".format(int(min_minutes), int(min_seconds))

print("Minimum speed: {}/km\nMaximum speed: {}/km".format(min_speed, max_speed))

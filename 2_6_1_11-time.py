hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Add the duration to the starting minutes
total_mins = mins + dura

# Calculate the number of hours and minutes from the total minutes
end_hour = (hour + total_mins // 60) % 24
end_mins = total_mins % 60

print(f"The event ends at {end_hour:02d}:{end_mins:02d}")

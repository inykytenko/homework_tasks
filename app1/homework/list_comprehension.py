# output list with work days and output weekend set


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekend = ('Saturday', 'Sunday')

work_days = [day for day in days if day not in weekend]
print(work_days)
print(weekend)


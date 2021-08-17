day = int(input("""write current day in number. 
Sunday is    0\nMonday is    1\nTuesday is   2\nWednesday is 3\nThursday is  4\nFriday is    5\nSaturday is  6\n"""))

nights = int(input('how mane nights: '))

return_day = 3 + (nights - ((nights/7) * 7))
if return_day > 6:
	return_day = return_day - (7 * (return_day/7))
print('You will return the day number', return_day)

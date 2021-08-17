cur_time = input('current time: ')
alarm =	input('alarm_time: ')

idx = alarm / 24
time = cur_time + (alarm - (idx * 24))
if time > 24:
	idx = time/24
	time = time - (idx * 24)

print("time will be ", time)

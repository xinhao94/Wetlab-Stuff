# Convert plate reader time in seconds to hh:mm:ss

def format_elapse_time(time: int) -> str:
  hour = int(time / 60)
  hour_str = str(hour)
  if hour < 10:
    hour_str = "0" + hour_str
  time -= hour * 60

  minute = time;
  minute_str = str(minute)
  if minute < 10:
    minute_str = "0" + minute_str

  return hour_str + ":" + minute_str + ":00"

interval = int(input('Please enter the reading interval in min: '))
num_readings = int(input('Please enter the number of readings: '))

raw_time = []
curr_time = -interval
for i in range(num_readings):
  curr_time += interval;
  raw_time.append(curr_time)

# print(raw_time)

for time in raw_time:
  print(format_elapse_time(time))

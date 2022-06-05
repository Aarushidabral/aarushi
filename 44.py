#current date and time
from datetime import datetime
today=datetime.now()
print("current date and time=",today)
dt=today.strftime("%B %d,%Y %H:%M:%S")
print("current date and time=",dt)

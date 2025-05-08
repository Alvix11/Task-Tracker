from datetime import datetime

def actual_date_and_time():
    # Gets date and time in current time
    present_date = datetime.now() 
    return present_date.strftime("%A %d de %B, %H:%M")
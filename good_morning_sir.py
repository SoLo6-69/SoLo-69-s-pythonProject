import time

t = time.strftime('%H:%M:%S')

hour = int(time.strftime('%H'))
if hour < 12:
    print(t, 'GoodMorning Sir')
elif hour > 12:
    print(t, "GoodAfternoon Sir")
else:
    print(t, "GoodEvening Sir")

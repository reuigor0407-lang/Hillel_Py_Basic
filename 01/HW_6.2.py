sec = int(input("Enter the second: "))

if sec >= 0 and sec <= 8640000:
    days = sec // (24 * 3600)
    hours = (sec % (24 * 3600)) // 3600
    minutes = ((sec % (24 * 3600)) % 3600) // 60
    seconds = ((sec % (24 * 3600)) % 3600) % 60

    time = str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

    if days % 100 in (11, 12, 13, 14):
        word = " днiв "
    elif days % 10 in (2, 3, 4):
        word = " днi "
    elif days % 10 == 1:
        word = " день "
    else:
        word = " днiв "
    print(str(days) + word + time)

else:
    print("Invalid input")

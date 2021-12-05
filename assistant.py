def add_fun():
    event = input("What is the name of the event?")
    day = input("On which day would you like to schedule the event?")
    start = input("What is the start time?")
    end = input("What is the end time? ")
    f = open("data.txt", "a")
    f.write("event name" + ":" + event)
    f.write("\n" + "date" + ":" + day)
    f.write("\n" + "start_time" + ":" + start)
    f.write("\n" + "end_time" + ":" + end)
    f.close()


def check_fun():
    time_list = []
    data_file = open("data.txt", "r")
    for line in data_file.readlines():
        if len(line) != 2:
            continue
        time_list.append(line.split()[2])
        data_file.close()
    return line


while True:
    greetings = "Hello there, it's Hal, your friendly scheduling assistant! "
    print(greetings)
    add_check = input(
        "Would you like to add a new event, or check an existing time slot?"
    )
    if add_check == "add":
        add_fun()
        print("Successfully added the event to your day!")
    elif add_check == "check":
        day = input("On which day would you like to check for scheduled events?")
        time = input("What time would you like to check for availability?")
        get_time = check_fun()
        if time < get_time:
            print("At that time, you'll be busy with CS41 Lecture.")
    else:
        print("I'm sorry Dave, I'm afraid I can't let you do that.")

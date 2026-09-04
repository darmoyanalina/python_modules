def ft_count_harvest_recursive(day=0, days=0):
    if day == 0:
        days = input("Days until harvest: ")
    if day < int(days):
        print(f"Day {day + 1}")
        ft_count_harvest_recursive(day + 1, days)
    else:
        print("Harvest time!")

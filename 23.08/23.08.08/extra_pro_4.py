year, month, day = input().split(".")


def x_month(month_input):
    try:
        test = int(month_input)
        return 1
    except ValueError:
        if month_input == "XX":
            return 3
        elif month_input == "X":
            return 9
        elif month_input.startswith("X"):
            return 1
        else:
            return 3


def x_day(day_input):
    try:
        test = int(day_input)
        return 1
    except ValueError:
        if day_input == "XX":
            return 22
        elif day_input == "X":
            return 9
        elif day_input.startswith("X"):
            if day_input.endswith("0") or day_input.endswith("1"):
                return 3
            else:
                return 2
        else:
            if day_input.startswith("3"):
                return 2
            else:
                return 10


print(x_month(month) * x_day(day))

while True:
    fuel_load = input("Fraction: ")
    divided_by = fuel_load.find("/")

    try:
        x = int(fuel_load[:divided_by])
        y = int(fuel_load[divided_by+1:])
        percent = (x / y) * 100

        if x > y:
            continue
        break

    except (ValueError, ZeroDivisionError):
        continue


if percent >= 99:
        print("F")

elif percent <= 1:
            print("E")

else:
      percent = int(round(percent))
      percent = str(percent)
      print(percent + "%")
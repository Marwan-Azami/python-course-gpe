
# 1h  -> 60 min
def hours_to_mins(hours):
    return hours * 60

def mins_to_seconds(min):
    return min * 60

def hours_to_seconds(hours):
    return hours * 60 * 60

def print_conversion(heure):
    print("#############Welcome to conversion############")
    print("Heure ", heure)
    min = hours_to_mins(heure)
    print("Min ", min)
    seconds = mins_to_seconds(min)
    print("Seconds ", seconds)
    print("Direct conversion  : ")
    print("Conversion :", hours_to_seconds(heure))
    print("###################################")





for counter  in range(10):
    heure = int(input("Donner l'heure"))
    print_conversion(heure)
def get_max_temp(temps):
    return max(temps)

def get_min_temp(temps):
    return min(temps)

def get_sredn_temp(temps):
    return sum(temps)/len(temps)

def get_max_min_temp(temps):
    max_temp=max(temps)
    min_temp=min(temps)
    count_max = temps.index(max_temp)
    count_min = temps.index(min_temp)
    return count_min, count_max

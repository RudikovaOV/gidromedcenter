def filesave(name_file,temps):
    f=open(name_file, "w")
    f.writelines(list(map(str,temps)))
    f.close()

def filereadtemps(name_file):
    name_file += ".txt"
    data_temps = open(name_file, "r")
    data_temps_out = list(map(int, data_temps.readlines()))
    data_temps.close()
    return data_temps_out

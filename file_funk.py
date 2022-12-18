def filesave(name_file,temps):
    f=open(name_file, "w")
    f.writelines(list(map(str,temps)))
    f.close()

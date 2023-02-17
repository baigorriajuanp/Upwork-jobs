def main():

    route_in = r"path of origin file"
    route_out = r"path of final file"
    users_list = ""
    count = 0

    f = open(route_in, "r")
    for users in f:
        users = users.strip("\n")
        users_list = users_list + users + " "    

    f.close()

    lista = users_list.split()
   
    f = open(route_out, "w")

    for i in lista:
        f.write(i)
        if count%3 != 2:
            f.write(" ")
        else:
            f.write("\n")
        count += 1

    f.close()
  
if __name__ == "__main__":
    main()

def ve_vieng_hinh_vuong(kich_thuoc):

    for i in range(kich_thuoc):

        for j in range(kich_thuoc):

            if i == 0 or i == kich_thuoc - 1 or j == 0 or j == kich_thuoc - 1:

                print("* ", end="")

            else:

                print("  ", end="")

        print()



kich_thuoc = int(input("Nhập kích thước của hình vuông: "))

ve_vieng_hinh_vuong(kich_thuoc)

names = ["c_minus_axe-", "c_plus_axe-", "pot-axe-"]
for name in names:
    for i in range(50, 2001, 50):
        if i < 100:
            n = f"{name}00{i}"
        elif 100 <= i < 1000:
            n = f"{name}0{i}"
        else:
            n = name + str(i)
        with open(f'Data/{n}', encoding="utf-8", mode="r") as file_read:
            info = file_read.read()
        with open(f'Data1/{n}.txt', encoding="utf-8", mode="w") as file_write:
            file_write.write(info)

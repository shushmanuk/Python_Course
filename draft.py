name = "Shushanik"
# print(name.upper())
# print(name.lower())
# print(name.partition("a"))
# print(name.replace("ik",""))
# print(name.split("h"))
# print(name.capitalize())
# print(name.casefold())
# print(name.center(len(name), "h"))
# print(name.count("h"))
# print(name[::-1])
# print(name.encode("utf-8"))
# print(name.expandtabs())
# print(name.endswith("ik"))
# print(name.rfind("h"))
# print(name.format("h"))
# print(name.format_map("h"))
# # print(name.rindex("h"))
# print(name.isalnum()) #եթե թիվ ու տառ է մենակ՝ True, եթե գոնե մեկ նշան՝ False
# print(name.isalpha()) #եթե բոլորը տառեր են
# print(name.isascii())
# print(name.isdecimal()) #եթե բոլորը ամբողջ թվեր են առնվազն մեկ հատ
# print(name.isdigit()) #եթե բոլորը թվեր են
# print(name.isidentifier())
# print(name.islower()) #եթե բոլորը փոքրատառ են
# print(name.isnumeric()) #եթե բոլորը թիվ են
# print(name.isprintable()) #\n \t False տվեց, դատարկն ու մնացածը True
# print(name.isspace()) #եթե մեկ և ավելի բացատ կա բայց ուրիշ ոչինչ
# print(name.istitle()) #եթե առաջին տառը մեծատառ է
# print(name.join(["ik"]))
# # print(name.keys())
# # print(name.values())
# print(name.ljust(30)) #???
# print(name.lstrip()) #???
# print(name.maketrans("h","3"))
# print(name.removeprefix("Sh")) #հեռացնում է միայն առաջին string֊ի սկզբի հատվածը, որը նշված է
# print(name.removesuffix("ik")) #․․․ վերջի ․․․
# print(name.rjust(10)) #անհասկանալի space֊եր դրեց
# print(name.rpartition("h")) #բաժանում է նշվածով, պահպանելով նշվածը որպես առանձին str բաժանարար
# print(name.split("an")) #բաժանում է նշվածով, հեռացնելով նշվածը
# print(name.strip()) #կտրում է ավելորդ space֊երը եզրերից, rspace֊ը՝ միայն աջից
# print(name.splitlines(5))
# print(name.startswith("Shu"))
# print(name.swapcase()) #առաջին տառերը՝ փոքրատառ
# print(name.title()) #․․․ մեծատառ
# print(name.translate(""))
# name = "12000"
# print(name.zfill(10))



# name1 = "Shushanik"
# list1 = list(name1)
# list1[5:] = "iki"
# name2 = ''.join(list1)
# print(name2)

pin = input("Please, enter a pin: ")
cond_1 = len(pin) == 4 or len(pin) == 6
cond_2 = pin.isdigit()
cond_3 = pin.isspace()
print(bool(cond_1 * cond_2 * (not cond_3)))



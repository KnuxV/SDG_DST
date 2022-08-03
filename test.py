CU = ("Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark",
              "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy",
              "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland",
              "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden""Iceland", "Liechtenstein", "Norway", "Switzerland", "United Kingdom")

# CU = CU.replace(", ", " OR ")
CU = list(CU)
str_cu = " OR ".join(CU)
print(str_cu)
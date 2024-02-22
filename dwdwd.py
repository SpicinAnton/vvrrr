user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)

user = User()
user.surname = "Name"
user.name = "Surnemov"
user.age = 35
user.position = "zam capitana"
user.speciality = "repairman"
user.address = "module_2"
user.email = "repairman22@mars.org"
user.hashed_password = "vrachhhh"
session.add(user)

user = User()
user.surname = "Evgeni"
user.name = "Rod"
user.age = 28
user.position = "glanvi security"
user.speciality = "security"
user.address = "module_3"
user.email = "genia44@mars.org"
user.hashed_password = "vefefef"
session.add(user)

user = User()
user.surname = "Diana"
user.name = "Mumba"
user.age = 19
user.position = "healer"
user.speciality = "medic"
user.address = "module_4"
user.email = "vrach441@mars.org"
user.hashed_password = "vefefopthtef"
session.add(user)

from train import train


class booking:
    def __init__(self, name, age, train_no, berth):
        self.name = name
        self.age = age
        self.train_no = train_no
        self.berth = berth

    def checker(self):
        self.cnt = 0
        for i in train_list:
            if(self.train_no == i.no):
                if(self.berth == "lb"):
                    self.cnt = i.lb

                if(self.berth == "mb"):
                    self.cnt = i.mb
                if(self.berth == "ub"):
                    self.cnt = i.ub
            if(self.cnt > 0):
                return 1
            else:
                return 0


train_list = []

booking_list = dict()
exit = 0
choice_list = ["1. book", "2. status", "3 .cancel", "4 .chart", "5. exit"]


def get_status():
    print("the details are as following :\n")
    print("{0:<10}{1:<10}{2:<10}{3:<10}".format(
        "train no", "from", "to", "departure"))
    for i in range(len(train_list)):
        print("{0:<10}{1:<10}{2:<10}{3:<10}".format(
            train_list[i].no, train_list[i].from_, train_list[i].to_, train_list[i].departure))


def create_train():
    train_no = [1, 2, 3, 4]
    from_list = ["a", "b", "c", "d"]
    to_list = ["z", "y", "x", "w"]
    dept_list = ["1", "2", "3", "4"]
    print("enter train details_\n")
    for i in range(4):
        train_list.append(
            train(train_no[i], from_list[i], to_list[i], dept_list[i]))


def cancel():
   # printf("enter booking no:")
    global booking_list
    print(booking_list)
    no = int(input("Enter your booking no"))
    if(no in booking_list):
        del booking_list[no]
        print("successfully deleted😀😀😀")
    else:
        print("no such booking")


create_train()
booking_no = 0
while(exit != 1):
    print("enter choice\n  _______________________________")
    for i in range(len(choice_list)):
        print(choice_list[i])
    choice = int(input())
    if(choice == 1):
        name = input("name ")
        age = int(input("age "))
        train_no = int(input("train no "))
        berth = input("berth ")
        if(booking(name, age, train_no, berth).checker() == 1):
            
            for i in train_list:
                if(i.no == train_no):
                    if(berth == "lb"):

                        i.lb -= 1
                        i.book()
                        latest=i.latest
                    elif(berth == "ub"):
                        i.ub -= 1
                        i.book()
                        latest=i.latest
                    else:
                        i.mb -= 1
                        i.book()
                        latest=i.latest
                    break
            booking_list[latest] = booking(name, age, train_no, berth)
            print("latest",latest)
            print("confirmed ,,,your booking no and seat no is is",
                  latest, latest)

        else:
            print("no preffered train// check another")
    elif(choice == 2):
        get_status()
        
    elif(choice == 5):
        exit = 1
    elif(choice == 3):
        cancel()
        print(booking_list)

    else:
        print("enter valid")

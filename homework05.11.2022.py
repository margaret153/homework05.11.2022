import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.alive = True

    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Auto(brand_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('I happy')
            self.gladness += 10
            self.money -= 15
            self.satiety += 2


    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self):
        print(f"satiety = {self.satiety}")
        print(f"money = {self.money} $")
        print(f"gladness = {self.gladness} level of happiness")
        print(f"brand of car = {self.brand}")
        print(f"level of fuel in the car = {self.fuel}")
        print(f"your car is good if its start is more than 0 = {self.strength}")
        print(f"your home tidy level = {self.home.mess}")
        print(f"level of food in the house = {self.home.food}")




    def is_alive(self):
        if self.satiety <= 0:
            self.alive = False
            print("You wanted to eat and you ate raw meat than you got poisoned.")
        elif self.gladness <= 0:
            self.alive = False
            print("depression")
        elif self.money <= -300:
            self.alive = False
            print("You got bad mood")

    def live(self):
        if self.is_alive() == False:
            return False
        if self.home == None:
            print('Settled in the house')
            self.ger_home()
        if self.car == None:
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f"I don't have a job going to get a job {self.job.job}" )
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        if self.gladness < 20:
            if self.home.mess > 15:
                print("I want chill, but mess")
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money < 0:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_home()
        elif dice == 4:
            print("Time for shopping")
            self.shopping(manage='delicacies')









class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_of_car[self.brand]['fuel']
        self.strength = brand_of_car[self.brand]['strength']
        self.consumption = brand_of_car[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False

class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {'Java': {'salary': 50, 'gladness_less': 10},
            'Python': {'salary': 40, 'gladness_less': 3},
            'C++': {'salary': 70, 'gladness_less': 25},
            'Rust': {'salary': 60, 'gladness_less': 1}}

brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
                'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
                'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
                'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14}}



nick = Human(name='Nick')
for day in range(1,8):
    if nick.live(day) == False:
        break
import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.satiety = 50
        self.food = 70
        self.gladness = 60


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
        if self.food <= 0:
            self.eating('EAT')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satienty += 6
            self.home.food -= 6

    def eat(self):
        if self.home <= 0:
            self.shopping('food')

    def work(self):
        if self.car.drive()
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
            if manage == 'fuel' :
                print('I bought fuel')
                self.money -= 100
                self.car.fuel += 100
            elif manage == 'food':
                print('Bought food')
                self.money -= 50
                self.home.food += 50
            elif manage == 'delicacies' :
                print('I happy')
                self.gladness += 10
                self.money -= 15
                self.satienty += 2


    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def days_indexes(self):

    def is_alive(self):
        pass
    def live(self):
        pass

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
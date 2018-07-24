#_*_coding:utf-8_*_
__author__ = 'Alex Li'

#######################
#  策略模式 模板接口  #
#######################
class TravelStrategy(object):
    '''
    出行策略
    '''

    def travelAlgorithm(self):
        pass

class AirplaneStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("坐飞机出行....")

class TrainStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("坐高铁出行....")


class CarStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("自驾出行....")

class BicycleStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("骑车出行....")


class TravelInterface(object):
    def __init__(self,travel_strategy):
        self.travel_strategy = travel_strategy

    def set_strategy(self,travel_strategy):
        self.travel_strategy = travel_strategy

    def travel(self):
        return self.travel_strategy.travelAlgorithm()



#坐飞机
travel = TravelInterface(AirplaneStrategy())

travel.travel()

#改开车
travel.set_strategy(CarStrategy())
travel.travel()


#####################
# 策略模式 外链接口 #
#####################

import types


class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')
# -*- coding: utf-8 -*-
#建造者模式

#相关模式：思路和模板方法模式很像，模板方法是封装算法流程，对某些细节，提供接口由子类修改，建造者模式更为高层一点，将所有细节都交由子类实现。
# 建造者模式：将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示。
# 基本思想
# 某类产品的构建由很多复杂组件组成；
# 这些组件中的某些细节不同，构建出的产品表象会略有不同；
# 通过一个指挥者按照产品的创建步骤来一步步执行产品的创建；
# 当需要创建不同的产品时，只需要派生一个具体的建造者，重写相应的组件构建方法即可。


def print_info(info):
    print(info)


class PersonBuilder():
    """建造者基类 车间"""
    def __init__(self):
        pass
    
    def build_frame(self):
        pass

    def build_fly(self):
        pass

    def build_engine(self):
        pass


class J10Builder(PersonBuilder):
    """歼10建造车间"""
    type = '歼10'

    def build_frame(self):
        print_info("建造%s的机身" % self.type)

    def build_fly(self):
        print_info("建造%s的机翼" % self.type)

    def build_engine(self):
        print_info("建造%s的引擎" % self.type)


class J20Builder(PersonBuilder):
    """歼20建造车间"""
    type = '歼20'

    def build_frame(self):
        print_info("建造%s的机身" % self.type)

    def build_fly(self):
        print_info("建造%s的机翼" % self.type)

    def build_engine(self):
        print_info("建造%s的引擎" % self.type)


class JDirector():
    """歼-系列设计师"""
    pb = None

    def __init__(self, pb):
        self.pb = pb

    def create(self):
        self.pb.BuildFrame()
        self.pb.BuildFly()
        self.pb.BuildEngine()


def aviation_industry_chengdu_aircraft_industry():
    """成都飞机工业集团"""
    pb = J10Builder()
    pd = JDirector(pb)
    pd.create()

    pb2 = J20Builder()
    #pd = PersonDirector(pb)
    pd.pb = pb2
    pd.create()
    return


if __name__ == '__main__':
    aviation_industry_chengdu_aircraft_industry()
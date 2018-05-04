class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)

    def grow(self):
        print("%s grows up" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def get_paid(self):
        print("The employee gets paid.")


class Programmer(Employee):
    def __init__(self, name, age, job):
        super(Programmer, self).__init__(name, age, job)

    def design(self):
        print("The programmer designs codes")
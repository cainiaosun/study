class Person:
    '''Represents a person.'''
    population = 0
    def __init__(self,name,age):
        '''Initializes the person's data.'''
        self.name = name
        self.age = age
        print '(Initializing %s)' % self.name
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' %Person.population
    def sayhi(self):
        print "Hi,my name is %s %s"% (self.name,self.age)
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We  have  %d  persons  here.'  %Person.population
print Person.population
test1=Person("sunhongbin","28")
test1.sayhi()
test1.howMany()

test2=Person("lihua","30")
test2.sayhi()
test2.howMany()

test1.sayhi()
test1.howMany()
del test1
del test2


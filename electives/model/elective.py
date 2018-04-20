class Elective:
    def __init__(self,crn='crn', name='name', year='year', day='day', time='time', level='level',
                  instructor='instructor', description='description'):
         self._crn = crn
         self._name = name
         self._year = year
         self._day = day
         self._time = time
         self._level = level
         self._instructor = instructor
         self._description = description

    @property
    def crn(self):
        return self._crn

    @crn.setter
    def crn(self, crn):
        self._crn = crn

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year
        
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day
        
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
        
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level
        
    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    def instructor(self, instructor):
        self._instructor = instructor
        
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
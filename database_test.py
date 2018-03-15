import random

class DataBase:
    def __init__(self):
        self.name = "2A"
        self.students = []

    def add(self, student):
        self.students.append(student)
    
    def remove(self, index):
        self.students.pop(index)
        
    def search(self, name): 
        for index, student in enumerate(self.students):
            if student.name == name:
                return index
    
    def get_histories(self):
        all_histories = []
        for student in self.students:
            all_histories.append(student.history)
        return all_histories
    
    def get_data(self):
        all_data = []
        for student in self.students:
            all_data.append(student.get_data())
        return all_data
    
    def export_data(self, file_name, format=".txt"):
        with open(file_name + format, "w") as file:
            for student in self.get_data():
                file.write(f"{student[0]}-{student[1]}\n")

class Student:
    def __init__(self, name):
        self.name = name
        self.history = {}
    
    def add_history(self, time, program):
        self.history[time] = program
        
    def get_data(self):
        return (self.name, self.history)

names = ["Arvid", "Vincent", "Ida", "SaltyBoye Alex"]
last_names = ["Ilber", "Uden", "Franzén", "Inte ordförande i elevkåren"]
times = ["11:59", "04:20", "13:37", "12:34"]
programs = ["Drive", "Runescape", "Classroom", "Youtube"]

base = DataBase()
for x in range(30):
    tmp = Student(random.choice(names) + " " + random.choice(last_names))
    tmp.add_history(random.choice(times), random.choice(programs))
    base.add(tmp)

base.students[0].add_history("13:10", "Bananpaj")
base.export_data("1")
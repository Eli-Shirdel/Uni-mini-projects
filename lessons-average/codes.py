lessons = [] 
weights = []
with open ("student's course.txt" , "r") as file:
    for line in file.readlines():
        lesson , weight = line.strip().split(', ')
        lessons.append(lesson)
        weights.append(weight)
del lessons[0]

class Student:
    dic = { }
    average = 0
    def __init__(self , name):
        self.name = name

    def average(self):
        sum = 0
        value = 0
        for i in range(0 , len(lessons)):
            for j in weight:
                score = float(input(f"Enter {lessons[i]} score:"))
                self.dic[lessons[i]] = score
                sum  = sum  + int(j) * score
                value = value + int(j)
        average = sum / value

        f = open("students_Info.txt", "a")
        f.write(f"{self.name} , Greades: {self.dic} , Average: {average} \n")
        f.close()
student1 = Student("Nila")
Student.average(student1)
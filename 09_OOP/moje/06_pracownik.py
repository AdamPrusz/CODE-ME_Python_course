# 6▹ Utwórz klasę Pracownik.
# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
# Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. Pracownik powinen odprowadzać
# podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem
# jego składka zdrowotna wynosi 0%.
# Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą
# adres mailowy. Np.
# Adam Kowalski Love Python Company
# email -> smkwlsk@lovepythoncompany.com

import random

class Worker():

    company = "bnpparibas"

    def __init__(self, position, name, surname, seniority):
        self.position = position
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.salary = 3000  #salary for start
        self.student = 0


    def money(self, list):
        for i in list:
            if 1 <= self.seniority < 2:
                self.salary += 500
            if 2 <= self.seniority < 3:
                self.salary += 1000
            if 3 <= self.seniority < 4:
                self.salary += 1500
            if self.seniority >= 4:
                self.salary += 2000
            if self.position == "mid":
                self.salary += 1000
            if self.position == "senior":
                self.salary += 2000
            if self.position == "expert":
                self.salary += 3000
            if self.position == "junior":
                self.salary += 3000

            return self.salary

    def if_student(self, student):
            if self.position == "junior":
                status = random.choice(student)
                self.student = status

            return self.student


    def taxes(self):
        if self.student == "yes":
            health_price = 0
        else:
            health_price = 0.09

        tax = 1 - (0.17 + health_price)

        return tax

    def e_mail(self, letters):
        name = []
        surname = []
        for step in letters:
            if step in self.name:
                name.append(step)

            if step in self.surname:
                surname.append(step)

        return name, surname







job_positions = ["junior", "mid", "senior", "expert"]
names = ['Adam','Aleks', 'Michał', 'Patryk']
surnames = ['Pruszyński', "Markiewicz", "Ludek", "Prysak"]
years_seniority = [0.7, 1.2, 2.1, 3.2]
choice = ['yes', 'no']

cosonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z',
                    'w', 'y']

employees = []
for step in range(4):
    employee = Worker(random.choice(job_positions), random.choice(names), random.choice(surnames),
                          random.choice(years_seniority))
    employees.append(employee)



print(employees[3].name)
print(employees[3].surname)


print(employees[3].position)
print(employees[3].seniority)


money = employees[3].money(employees)
if_student = employees[3].if_student(choice)
print(employees[3].student)



tax = employees[3].taxes()


print(money)
print(tax)

print("full salary is", money * tax)


print(employees[3].e_mail(cosonant))





















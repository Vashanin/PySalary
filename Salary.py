# !/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from Employee import *
from Position import *
from Table import *

class Salary:
    monthes = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December"
    }

    def __init__(self):
        self.employees_info = Employee().get_all_db_data()
        self.positions_info = Position().get_all_db_data()
        self.tables_info = Table().get_all_db_data()

    def calculate_salary_for_all(self):
        try:
            employee_wages = {}
            for position in self.positions_info:
                employee_wages[position["name"]] = position["salaryPerHour"]

            employees = {}
            for employee in self.employees_info:
                employees[employee["id"]] = employee


            salaries = []

            # підраховуємо заробітні плати та формуємо відповідні структури даних
            for table in self.tables_info:
                year = table["year"]
                month = self.monthes[table["month"]]
                employee_id = table["employeeId"]
                current_employee = employees[employee_id]

                employee_name = current_employee["name"]

                position = current_employee["post"]
                wage_per_hour = employee_wages[position]
                employee_rate = current_employee["rate"]

                daily_hours = table["hours"].split(" ")
                sum_of_hours = 0
                amount_of_simple_days = 0
                amount_of_vacation_days = 0
                amount_of_hospital_days = 0
                for day_hours in daily_hours:
                    if day_hours.isnumeric():
                        try:
                            sum_of_hours += int(day_hours)
                            amount_of_simple_days += 1
                        except Exception:
                            traceback.format_exc()
                    if day_hours == "v":
                        amount_of_vacation_days += 1
                    if day_hours == "h":
                        amount_of_hospital_days += 1

                sum = 0.0
                # зарплата за звичайний день
                sum += sum_of_hours * wage_per_hour
                if sum_of_hours > employee_rate:
                    sum_of_hours = employee_rate
                # зарплата за відпустку
                sum += amount_of_vacation_days * (employee_rate / len(daily_hours)) * (wage_per_hour * 0.8)
                # зарплата за лікарняний
                sum += amount_of_hospital_days * (sum_of_hours / amount_of_simple_days) * wage_per_hour

                compiled_salary = (year, month, employee_name, position, str(sum) + " $")
                salaries.append(compiled_salary)

            return tuple(salaries)
        except Exception as e:
            traceback.format_exc()
            print("Trouble with calculate_salary_for_all: " + e.args[0])

    def represent_as_date_dictionary(self, raw_tuple):
        """
        :param raw_tuple: tuple з "сирими" данними про зарплати робітників
        :return: date_dictionary: дані у форматі словника [year][month][employee, position,salary] 
        """
        try:
            date_dictionary = {}

            # переписуємо дані отримані з функції calculate_salary_for_all у відповідній формі, вказаній вище
            for item in raw_tuple:
                year = item[0]
                date_dictionary[year] = {}

            for item in raw_tuple:
                month = item[1]
                year = item[0]
                date_dictionary[year][month] = []

            for item in raw_tuple:
                year = item[0]
                month = item[1]
                date_dictionary[year][month]\
                    .append({"employee" : item[2], "position" : item[3], "salary" : item[4]})

            return date_dictionary

        except Exception as e:
            print("Troubles with represent_as_employee_dictionary: " + e.args[0])
            traceback.format_exc()


    def represent_as_employee_dictionary(self, raw_tuple):
        """
        :param raw_tuple: tuple з "сирими" данними про зарплати робітників
        :return: employee_dictionary: дані у форматі словника [employee][year][month][salary, position]
        """
        try:
            employees_info = {}
            for employee in self.employees_info:
                employees_info[employee["id"]] = employee

            employee_dictionary = {}

            # переписуємо дані отримані з функції calculate_salary_for_all у відповідній формі, вказаній вище
            for item in raw_tuple:
                employee = item[2]
                employee_dictionary[employee] = {}

            for item in raw_tuple:
                employee = item[2]
                year = item[0]
                employee_dictionary[employee][year] = {}

            for item in raw_tuple:
                employee = item[2]
                year = item[0]
                month = item[1]
                employee_dictionary[employee][year][month] = []

            for item in raw_tuple:
                employee = item[2]
                year = item[0]
                month = item[1]
                position = item[3]
                sum = item[4]
                employee_dictionary[employee][year][month]\
                    .append({"position" : position, "sum" : sum})

            print(employee_dictionary.keys())

            return employee_dictionary
        except Exception as e:
            traceback.format_exc()
            print("Troubles with represent_as_employee_dictionary: " + e.args[0])

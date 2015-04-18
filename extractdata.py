from bs4 import BeautifulSoup
from htmlstring import s

soup = BeautifulSoup(s)
td = soup.get_text().split("\n")


def is_course(c):
    if c.count("-") == 2 and len(c) == 12:
        return True


def is_teacher(c):
    if c.replace(" ", "").replace("-", "").isalpha():
        return True


all_data = []
index = 0
while index < len(td):
    if "TEXAS" in td[index]:
        index += 99
    if "REPORT" in td[index]:
        index += 98
    if "." in td[index] and "%" not in td[index]:
        all_data.append(td[index])
        index += 7
    if not td[index].isspace() and td[index] and "%" not in td[index]:
        all_data.append(td[index])
    index += 1


base_course = ""
temp_grades = []
courses_combined = {}
courses_profs = {}
for x in range(len(all_data)):
    if is_course(all_data[x]):
        base_course = all_data[x]
        temp_grades = [all_data[x+1], all_data[x+2], all_data[x+3],all_data[x+4], all_data[x+5], all_data[x+7]]
    if "COURSE" in all_data[x]:
        courses_combined[base_course[0:8]] = [all_data[x+1], all_data[x+2], all_data[x+3],
                                              all_data[x+4], all_data[x+5], all_data[x+7]]
    if is_teacher(all_data[x]):
        courses_profs[base_course] = [all_data[x-7], all_data[x-6], all_data[x-5],
                                      all_data[x-4], all_data[x-3], all_data[x-1], all_data[x]]


def search_course(c):
    course = c.upper()
    try:
        print(course + " AVERAGE: ", end="")
        print(courses_combined[course])
        for key in sorted(courses_profs):
            if course in key:
                print(key + ": ", end="")
                print(courses_profs.get(key))
    except KeyError:
        print("Course not found.")
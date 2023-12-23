import itertools
import random
from prettytable import PrettyTable

# Function to check if there is a course conflict between two groups at a specific time slot and day
def has_conflict(group_schedule, group1, group2, day, time_slot):
    courses_group1 = group_schedule[group1][day][time_slot]
    courses_group2 = group_schedule[group2][day][time_slot]
    return bool(courses_group1.intersection(courses_group2))

# Function to rearrange the schedule for two conflicting groups at a specific time slot and day
def rearrange_schedule(group_schedule, group1, group2, day, time_slot):
    # Swap courses between the two groups at the specified time slot and day
    temp_courses = group_schedule[group1][day][time_slot]
    group_schedule[group1][day][time_slot] = group_schedule[group2][day][time_slot]
    group_schedule[group2][day][time_slot] = temp_courses

# Sample data: Lecturers, courses, groups, classrooms, and constraints
lecturers_courses = {
    'Lecturer1': {'CourseA', 'CourseB', 'CourseC'},
    'Lecturer2': {'CourseB', 'CourseD', 'CourseE'},
    'Lecturer3': {'CourseA', 'CourseD', 'CourseF'}
}

groups_courses = {
    'Group1': {'CourseA', 'CourseB'},
    'Group2': {'CourseC', 'CourseD'},
    'Group3': {'CourseE', 'CourseF'}
}

classrooms = {'Classroom1', 'Classroom2', 'Classroom3', 'Classroom4', 'Classroom5', 'Classroom6'}

# Define a 5-day week and time slots for lectures
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_slots = ['9:00-10:30', '10:45-12:15', '1:00-2:30', '2:45-4:15']

# Initialize schedules for lecturers, groups, courses, and classrooms
lecturer_schedule = {lecturer: {day: {time_slot: set() for time_slot in time_slots} for day in days} for lecturer in lecturers_courses}
group_schedule = {group: {day: {time_slot: set() for time_slot in time_slots} for day in days} for group in groups_courses}
course_schedule = {course: {day: {time_slot: {'Classroom': None, 'Class': set()} for time_slot in time_slots} for day in days} for courses in lecturers_courses.values() for course in courses}
classroom_schedule = {classroom: {day: {time_slot: set() for time_slot in time_slots} for day in days} for classroom in classrooms}

# Randomly assign courses to time slots for lecturers, groups, and classrooms
for lecturer, schedule in lecturer_schedule.items():
    for day, time_slots_data in schedule.items():
        for time_slot in time_slots_data:
            random_course = random.choice(list(lecturers_courses[lecturer]))
            lecturer_schedule[lecturer][day][time_slot].add(random_course)

for group, schedule in group_schedule.items():
    for day, time_slots_data in schedule.items():
        for time_slot in time_slots_data:
            random_course = random.choice(list(groups_courses[group]))
            group_schedule[group][day][time_slot].add(random_course)

for classroom, schedule in classroom_schedule.items():
    for day, time_slots_data in schedule.items():
        for time_slot in time_slots_data:
            random_course = random.choice(list(lecturers_courses[random.choice(list(lecturers_courses))]))
            classroom_schedule[classroom][day][time_slot].add(random_course)

# Assign courses to classrooms in the course_schedule
for day in days:
    for time_slot in time_slots:
        for course, course_data in course_schedule.items():
            classroom = random.choice(list(classrooms))
            course_data[day][time_slot]['Classroom'] = classroom
            classroom_schedule[classroom][day][time_slot].add(course)

# Display initial schedules with classroom numbers using PrettyTable
def display_schedule(schedule, title):
    print(f"{title} Schedule:")
    for group, group_schedule in schedule.items():
        table = PrettyTable()
        table.field_names = ['Day', 'Time Slot'] + list(schedule[group]['Monday'].keys())
        for day in days:
            for time_slot in time_slots:
                row = [day, time_slot]
                row.extend(', '.join(course + f" ({course_schedule[course][day][time_slot]['Classroom']})" for course in group_schedule[day][time_slot]))
                table.add_row(row)
        print(f"\n{group}'s Schedule:")
        print(table)

# Display initial schedules with PrettyTable

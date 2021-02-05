from .models import *
def can_assign(course_list,course):
    return True
def find_student_in_list(students,pk):
    for i in range(len(students)):
        if students[i]['student']==pk:
            return i

def get_students_courses():
    bids = Bid.objects.all().order_by('-value')
    st = Student.objects.all()
    students = [{"student": s.pk,"courses" : []} for s in st]
    for bid in bids:
        student = bid.student.pk
        index = find_student_in_list(students,student)
        course_list = students[index]['courses']
        if can_assign(course_list,bid.course):
            course_list.append(bid.course.pk)
            students[index]['courses']=course_list

    return students

def get_student_courses(student):
    all_students_courses = get_students_courses()
    index = find_student_in_list(all_students_courses,student)
    return all_students_courses[index]

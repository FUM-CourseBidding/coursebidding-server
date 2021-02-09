MAX_UNITS = 20
MIN_UNITS = 14


def max_units(aCourse_list):
    units = 0
    for aCourse in aCourse_list:
        units += aCourse.course.unit
    if units > MAX_UNITS:
        return False
    return True

max_units.errorMsg = "too many units."

def min_units(aCourse_list):
    units = 0
    for aCourse in aCourse_list:
        units += aCourse.course.unit
    if units < MIN_UNITS:
        return False
    return True

min_units.errorMsg = "too few units."

def unique_courses(aCourse_list):
    course_list = []
    for aCourse in aCourse_list:
        course_list.append(aCourse.course)
    if len(set(course_list)) != len(course_list):
        return False
    return True

unique_courses.errorMsg = "two courses of the same subject."

def unique_sessions(aCourse_list):
    session_list = []
    for aCourse in aCourse_list:
        session_list.append(aCourse.session1.return_as_tuple())
        if aCourse.session2 != None: session_list.append(aCourse.session2.return_as_tuple())
        
    if len(set(session_list)) != len(session_list):
        return False
    return True

unique_sessions.errorMsg = "two sessions at the same time."


rules = [max_units, min_units, unique_courses, unique_sessions]
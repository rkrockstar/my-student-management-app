from DatabaseConnection import * #Database Connection is imported here


def insert_student(sid, sname, sdepartment, scourses, sadd, sphone):
    curs = conn.cursor()
    curs.execute("insert into STUDENT_DATABASE values(%d,%s,%s,%s,%s,%d)",
                 (sid, sname, sdepartment, scourses, sadd, sphone))
    conn.commit()


def delete_student(sid):
    curs = conn.cursor()
    curs.execute("delete from COURSE_DATABASE where StudentID=%d", (sid))

    conn.commit()

def list_students_in_a_course(cid, cname, year, sem):
    curs = conn.cursor()
    curs.execute("select STUDENT_ID from COURSE_DATABASE where COURSE_ID = %s", (cid))
    rows = curs.fetchall()
    return rows


def list_courses_of_a_student():
    curs = conn.cursor()
    curs.execute("select * from STUDENT_DATABASE")
    rows = curs.fetchall()
    return rows

def list_department_courses():
    curs = conn.cursor()
    curs.execute("select * from DEPARTMENT_DATABASE")
    rows = curs.fetchall()
    return rows

def list_course_database(course_id, department_name, course_instructor, year, semester):
    curs = conn.cursor()
    curs.execute("select * from COURSE_DATABASE WHERE  COURSE_ID=%d", course_id)
    rows = curs.fetchall()
    return rows


def list_student_database():
    curs = conn.cursor()
    curs.execute("select * from STUDENT_DATABASE")
    rows = curs.fetchall()
    return rows


def list_department_database():
    curs = conn.cursor()
    curs.execute("select * from DEPARTMENT_DATABASE")
    rows = curs.fetchall()
    return rows


def edit_student_info(sid, sname, sdepartment, sadd, sphone):
    curs = conn.cursor()
    try:
        curs.execute("update STUDENT_DATABASE set STUDENT_ID=%d, STUDENT_NAME=%s, STUDENT_DEPARTMENT=%s, STUDENT_ADDRESS=%s, STUDENT_PHONE=%d where STUDENT_ID=%d", (sid, sname, sdepartment, sadd, sphone))
        conn.commit()
        return True
    except:
        pass
        return False

def edit_course_info(cid, dname, cinstructor, year, semester):
    curs = conn.cursor()
    try:
        curs.execute("update COURSE_DATABASE set COURSE_ID=%d, DEPARTMENT_NAME=%s, COURSE_INSTRUCTOR=%s, COURSE_YEAR=%d, SEMESTER=%s where COURSE_ID=%d", (cid, dname, cinstructor, year, semester))
        conn.commit()
        return True
    except:
        pass
        return False


def edit_quarter_info(did, dname, dcourses, year, semester):
    curs = conn.cursor()
    try:
        curs.execute("update DEPARTMENT_DATABASE set DEPARTMENT_ID=%d, DEPARTMENT_NAME=%s, DEPARTMENT_COURSE=%s, COURSE_YEAR=%d, SEMESTER=%s where DEPARTMENT_ID=%d", (did, dname, dcourses, year, semester))
        conn.commit()
        return True
    except:
        pass
        return False

def remove_student_info(sid):
    curs = conn.cursor()
    curs.execute("delete from STUDENT_DATABASE where STUDENT_ID=%d", sid)
    conn.commit()

def remove_course_info(cid):
    curs = conn.cursor()
    curs.execute("delete from COURSE_DATABASE where COURSE_ID=%d", cid)
    conn.commit()

def remove_quarter_info(did):
    curs = conn.cursor()
    curs.execute("delete from DEPARTMENT_DATABASE where DEPARTMENT_ID=%s", (did))
    conn.commit()

def connections():
    c = conn.cursor()
    return c, conn
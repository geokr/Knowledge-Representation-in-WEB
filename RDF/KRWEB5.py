from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, Namespace


def question_a():
    uni = Namespace("http://www.mydomain.org/uni/")

    # import rdf from
    g = Graph()
    g.parse("2\KRWEB3.rdf")

    # locate and load Department
    dep_name = URIRef("http://www.mydomain.org/uni/dep_name")

    # print("Choose one of the following departments:")

    for s, p, o in g.triples((None, dep_name, None)):
        print("*{}" .format(o))

    chosen_department = input(
        '\n Choose a department by typing the fullname of the department as it is seen in the list above.\n> ')

    if chosen_department == "Department of Biosystems and Agricultural Engineering":
        my_department = URIRef("http://www.mydomain.org/uni/BAE")
    elif chosen_department == "Department of Business Administration":
        my_department = URIRef("http://www.mydomain.org/uni/BMA")
    elif chosen_department == "Department of Computer Engineering and Informatics":
        my_department = URIRef("http://www.mydomain.org/uni/CEID")
    elif chosen_department == "Department of Chemistry":
        my_department = URIRef("http://www.mydomain.org/uni/CHEM")
    elif chosen_department == "Department of Civil Engineering":
        my_department = URIRef("http://www.mydomain.org/uni/CIV")
    elif chosen_department == "Department of Food Science and Technology":
        my_department = URIRef("http://www.mydomain.org/uni/DEAPT")
    else:
        print("Wrong input.Try again!")

    qres_faculty = """
            SELECT ?professor ?age ?phone
            WHERE {
            ?x rdf:type <http://www.mydomain.org/uni/#Professor> ;
            uni:has_name ?professor ;
            uni:has_age ?age ;
            uni:has_phone ?phone ;
            uni:member_of ?member_of.

            FILTER (?member_of = ?the_chosen_one).
            }
            """
    faculty = g.query(qres_faculty, initBindings={
                      'the_chosen_one': my_department})

    print("\nPROFESSORS\n<professor's fullname> | <professor's age> | <professor's phone>")
    for row in faculty:
        print("%s | %s | %s " % row)

    qres_students = """
            SELECT ?student ?age ?phone
            WHERE {
            ?x rdf:type <http://www.mydomain.org/uni/#Student> ;
            uni:has_name ?student ;
            uni:has_age ?age ;
            uni:has_phone ?phone ;
            uni:member_of ?member_of.

            FILTER (?member_of = ?the_chosen_one).
            }
            """
    students = g.query(qres_students, initBindings={
        'the_chosen_one': my_department})

    print("\nSTUDENTS\n<student's fullname> | <student's age> | <student's phone>")
    for row in students:
        print("%s | %s | %s " % row)

    qres_classrooms = """
            SELECT ?classroom ?capacity
            WHERE {
            ?x rdf:type <http://www.mydomain.org/uni/#Classroom> ;
            uni:room_name ?classroom ;
            uni:room_capacity ?capacity ;
            uni:room_department ?room_department.

            FILTER (?room_department = ?the_chosen_one).
            }
            """
    classrooms = g.query(qres_classrooms, initBindings={
        'the_chosen_one': my_department})

    print("\nCLASSROOMS\n<Classroom name> | <Classroom capacity>")
    for row in classrooms:
        print("%s | %s " % row)

    qres_lessons = """
            SELECT ?lesson ?taught_by
            WHERE {
            ?x rdf:type <http://www.mydomain.org/uni/#Professor> ;
            uni:has_name ?taught_by ;
            uni:teaches ?l ;
            uni:member_of ?member_of.

            ?l uni:les_name ?lesson.

            FILTER (?member_of = ?the_chosen_one).
            }
            """
    lessons = g.query(qres_lessons, initBindings={
        'the_chosen_one': my_department})

    print("\nLESSONS\n<Lesson name> | <Lesson professor>")
    for row in lessons:
        print("%s | %s " % row)


def question_b():
    uni = Namespace("http://www.mydomain.org/uni/")
    Professor = URIRef("http://www.mydomain.org/uni/#Professor")
    Student = URIRef("http://www.mydomain.org/uni/#Student")
    Department = URIRef("http://www.mydomain.org/uni/#Department")
    Classroom = URIRef("http://www.mydomain.org/uni/#Classroom")
    # import rdf from
    g = Graph()
    g.parse("2\KRWEB3.rdf")

    addition = input(
        "For what entity do you want to add new data for?\nProfessor\nStudent\nDepartment\nLesson\nClassroom\n> ")

    if addition == "Professor":
        pass
    elif addition == "Student":
        pass
    elif addition == "Department":
        pass
    elif addition == "Lesson":
        pass
    elif addition == "Classroom":
        pass


def question_c():
    uni = Namespace("http://www.mydomain.org/uni/")
    g = Graph()
    g.parse("2\KRWEB3.rdf")

    input_URI = input("Enter the URI you wish to search: ")
    search_URI = URIRef(input_URI)

    for s, p, o in g.triples((search_URI, None, None)):
        print("{}  ||  {} ||  {}" .format(s, p, o))

    for s, p, o in g.triples((None, search_URI, None)):
        print("{}  ||  {} ||  {}" .format(s, p, o))

    for s, p, o in g.triples((None, None, search_URI)):
        print("{}  ||  {} ||  {}" .format(s, p, o))


choice = input(
    'Hello there! Which question do you want to execute: A/ B/ C?\n> ')

if choice == "A":
    question_a()
elif choice == "B":
    # question_b()
    print("Sorry this code is not ready to run, try A.")
elif choice == "C":
    question_c()
    #print("Sorry this code is not ready to run, try A.")

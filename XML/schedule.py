import xml.etree.ElementTree as ET
import xmlschema
from pprint import pprint

def schema_check(xmlfile, schemafile):
    xsd = xmlschema.XMLSchema(xmlfile)
    pprint(xsd.is_valid(schemafile))

def search_schedule(xmlfile):
    tree = ET.parse(xmlfile)
    lessons = tree.findall('Lesson')

    my_day = input('Enter the day you wish to see: ' )
    print('\n{}-------{}-------{}'.format('Title', 'Day', 'Professor'))

    for l in lessons:
        title = l.find('Title').text
        professor = l.find('Professor')
        if professor is None:
            professor = ''
        else:
            professor = professor.text
        day= l.find('Lecture/Day').text
        
        if day == my_day:
            print('*{}-------{}-------{}'.format(title, day, professor))

def add_lesson(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    lect_class=[]
    lect_day=[]
    lect_time=[]

    #start input new lesson information
    print('Please enter the information of the Lesson you wish to add.\n')
    Title = input('Title: ')

    lect_num = int(input('\nEnter the number of lectures you want to add for this lesson: '))
    lect_num_ind= 1
    while lect_num > 0:
        print('Enter the information about Lecture {}'.format(lect_num_ind))
        Classroom = input('Classroom: ')
        lect_class.append(Classroom)

        Day = input('Day: ')
        lect_day.append(Day)

        Time = input('Time: ')
        lect_time.append(Time)   

        lect_num -= 1
        lect_num_ind += 1
        
    Professor = input('Professor: ')
    #end input new lesson information

    #start -- creation of new Lesson
    new_lesson = ET.Element('Lesson')
    root.append(new_lesson)

    new_lesson_title = ET.SubElement(new_lesson,'Title')
    new_lesson_title.text = Title

    i=0
    while i != len(lect_class):
        new_lesson_lecture = ET.SubElement(new_lesson, 'Lecture', attrib={'Classroom': lect_class[i]})

        new_lesson_lecture_day = ET.SubElement(new_lesson_lecture, 'Day')
        new_lesson_lecture_day.text= lect_day[i]

        new_lesson_lecture_time = ET.SubElement(new_lesson_lecture, 'Time')
        new_lesson_lecture_time.text= lect_time[i]
        i+=1

    if not Professor:
        pass
    else:
        lect_prof = ET.SubElement(new_lesson, 'Professor')
        lect_prof.text = Professor

    tree.write('test.xml')
    #end -- creation of new element:Lesson

    #empty lists for next input
    for obj in lect_class:
        lect_class.pop()
        lect_day.pop()
        lect_time.pop()

xml_file = input('\nHello user! \n\nI am here to help you with you XML files. Before we begin please give me the name of the XML file you want to use.\n\n> ')

chosen_function=input('\nGreat! Which of the following functions would you like to execute: \nA. Validate XML \nB. Add a new lesson \nC. Search for lectures on a specific day \nD. Exit \n\n> ')

while chosen_function != 'D':
    if chosen_function == 'A':
        xsd_file = input('\nPlease gime me the currosponding xml schema file.\n\n> ')
        schema_check(xml_file, xsd_file)
    elif chosen_function == 'B':
        add_lesson(xml_file)
    elif chosen_function == 'C':
        search_schedule(xml_file)
    else:
        print('Input invalid. Please choose one of the given choices, by entering its first letter')

    to_continue=input('\nDo you want to continue? Y/N\n > ')
    if to_continue == 'N':
        chosen_function = 'D'
    elif to_continue == 'Y':
        chosen_function=input('\n\nWhich of the following functions would you like to execute: \nA. Add a new lesson \nB. Search for lectures on a specific day \nC. Exit \n\n> ')

print('Goodbye!')





import sqlite3
import datetime

def todayDate():
  #print("Current date and time : ")
  today = datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y')
  d = datetime.datetime.strftime(datetime.datetime.today() , '%d %B')
  #print(today)
  #return today;
  return d;

def nextDay(a):
    oneDayLate = datetime.datetime.today() + datetime.timedelta(days=a)
    #print("Time after one day : ")
    #print(datetime.datetime.strftime(oneDayLater , '%d/%m/%Y'))
    oneDayLater = datetime.datetime.strftime(oneDayLate , '%d %B')
    return oneDayLater;
#nextDay()

nd=str(nextDay(1))


DB_NAME = 'Facerecc.db'
conn = sqlite3.connect(DB_NAME)

cmd = "CREATE TABLE IF NOT EXISTS AttendanceRegister (ID INTEGER PRIMARY KEY,NAME VARCHAR,USN INTEGER,"+"\""+nextDay(0)+"\""+" INT,"+"\""+nextDay(1)+"\""+" INT,"+"\""+nextDay(2)+"\""+" INT,"+"\""+nextDay(3)+"\""+" INT,"+"\""+nextDay(4)+"\""+" INT, TOTALCLASSES INT, TOTALDAYS INT);"
cmd2=str(cmd);
#print(cmd2)
conn.execute(cmd2)

#conn.execute("CREATE TABLE IF NOT EXISTS AttendanceRegister (ID NUMBER, USN VARCHAR, NAME VARCHAR,"+ str(dayOne) +" INT, DAY2 INT, DAY3 INT, DAY4 INT, DAY5 INT, TOTALCLASSES INT, TOTALDAYS INT);")

def getDate():
    #datetime.date.today().strftime("%d/%m/%y");
    c="1"
    return c;

cursor2 = conn.execute("SELECT * FROM AttendanceRegister;")

names = [description[0] for description in cursor2.description]
cursor2.close()
def update_attendance(id, usn, name, isPresent):

    #print(names[4])
    cursor = conn.execute("SELECT * FROM AttendanceRegister WHERE ID=" + str(id) + ";")

    match = cursor.fetchone()
    cursor.close()
    if match:
        numDays = match[9];
        if isPresent:

            if numDays == 1 and nextDay(1)!=names[4]:
                #if str(nextDay(1)!=str(names[4])):
                    conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + getDate() + ", "+"\""+str(names[5])+"\""+" = -1 , "+"\""+str(names[6])+"\""+" = -1, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8] + 1) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
                    print(name+" is Present")
            elif numDays == 2 and nextDay(1)!=names[5]:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + getDate() + ", "+"\""+str(names[6])+"\""+" = -1, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8] + 1) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
                print(name + " is Present")
            elif numDays == 3 and nextDay(1)!=names[6]:
                print(name + " is Present")
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(match[5]) + ", "+"\""+str(names[6])+"\""+" = " + getDate() + ", "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8] + 1) + ", totalDays =  " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 4 and nextDay(1)!=names[7]:
                print(name + " is Present")
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(match[5]) + ", "+"\""+str(names[6])+"\""+" = " + str(match[6]) + ", "+"\""+str(names[7])+"\""+" = " + getDate()  + ", totalClasses = " + str(match[8] + 1) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
        else:
            if numDays == 1:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(0) + ", "+"\""+str(names[5])+"\""+" = -1 , "+"\""+str(names[6])+"\""+" = -1, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8] ) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 2:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(0) +", "+"\""+str(names[6])+"\""+" = -1, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8]) + ",totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 3:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(match[5]) + ", "+"\""+str(names[6])+"\""+" = " + str(0) + ", "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 4:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(match[5]) + ", "+"\""+str(names[6])+"\""+" = " + str(match[6]) + ", "+"\""+str(names[7])+"\""+" = " + str(0)  + ", totalClasses =" + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")

    else:
        if isPresent:
            conn.execute("INSERT INTO AttendanceRegister VALUES (" +str(id) + ", '" + name + "', " + usn + ",'" + getDate() + "', -1 , -1 , -1, -1 ," + str(1) + ", " + str(1) + " );")
            print(name+" is Present")
        else:
            cursor1 = conn.execute("SELECT * FROM AttendanceRegister ;")
            match = cursor1.fetchone()
            print("match")
            if match:
                 numDays1 = match[9]
                 if numDays1 == 1:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = 0, "+"\""+str(names[5])+"\""+" = -1 , "+"\""+str(names[6])+"\""+" = -1, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                 elif numDays1 == 2:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = 0 , "+"\""+str(names[6])+"\""+" = -1, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                 elif numDays1 == 3:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(match[5]) + " , "+"\""+str(names[6])+"\""+" = 0, "+"\""+str(names[7])+"\""+" = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                 elif numDays1 == 4:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', "+"\""+str(names[3])+"\""+" = " + str(match[3]) + ", "+"\""+str(names[4])+"\""+" = " + str(match[4]) + ", "+"\""+str(names[5])+"\""+" = " + str(match[5]) + " , "+"\""+str(names[6])+"\""+" = " + str(match[5]) + ", "+"\""+str(names[7])+"\""+" = 0 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                #conn.execute("INSERT INTO att_reg VALUES ("+ str(id) + ", '" + usn + "', '" + name + "', " + str(0) + ", -1 , -1 , -1, -1 ," + str(0) + ", " + str( 1) + " );")
            cursor1.close()

    conn.commit()
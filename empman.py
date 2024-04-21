import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "my_database"
)
mycursor=mydb.cursor()

'''mycursor.execute("create table Emp(id int(10)primary key auto_increment, name varchar(120),address varchar(115), mail varchar(125),phone varchar(10),depertment varchar(100))")
print("Table created successfully.")'''


sql = "insert into Emp(id,name,address,mail,phone,depertment) values(%s,%s,%s,%s,%s,%s)"
val = [
    ('',"Mr.Lohar","Rohini","lohar1234@gmail.com","3412870933","sales"),
    ('',"Mr.Tudu","Bankura","tudu4319@gmail.com","42991042210","purches"),
    ('',"Mr.Sujit","Kolkata","sujit4444@gmail.com","9823661180","finance"),
    ('',"Mr.Maitra","Kurseong","maitra7890@gmail.com","1136789943","customarcare"),
    ('',"Mrs.Rai","Hooghly","rai9966@gmail.com","1678003418","accounts"),
    ('',"Mrs.Haldar","Sealdah","haldar1090@gmail.com","3412874419","security"),
    ('',"Mrs.Kar","Medinipur","kar4567@gmail.com","3317870933","electical")
]

'''mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "row/s added successfully.")'''
'''mycursor.execute("select * from Emp")
result = mycursor.fetchall()
for t in result:
    print(t)'''

'''sql = "update Emp set name = %s where name = %s"
val = ("Mr.Lohit", "Mr.Lohar")
mycursor.execute(sql,val)
print(mycursor.rowcount, "row/s affected.")'''

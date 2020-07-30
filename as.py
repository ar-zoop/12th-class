import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost", user="root")
if mycon.is_connected():
    print ("yes")

#This is Server side
# This is the database connection
# Receiving program

from flask import Flask, request

import pymysql

#connecting to db
#db = pymysql.connect(user='Sdipuser', passwd='password', host='localhost', db='MySensor')
db = pymysql.connect(user='Sdipuser', passwd='password', host='localhost', db='Temperature')

cursor = db.cursor()

app = Flask(__name__)


@app.route('/get')
def get():
    TempID = request.args.get('TempID')
    Temp = request.args.get('Temp')
    #Humi = request.args.get('Humi')
    #Status=('Hot')

    
    #cursor.execute("Insert into MySensor.Data(SensorID,Temp,Humi) values (%s,%s,%s)", (SensorID, Temp, Humi))
    #cursor.execute("Insert into Temperature.Readings(TempID,Temp) values (%s,%s)", (TempID, Temp))
    #cursor.execute("Insert into Temperature.Readings(TempID,Temp,Status) values (%s,%s,Hot)", (TempID, Temp, Status))
    cursor.execute("Insert into Temperature.Readings(TempID,Temp,Status) values (%s,%s,Check)", (TempID, Temp))


    db.commit()

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.189')
    #app.run(debug=True, host='172.16.222.101')

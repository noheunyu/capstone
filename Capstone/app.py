from flask import Flask, render_template,request
import pymysql
import time

dbconn = pymysql.connect(
            host = 'Shdmsdb1.mysql.pythonanywhere-services.com',
            port = 3306,
            user = 'Shdmsdb1',
            passwd = '111111aa',
            db = 'Shdmsdb1$ict-diffuser',
            charset = 'utf8'
        )
cursor = dbconn.cursor()


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/iot', methods=["GET","POST"])
def iot():
    if request.method == 'GET':
        pir = request.args.get('pir')
        indate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        temper = request.args.get('temper')
        humidity = request.args.get('humidity')
        d_1 = request.args.get('d_1')
        d_2 = request.args.get('d_2')
        d_3 = request.args.get('d_3')

        sql = "insert into iot set pir = '%s', indate='%s', temper='%s', humidity='%s', d_1='%s', d_2='%s', d_3='%s';" % (pir, indate, temper, humidity, d_1, d_2, d_3)
        cursor.execute(sql)
        dbconn.commit()
    return "ok"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
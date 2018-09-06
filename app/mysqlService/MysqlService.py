import pymysql
from config import *
from app import app

class MysqlService:

    # 用户的增改查
    # 增
    def addUser(self, id, mobile, name):
        sql = "INSERT INTO tb_dm_user(id, mobile, name) \
               VALUES ('%s','%s', '%s')" % \
              (id, mobile, name)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except:
            db.rollback()

    # 判断用户是否已经存在
    def judgeIdExist(self, id):
        sql = "SELECT id from tb_dm_user where id ='%s'" % (id)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            db.close()
            if (results == None):
                return False;
            else:
                return True;
        except:
            db.rollback()

    # 查询用户信息
    def selectUserInfo(self, id):
        dict = {}
        sql = "SELECT name,mobile from tb_dm_user where id = '%s'" % (id)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            myresult = cursor.fetchall()
            for x in myresult:
                dict['name']=x[0]
                dict['mobile']=x[1]
            db.close()
            return dict
        except:
            db.rollback()

    # 签到表的增查
    # 签到，请假
    def sign(self, id, time, section,status,position):
        sql_sign = "INSERT INTO tb_dm_sign(id, time, section,status,position) \
               VALUES ('%s','%s', '%d','%d','%s')" % \
                   (id, time, section,status,position)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql_sign)
            db.commit()
            db.close()
        except:
            db.rollback()

    # 签出
    def sign_out(self, id, time, section, status):
        sql_sign = "UPDATE tb_dm_sign set status='%d' where id='%s' and time='%s' and section='%d' " % \
                   (status, id, time, section)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql_sign)
            db.commit()
            db.close()
        except:
            db.rollback()

    # 查所有签到
    def sign_search(self, id):
        sql = "SELECT * from tb_dm_sign where id ='%s'" % (id)
        list=[]
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                dict = {}
                dict['id'] = x[0]
                dict['time'] = x[1]
                dict['section'] = x[2]
                dict['status'] = x[3]
                dict['position'] = x[4]
                list.append(dict)
            db.close()
            return list
        except:
            db.rollback()

    # 排班表的增删改查
    # 增
    def addSchedule(self, week, section, id, name, position):
        sql = "INSERT INTO tb_dm_schedule(week, section, id, name ,position) \
               VALUES ('%d','%d', '%s','%s','%s')" % \
              (week, section, id, name, position)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except:
            db.rollback()

    # 查某人本周所有的值班
    def querySchedule(self, id):
        list = []
        sql = "SELECT * from tb_dm_schedule where id = '%s' order by week,section"% (id)
        print(sql)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                dict = {}
                dict['week'] = x[0]
                dict['section'] = x[1]
                dict['id'] = x[2]
                dict['name'] = x[3]
                dict['position'] = x[4]
                list.append(dict)
            print(list)
            db.close()
            return list
        except:
            db.rollback()

        # 查某人今天所有的值班
    def queryDaySchedule(self, id,week,day):
        list = []
        sql = "SELECT tb_dm_schedule.* ,status from tb_dm_schedule left join tb_dm_sign on  " \
              "tb_dm_schedule.id =tb_dm_sign.id and  tb_dm_schedule.section =tb_dm_sign.section and tb_dm_sign.time='%s' where tb_dm_schedule.id ='%s' and week='%d' order by tb_dm_schedule.section" % (day,id,week)
        print(sql)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                dict = {}
                dict['week'] = x[0]
                dict['section'] = x[1]
                dict['id'] = x[2]
                dict['name'] = x[3]
                dict['position'] = x[4]
                dict['status'] = x[5]
                list.append(dict)
            print(list)
            db.close()
            return list
        except:
            db.rollback()

    # 查当前时间段值班的信息
    def queryNowSchedule(self, week,section,time):
        list = []
        sql = "SELECT tb_dm_schedule.name ,status from tb_dm_schedule left join tb_dm_sign on  " \
              "tb_dm_schedule.id =tb_dm_sign.id and  tb_dm_schedule.section =tb_dm_sign.section and tb_dm_sign.time='%s' where week='%d' and tb_dm_schedule.section='%d' order by tb_dm_schedule.section" % (time,week,section)
        print(sql)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                dict = {}
                dict['week'] = x[0]
                dict['section'] = x[1]
                dict['id'] = x[2]
                dict['name'] = x[3]
                dict['position'] = x[4]
                dict['status'] = x[5]
                list.append(dict)
            print(list)
            db.close()
            return list
        except:
            db.rollback()

    # 删
    def deleteSchedule(self, week, section, id):
        sql = "DELETE from tb_dm_schedule where id = '%s', week = '%d', section = '%d'" % (id) % (week) % (section)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except:
            db.rollback()

    # 改
    def updateSchedule(self, week, section, new_id, old_id):
        sql = "UPDATE tb_dm_schedule set id = '%s' where week = '%d', section = '%d' id='%s'" % (new_id) % (week) % (
            section) % (old_id)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except:
            db.rollback()

    #查询联系方式
    def queryContacts(self):
        sql="select * from tb_dm_contact"
        list=[]
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results=cursor.fetchall()
            for x in results:
                dict = {}
                dict['id'] = x[0]
                dict['name'] = x[1]
                dict['mobile'] = x[2]
                list.append(dict)
            db.close()
            return list
        except:
            db.rollback()

    # 添加建议
    def insertSuggestion(self,id, content):
        sql = "INSERT INTO tb_dm_suggestion(id, content) \
                       VALUES ('%s','%s')" % \
              (id, content)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
        except:
            db.rollback()
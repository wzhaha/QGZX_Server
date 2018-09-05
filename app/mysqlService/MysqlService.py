import pymysql
from config import *


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
        dict = set()
        sql = "SELECT * from tb_dm_user where id = '%s'" % (id)
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            myresult = cursor.fetchall()
            for x in myresult:
                dict.add(x)
            db.close()
            return dict
        except:
            db.rollback()

    # 签到表的增查
    # 增
    def sign(self, id, time, section):
        sql_sign = "INSERT INTO tb_dm_sign(id, time, section) \
               VALUES ('%s','%s', '%d')" % \
                   (id, time, section)
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
        try:
            db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            db.close()
            return results
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

    # 查
    def querySchedule(self, id):
        list = []
        sql = "SELECT * from tb_dm_schedule where id = '%s'" % (id)
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
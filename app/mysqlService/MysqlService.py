import pymysql
from config import *

class MysqlService:
    db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
    cursor = db.cursor()
#用户的增改查
    #增
    def addUser(self, id, mobile, name):
        sql = "INSERT INTO tb_dm_user(id, mobile, name) \
               VALUES ('%s','%s', '%s')" % \
              (id, mobile, name)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    #判断用户是否已经存在
    def judgeIdExist(self, id):
        sql = "SELECT id from tb_dm_user where id ='%s'" % (id)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if(results==None):
                return False;
            else:
                return True;
        except:
            self.db.rollback()
    #查询用户信息
    def selectUserInfo(self, id):
        dict=set()
        sql = "SELECT * from tb_dm_user where id = '%s'" % (id)
        try:
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            for x in myresult:
                dict.add(x)
            return dict
        except:
            self.db.rollback()

#签到表的增查
    #增
    def sign(self, id, time, section):
        sql_sign = "INSERT INTO tb_dm_sign(id, time, section) \
               VALUES ('%s','%s', '%d')" % \
              (id, time, section)
        try:
            self.cursor.execute(sql_sign)
            self.db.commit()
        except:
            self.db.rollback()


    #查所有签到
    def sign_search(self, id):
        sql = "SELECT * from tb_dm_sign where id ='%s'" % (id)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return  results
        except:
            self.db.rollback()


#排班表的增删改查
    #增
    def addSchedule(self, week, section, id):
        sql = "INSERT INTO tb_dm_schedule(week, section, id) \
               VALUES ('%d','%d', '%s')" % \
              (week, section, id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    #查
    def querySchedule(self, week, section, id):
        sql = "SELECT * from tb_dm_schedule where id = '%s'," % (id)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            self.db.rollback()
    #删
    def deleteSchedule(self, week, section, id):
        sql = "DELETE from tb_dm_schedule where id = '%s', week = '%d', section = '%d'" % (id) %(week) %(section)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    #改
    def updateSchedule(self, week, section, new_id,old_id):
        sql = "UPDATE tb_dm_schedule set id = '%s' where week = '%d', section = '%d' id='%s'" % (new_id) % (week) % (section) %(old_id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

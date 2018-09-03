import pymysql
from config import *


class MysqlService:
    db = pymysql.connect(MYSQL_URL, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
    cursor = db.cursor()

    def addUser(self, id, mobile, name):
        sql = "INSERT INTO tb_dm_user(id, mobile, name) \
               VALUES ('%s','%s', '%s')" % \
              (id, mobile, name)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

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



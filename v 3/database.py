import pymysql.cursors
import mysql.connector

class Database:
    def __init__(self, host, user, password, database):

        self.connection = pymysql.connect(host=host, user=user, 
                                          password=password, database=database)



    def create_user(self, email, password):
        """Добавляет пользователя и возвращает id созданной записи."""
        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (email, password))
            self.connection.commit()
            return cursor.lastrowid

    def insert_users(self, email, password):
        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (email, password))
            self.connection.commit()

    def select_users(self, login, password):
            cursor = self.connection.cursor()
            sql = "SELECT * FROM users WHERE email = %s and password = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (login, password))
                user = cursor.fetchone()
                return user

    def get_user_by_email(self, email):
        sql = "SELECT id FROM users WHERE email = %s"

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (email,))
            return cursor.fetchone()

    # def insert_classes(self, places1, places2):
    #     cursor = self.connection.cursor()
    #     sql = "INSERT INTO classes (class_name, places) VALUES (%s, %s)"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(sql, (places1, places2))
    #         self.connection.commit()


    # def select_classes(self):
    #     cursor = self.connection.cursor()
    #     sql = "SELECT * FROM classes"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(sql)
    #         classes = cursor.fetchall()
    #         for row in classes:
    #             print(row)

    

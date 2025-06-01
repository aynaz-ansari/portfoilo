import mysql.connector

class Database():
    def __init__(self):
        self.connector=mysql.connector.connect(host="localhost",user="root",password="aynaz7989!",database="products")
        self.cursor=self.connector.cursor()

    def add_product(self,ca,b,m,co,p,w,tp):
        self.cursor.execute(f"INSERT INTO electronic_products (category,brand,model,color,price,warranty,total_price) VALUES ('{ca}','{b}','{m}','{co}',{p},{w},{tp}) ")
        self.connector.commit()
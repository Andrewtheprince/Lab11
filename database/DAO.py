from database.DB_connect import DBConnect
from model.product import Prodotto


class DAO:

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """SELECT p.Product_color FROM go_products p group by p.Product_color order by p.Product_color asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProdotti(colore):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT *
                   FROM go_products p
                   WHERE p.Product_color = %s"""
        cursor.execute(query, (colore,))
        for row in cursor:
            result.append(Prodotto(**row))
        cursor.close()
        conn.close()
        return result

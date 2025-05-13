from database.DB_connect import DBConnect
from model.product import Prodotto


class DAO:

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT p.Product_color 
                    FROM go_products p 
                    group by p.Product_color 
                    order by p.Product_color asc"""
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

    @staticmethod
    def getVendite(anno, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select gds.Product_number as p1, gds2.Product_number as p2
                    from go_daily_sales gds, go_daily_sales gds2
                    where gds.Retailer_code = gds2.Retailer_code and gds.Date = gds2.Date and YEAR(gds.Date) = %s and gds.Product_number != gds2.Product_number
                    group by gds.Product_number, gds2.Product_number, gds.Date"""
        cursor.execute(query, (anno,))
        for row in cursor:
            if row["p1"] in idMap and row["p2"] in idMap:
                result.append(row)
        cursor.close()
        conn.close()
        return result

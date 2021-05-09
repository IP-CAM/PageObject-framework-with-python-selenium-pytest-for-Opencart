import mariadb


class MariaDb:
    def __init__(self):
        self.maria_db = mariadb.connect(host='localhost',
                                        user='bn_opencart',
                                        password='',
                                        port=3306,
                                        database='bitnami_opencart'

                                        )
        self.cursor = self.maria_db.cursor()

    def delete_customer(self, email):
        self.cursor.execute("DELETE FROM oc_customer WHERE email=?", (email, ))
        print("Customer is successfully deleted!")

    def delete_product(self, product_id):
        pass

    def close_connection(self):
        self.maria_db.close()
        print("Connection with database is closed!")

# del_customer = MariaDb()
# del_customer.delete_customer()
# del_customer.close_connetcion()

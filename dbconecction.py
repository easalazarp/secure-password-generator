import sqlite3



class DBConection:
    DB_NAME = "secure_password_db.db"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    connection = sqlite3.connect(DB_NAME)
    def __init__(self):
        self.create_db()

    # Conectar a la base de datos (o crearla si no existe)
    def create_db(self):

        try:
            cursor = self.connection.cursor()
            # Crear una tabla (si no existe)
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS password_references (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        reference TEXT,
                        password TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as error:
            print(f"{self.RED}Error al conectar a la base de datos: {error}{self.RESET}")


    @staticmethod
    def save_password(name, reference, password):
        try:
            cursor = DBConection.connection.cursor()
            # Insertar datos en la tabla
            cursor.execute("INSERT INTO password_references (name, reference, password) VALUES (?, ?, ?)", (name, reference, password))
            # Guardar los cambios
            DBConection.connection.commit()
            print("---------------------------------------")
            print(f"{DBConection.GREEN}**** Datos guardados correctamente ****{DBConection.RESET}")
            print("---------------------------------------")
        except sqlite3.Error as error:
            print(f"{DBConection.RED}Error al guardar a la base de datos: {error}{DBConection.RESET}")
        # finally:
        #     if DBConection.connection:
        #         DBConection.connection.close()
    @staticmethod
    def get_password():
        try:
            cursor = DBConection.connection.cursor()
            cursor.execute("SELECT * FROM password_references")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print(f"{DBConection.RED}Error al obtener los registros de la base de datos: {error}{DBConection.RESET}")
        # finally:
        #     if DBConection.connection:
        #         DBConection.connection.close()

    @staticmethod
    def update_name_and_reference(id_reference, name, reference):
        try:
            cursor = DBConection.connection.cursor()
            cursor.execute("UPDATE password_references SET name = ?, reference = ? WHERE id = ?", (name, reference, id_reference))
            DBConection.connection.commit()
            print("---------------------------------------")
            print(f"{DBConection.GREEN}**** Datos modificados correctamente ****{DBConection.RESET}")
            print("---------------------------------------")
        except sqlite3.Error as error:
            print(f"{DBConection.RED}Error al modificar los registros de la base de datos: {error}{DBConection.RESET}")
        # finally:
        #     if DBConection.connection:
        #         DBConection.connection.close()

    @staticmethod
    def register_delete(id_reference):
        try:
            cursor = DBConection.connection.cursor()
            cursor.execute("DELETE FROM password_references WHERE id = ?", (id_reference,))
            DBConection.connection.commit()
            print("---------------------------------------")
            print(f"{DBConection.GREEN}**** Datos eliminados correctamente ****{DBConection.RESET}")
            print("---------------------------------------")
        except sqlite3.Error as error:
            print(f"{DBConection.RED}Error al eliminar los registros de la base de datos: {error}{DBConection.RESET}")
        # finally:
        #     if DBConection.connection:
        #         DBConection.connection.close()
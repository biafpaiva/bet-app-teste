import sqlite3

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontuacao = 0
        self.apostas = []

    def register_user(self):

        username = self.nome
        email = self.email
        password = self.senha

        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()

        return msg


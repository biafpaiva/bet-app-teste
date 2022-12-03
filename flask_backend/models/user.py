import sqlite3
from flask_backend import dbFilePath

class User:
    def __init__(self, nome, email, senha, image):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontuacao = 0
        self.apostas = []
        self.image = image

    def register_user(self):
        with sqlite3.connect(dbFilePath) as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO users (username, email, password, image) VALUES (?, ?, ?, ?)', (self.nome, self.email, self.senha, self.image))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()

        return msg



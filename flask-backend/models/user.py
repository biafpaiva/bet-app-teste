from flask import session
import sqlite3
from services.utils import getImage

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontuacao = 0
        self.apostas = []

    def register_user(self):
        with sqlite3.connect('database/database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO users (username, email, password, image) VALUES (?, ?, ?, ?)', (self.nome, self.email, self.senha, getImage()))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()

        return msg



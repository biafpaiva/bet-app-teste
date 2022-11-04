from match import Match
from user import Usuario
import pandas as pd

df = pd.read_json("data/jogos-1.json")

matches = Match.from_df_to_obj(df)

user_1 = Usuario('Bia', 'bia@gmail.com', '123')
user_2 = Usuario('Ilana', 'bia@gmail.com', '123')

Usuario.salvar_usuario(user_1)
Usuario.autenticar_usario(user_1)
Usuario.autenticar_usario(user_2)

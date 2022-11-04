class Match:
    def __init__(self, id, grupo, rodada, diaSemana, data, hora, estadio, partida, mandante, visitante):
        self.id = id
        self.grupo = grupo
        self.rodada = rodada
        self.diaSemana = diaSemana
        self.data = data
        self.hora = hora
        self.estadio = estadio
        self.partida = partida
        self.mandante = mandante
        self.visitante = visitante

    def from_df_to_obj(df):
        matches = []
        for i in range(len(df)):
            matches.append(Match(df['id'][i], df['grupo'][i], df['rodada'][i],
                                 df['diaSemana'][i], df['data'][i], df['hora'][i],
                                 df['estadio'][i], df['partida'][i], df['mandante'][i], df['visitante'][i]))
        return matches
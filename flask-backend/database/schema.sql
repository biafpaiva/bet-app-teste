DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL unique ,
    password TEXT NOT NULL,
    score FLOAT,
    logged INTEGER
);

DROP TABLE IF EXISTS matches;

CREATE TABLE matches (
    id_ INTEGER,
    group_ TEXT NOT NULL,
    round INTEGER,
    day_of_week TEXT NOT NULL,
    date_ TEXT NOT NULL,
    time_ TEXT NOT NULL,
    stadium TEXT NOT NULL,
    teams TEXT NOT NULL,
    home TEXT NOT NULL,
    visitor TEXT NOT NULL,
    final_score_home INTEGER,
    final_score_visitor INTEGER,
    is_over INTEGER,
    winner TEXT
);

DROP TABLE IF EXISTS bets;

CREATE TABLE bets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_score INTEGER,
    visitor_score INTEGER,
    id_game INTEGER,
    email TEXT INTEGER,
    winner TEXT,
    score INTEGER,
    CONSTRAINT only_ unique (id_game,email)
);
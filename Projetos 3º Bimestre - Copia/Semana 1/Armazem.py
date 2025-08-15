import sqlite3

conn = sqlite3.connect("armazem.db")
cursor = conn.cursor()


cursor.execute ("""
CREATE TABLE IF NOT EXISTS armazem (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nome TEXT NOT NULL,
   quantidade INTEGER NOT NULL,
   consumo INTEGER NOT NULL,
   producao INTEGER NOT NULL
)
""")
conn.commit()

dados = [
 ('Grao', 120, 24, 0),
 ('Madeira', 20, 5, 0),
 ('Erva',  30, 2, 2),
 ('Ferro', 70, 10, 30),
]


cursor.executemany("INSERT INTO armazem (nome, quantidade, consumo, producao) VALUES (?, ?, ?, ?)", dados)
conn.commit()

cursor.execute("SELECT nome, quantidade, consumo, producao FROM armazem")
resultados = cursor.fetchall()


print("Recursos da vila:")


recursos_resultado = []


for nome, quantidade, consumo, producao in resultados:
   saldo_diario = producao - consumo


   if saldo_diario == 0:
       duracao = 0
   else:
       duracao = round(quantidade / abs(saldo_diario), 2)


   recursos_resultado.append((nome, quantidade, consumo, producao, duracao))


for nome, quantidade, consumo, producao, duracao in recursos_resultado:
   print(f"{nome}: Quantidade {quantidade}, Consumo Diario {consumo}, Produção {producao}, Duração: {duracao} dias")

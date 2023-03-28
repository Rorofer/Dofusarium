import sqlite3
import prettytable

def create_db_all_dd():

    # établir une connexion à la base de données
    conn = sqlite3.connect('DD.db')

    # créer une table si elle n'existe pas déjà
    conn.execute('''
        CREATE TABLE IF NOT EXISTS DD(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Generation INT,
            Type VARCHAR(20),
            Parent1 VARCHAR(20),
            Parent2 VARCHAR(20),
            Parchemins VARCHAR(20)
            );
    ''')

    # Vérification si les données sont déjà présentes dans la table
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM DD")
    result = cur.fetchone()[0]

    if result == 0:
        tuples = [
            (1,'Rousse','Rousse','Rousse','Doré'),
            (1,'Amande','Amande','Amande','Doré'),
            (1,'Dorée','Dorée','Dorée','Doré'),
            (2,'Rousse Amande','Rousse','Amande','Petit Vitalité'),
            (2,'Rousse Dorée','Rousse','Dorée','Petit Sagesse'),
            (2,'Amande Dorée','Amande','Dorée','Petit Sagesse'),
            (3,'Indigo','Rousse Amande','Amande Dorée','Petit Chance'),
            (3,'Ebène','Rousse Dorée','Amande Dorée','Petit Agilité'),
            (4,'Rousse Indigo','Rousse','Indigo','Petit Vitalité'),
            (4,'Rousse Ebène','Rousse','Ebène','Petit Vitalité'),
            (4,'Amande Indigo','Amande','Indigo','Petit Chance'),
            (4,'Amande Ebène','Amande','Ebène','Petit Agilité'),
            (4,'Dorée Indigo','Dorée','Indigo','Petit Sagesse'),
            (4,'Dorée Ebène','Dorée','Ebène','Petit Sagesse'),
            (4,'Indigo Ebène','Indigo','Ebène','Petit Chance'),
            (5,'Pourpre','Rousse Amande','Indigo Ebène','Petit Force'),
            (5,'Orchidée','Rousse Dorée','Indigo Ebène','Petit Intelligence'),
            (6,'Pourpre Rousse','Pourpre','Rousse','Moyen Force'),
            (6,'Orchidée Rousse','Orchidée','Rousse','Moyen Intelligence'),
            (6,'Amande Pourpre','Amande','Pourpre','Moyen Force'),
            (6,'Amande Orchidée','Amande','Orchidée','Moyen Vitalité'),
            (6,'Dorée Pourpre','Dorée','Pourpre','Moyen Sagesse'),
            (6,'Dorée Orchidée','Dorée','Orchidée','Moyen Sagesse'),
            (6,'Indigo Pourpre','Indigo','Pourpre','Moyen Chance'),
            (6,'Indigo Orchidée','Indigo','Orchidée','Moyen Chance'),
            (6,'Ebène Pourpre','Ebène','Pourpre','Moyen Agilité'),
            (6,'Ebène Orchidée','Ebène','Orchidée','Moyen Agilité'),
            (6,'Pourpre Orchidée','Pourpre','Orchidée','Moyen Intelligence'),
            (7,'Ivoire','Indigo Pourpre','Pourpre Orchidée','Grand Chance'),
            (7,'Turquoise','Ebène Orchidée','Pourpre Orchidée','Grand Agilité'),
            (8,'Ivoire Rousse','Ivoire','Rousse','Grand Vitalité'),
            (8,'Turquoise Rousse','Turquoise','Rousse','Grand Vitalité'),
            (8,'Amande Ivoire','Amande','Ivoire','Grand Chance'),
            (8,'Amande Turquoise','Amande','Turquoise','Grand Vitalité'),
            (8,'Dorée Ivoire','Dorée','Ivoire','Grand Sagesse'),
            (8,'Dorée Turquoise','Dorée','Turquoise','Grand Sagesse'),
            (8,'Indigo Ivoire','Indigo','Ivoire','Grand Chance'),
            (8,'Indigo Turquoise','Indigo','Turquoise','Grand Chance'),
            (8,'Ebène Ivoire','Ebène','Ivoire','Grand Agilité'),
            (8,'Ebène Turquoise','Ebène','Turquoise','Grand Agilité'),
            (8,'Pourpre Ivoire','Pourpre','Ivoire','Grand Force'),
            (8,'Turquoise Pourpre','Turquoise','Pourpre','Grand Force'),
            (8,'Ivoire Orchidée','Ivoire','Orchidée','Grand Intelligence'),
            (8,'Turquoise Orchidée','Turquoise','Orchidée','Grand Intelligence'),
            (8,'Ivoire Turquoise','Ivoire','Turquoise','Grand Agilité'),
            (9,'Emeraude','Pourpre Ivoire','Ivoire Turquoise','Puissant Force'),
            (9,'Prune','Orchidée Turquoise','Ivoire Turquoise','Puissant Intelligence'),
            (10,'Rousse Emeraude','Rousse ','Emeraude','Puissant Vitalité'),
            (10,'Rousse Prune','Rousse ','Prune','Puissant Vitalité'),
            (10,'Amande Emeraude','Amande','Emeraude','Puissant Vitalité'),
            (10,'Amande Prune','Amande','Prune','Puissant Vitalité'),
            (10,'Dorée Emeraude','Dorée','Emeraude','Puissant Sagesse'),
            (10,'Dorée Prune','Dorée','Prune','Puissant Sagesse'),
            (10,'Indigo Emeraude','Indigo','Emeraude','Puissant Chance'),
            (10,'Indigo Prune','Indigo','Prune','Puissant Chance'),
            (10,'Ebène Emeraude','Ebène','Emeraude','Puissant Force'),
            (10,'Ebène Prune','Ebène','Prune','Puissant Agilité'),
            (10,'Pourpre Emeraude','Pourpre','Emeraude','Puissant Force'),
            (10,'Pourpre Prune','Pourpre','Prune','Puissant Force'),
            (10,'Orchidée Emeraude','Orchidée','Emeraude','Puissant Intelligence'),
            (10,'Orchidée Prune','Orchidée','Prune','Puissant Intelligence'),
            (10,'Ivoire Emeraude','Ivoire','Emeraude','Puissant Chance'),
            (10,'Ivoire Prune','Ivoire','Prune','Puissant Chance'),
            (10,'Turquoise Emeraude','Turquoise','Emeraude','Puissant Agilité'),
            (10,'Turquoise Prune','Turquoise','Prune','Puissant Agilité'),
            (10,'Emeraude Prune','Emeraude','Prune','Puissant Intelligence'),
        ]

        # Insertion des tuples dans la table
        conn.executemany("INSERT INTO DD (Generation, Type, Parent1, Parent2, Parchemins) VALUES (?, ?, ?, ?, ?)", tuples)

    # Validation de la transaction
    conn.commit()

    # Fermeture de la connexion
    conn.close()


# ------ Afficher toutes les DD du jeu ------
def afficher_all_DD_console (input):
    tri = input
    create_db_all_dd()
    conn = sqlite3.connect('DD.db')
    
    # exécuter une requête SQL pour lister le contenu de la table
    if tri == '1' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY ID')
    elif tri == '2' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY ID DESC')
    elif tri == '3' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Type')
    elif tri == '4' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Type DESC')
    elif tri == '5' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Parent1')
    elif tri == '6' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Parent1 DESC')
    elif tri == '7' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Parent2')
    elif tri == '8' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Parent2 DESC')
    elif tri == '9' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Parchemins')
    elif tri == '10' :
        cursor = conn.execute('SELECT * FROM DD ORDER BY Parchemins DESC')
    

    # créer un tableau avec les noms de colonnes
    table = prettytable.PrettyTable(['ID', 'Génération', 'Type de DD', 'Parent 1', 'Parent 2','Type de parchemin donné'])
    # ajouter chaque tuple de la table au tableau
    for row in cursor:
        table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])
    # afficher le tableau
    print(table)
# ------  ------



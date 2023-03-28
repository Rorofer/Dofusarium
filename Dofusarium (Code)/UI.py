import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QMessageBox, QDialog, QInputDialog, QTableWidget, QTableWidgetItem
from Dofusarium import achat_date_prix
from Dragodindes import afficher_all_DD_console
import sqlite3

class MonInterfaceUtilisateur(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'TableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        # Titre
        titre = QLabel("Mon Application")

        # Boutons
        bouton_achat = QPushButton("Ajouter un achat")
        bouton_rentabilite = QPushButton("Calculer la rentabilité")
        bouton_afficher = QPushButton("Afficher toutes les dragodindes")

        # Connexion des boutons à des fonctions
        bouton_achat.clicked.connect(self.achat)
        bouton_afficher.clicked.connect(self.afficher)

        # Création de l'instance de la classe Rentabilite
        self.rentabilite_dialog = Rentabilite()
        bouton_rentabilite.clicked.connect(self.rentabilite_dialog.show)

        # Mise en page
        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()

        layout_horizontal.addWidget(bouton_achat)
        layout_horizontal.addWidget(bouton_rentabilite)
        layout_horizontal.addWidget(bouton_afficher)

        layout_vertical.addWidget(titre)
        layout_vertical.addLayout(layout_horizontal)

        self.setLayout(layout_vertical)
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle("Mon Application")
        self.show()

    @staticmethod
    def afficher():
        table_widget = TableWidget()
        table_widget.show()


    
    def achat(self):
        # Création d'une boîte de dialogue pour saisir les informations sur l'achat
        dialogue = QDialog(self)
        dialogue.setWindowTitle("Ajouter un achat")

        # Zone de texte pour la date de l'achat
        label_date = QLabel("Date de l'achat (jj/mm/aaaa) : ")
        champ_date = QLineEdit()
        layout_date = QHBoxLayout()
        layout_date.addWidget(label_date)
        layout_date.addWidget(champ_date)

        # Zone de texte pour le prix d'achat
        label_prix = QLabel("Prix d'achat (en kamas) : ")
        champ_prix = QLineEdit()
        layout_prix = QHBoxLayout()
        layout_prix.addWidget(label_prix)
        layout_prix.addWidget(champ_prix)

        # Boutons OK et Annuler
        bouton_ok = QPushButton("OK")
        bouton_annuler = QPushButton("Annuler")
        layout_boutons = QHBoxLayout()
        layout_boutons.addWidget(bouton_ok)
        layout_boutons.addWidget(bouton_annuler)

        # Mise en page de la boîte de dialogue
        layout_vert = QVBoxLayout()
        layout_vert.addLayout(layout_date)
        layout_vert.addLayout(layout_prix)
        layout_vert.addLayout(layout_boutons)
        dialogue.setLayout(layout_vert)

        # Connexion des boutons OK et Annuler
        bouton_ok.clicked.connect(dialogue.accept)
        bouton_annuler.clicked.connect(dialogue.reject)

        # Affichage de la boîte de dialogue et récupération des informations saisies si OK est cliqué
        if dialogue.exec_() == QDialog.Accepted:
            date_achat = champ_date.text()
            prix_achat = float(champ_prix.text())

            # Appel de la fonction d'ajout d'achat
            achat_date_prix(date_achat, prix_achat)


class Rentabilite(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcul de rentabilité")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label_item = QLabel("Nom de l'item (au minimum un caractère) : ")
        self.layout.addWidget(self.label_item)
        self.item_input = QLineEdit()
        self.layout.addWidget(self.item_input)
        self.label_ressources = QLabel("Nombre de ressources utilisées : ")
        self.layout.addWidget(self.label_ressources)
        self.ressources_input = QLineEdit()
        self.layout.addWidget(self.ressources_input)
        self.btn_calculer = QPushButton("Calculer rentabilité")
        self.layout.addWidget(self.btn_calculer)
        self.label_resultat = QLabel()
        self.layout.addWidget(self.label_resultat)
        self.btn_calculer.clicked.connect(self.calculer_rentabilite)

    def calculer_rentabilite(self):
        self.label_resultat.setText("\n" + "-" * 40 + "\n")
        
        nom_item, ok = QInputDialog.getText(self, "Nom de l'item", "Nom de l'item (au minimum un caractère) : ")
        if not ok or len(nom_item.strip()) == 0:
            self.label_resultat.setText("Veuillez entrer un nom d'item valide.")
            return
            
        nb_ressources = 0
        while nb_ressources <= 0:
            nb_ressources, ok = QInputDialog.getInt(self, "Nombre de ressources", "Nombre de ressources utilisées : ")
            if not ok or nb_ressources <= 0:
                self.label_resultat.setText("Veuillez entrer une valeur supérieure à 0.")
                nb_ressources = 0
                
        ressources = {}
        for i in range(nb_ressources):
            nom_ressource, ok = QInputDialog.getText(self, f"Nom de la ressource {i+1}", f"Nom de la ressource {i+1} :")
            if not ok or len(nom_ressource.strip()) == 0:
                self.label_resultat.setText("Veuillez entrer un nom de ressource valide.")
                return

            prix_unitaire = 0
            while prix_unitaire <= 0:
                prix_unitaire, ok = QInputDialog.getDouble(self, "Prix unitaire de la ressource", "Prix unitaire de la ressource : ")
                if not ok or prix_unitaire <= 0:
                    self.label_resultat.setText("Veuillez entrer une valeur supérieure à 0.")
            
            quantite_utilisee = 0
            while quantite_utilisee <= 0:
                quantite_utilisee, ok = QInputDialog.getInt(self, "Quantité utilisée de la ressource", "Quantité utilisée de la ressource : ")
                if not ok or quantite_utilisee <= 0:
                    self.label_resultat.setText("Veuillez entrer une valeur supérieure à 0.")
            
            ressources[nom_ressource] = (prix_unitaire, quantite_utilisee)

        prix_craft = sum([qte * prix_unitaire for prix_unitaire, qte in ressources.values()])
        
        prix_vente, ok = QInputDialog.getDouble(self, "Prix de revente de l'item", "Prix de revente de l'item")
        if not ok or prix_vente <= 0:
            self.label_resultat.setText("Veuillez entrer une valeur supérieure à 0.")
            return

        prix_final = prix_vente - (prix_vente * 0.02) - prix_craft

        self.label_resultat.setText(f"La rentabilité de l'item {nom_item} est de {prix_final:.2f} kamas.")
        
        try:
            with open("craft.txt", "a") as f:
                f.write("\n"+"-" * 40 + "\n")
                f.write(f"La rentabilité de l'item {nom_item} est de {prix_final:.2f} kamas.")
        except OSError as e:
            self.label_resultat.setText(f"Une erreur s'est produite lors de l'écriture dans le fichier : {e}")

class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'TableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def createTable(self):
        
        
        # établir une connexion à la base de données
        conn = sqlite3.connect('DD.db')

        # Créer un curseur
        cur = conn.cursor()

        # Récupérer les données de la table DD
        cur.execute("SELECT * FROM DD")
        rows = cur.fetchall()

        # Compter le nombre de colonnes de la table
        cur.execute("PRAGMA table_info(DD)")
        col_count = len(cur.fetchall())

        # Créer un tableau de la taille de la table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(col_count)
        
        # Insérer les données dans le tableau
        for i, row in enumerate(rows):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
        
        # Nommer les colonnes
        cur.execute("PRAGMA table_info(DD)")
        headers = [header[1] for header in cur.fetchall()]
        self.tableWidget.setHorizontalHeaderLabels(headers)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mon_ui = MonInterfaceUtilisateur()
    mon_ui.show()
    sys.exit(app.exec_())
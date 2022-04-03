import sys
from PyQt5 import QtWidgets
import sqlite3

class pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.baglantı_olustur()
        self.init_ui()

    def baglantı_olustur(self):

        baglanti=sqlite3.connect("database.db")

        self.cursor=baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler(kullanıcı_adı TEXT, parola TEXT)")
        baglanti.commit()


    def init_ui(self):

        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("GİRİŞ YAP")
        self.yazi_alani=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.giris)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.setGeometry(750,250,500,500)
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):
        ad=self.kullanici_adi.text()
        par=self.parola.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı=? and parola=?",(ad,par))
        data=self.cursor.fetchall()

        if len(data)==0:
            self.yazi_alani.setText("Böyle Bir Kullanıcı Yoktur!\n Lütfen Girdiğiniz Değerleri Kontrol ediniz")
        else:
            self.yazi_alani.setText("Hoşgeldiniz  "+ad)

app=QtWidgets.QApplication(sys.argv)
a=pencere()
sys.exit(app.exec_())


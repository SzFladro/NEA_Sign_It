import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

#importing UI
from DataBase import config, Account, WordClass
from src.ui_SignItInterface import *
from Interface import CatalogueInterface

# IMPORT Custom widgets
from Custom_Widgets import *

from Custom_Widgets.QAppSettings import QAppSettings


config_user = config.Config()
Words = WordClass.Word
Words.add_wordfromDB()
CatInterface = CatalogueInterface.InterfaceCatalogue

########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        CatInterface.set_ui(self.ui)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################

        loadJsonStyle(self, self.ui, jsonFiles = {"json-styles\dashboard_style.json"
        })
        ########################################################################


        QAppSettings.updateAppSettings(self)
        ########################################################################
        self.setWindowTitle("SignIt")
        self.show()
        self.showMaximized() 
        self.ui.MainWidget.setCurrentWidget(self.ui.Dashboard)
        self.populate_comboboxes()
        self.get_wordsbasedonsearch(None)

        #event listeners
        self.ui.HomeButton.clicked.connect(self.ui.MainWidget.setCurrentWidget(self.ui.Dashboard))
        self.ui.TranslatorButton.clicked.connect(lambda: self.show_TranslationMenu())
        self.ui.ProfileButton.clicked.connect(lambda: self.show_accountMenu())
        self.ui.SettingsButton.clicked.connect(lambda: self.show_settingsMenu())
        self.ui.CatalogueSearchBar.textChanged.connect(self.get_wordsbasedonsearch)
        self.ui.CatalogueCategoryselector.currentIndexChanged.connect(lambda: self.get_wordsbasedonsearch(None))


    def populate_comboboxes(self):
        Worditems4combobox = Words.get_categories()
        self.ui.CatalogueCategoryselector.addItems(Worditems4combobox)
        return None

    def show_TranslationMenu(self):
        print("Translator")
 
    def get_wordsbasedonsearch(self,searchword):
        search_category = self.ui.CatalogueCategoryselector.currentText()
        if(search_category == "All"):
            results = Words.search(word_name= searchword)
        else:
            results = Words.search(word_name= searchword, category= search_category)
        CatInterface.set_ui(self.ui)
        CatInterface.frame_creator(self,results)

    def show_accountMenu(self):
        self.ui.ExpandableSideMenu.expandMenu()
        self.ui.Sidemenulabel.setText("Account")
        user_name = config_user.get_username()
        if user_name == None:
            self.ui.OptionsWidget.setCurrentWidget(self.ui.Account_pg)
            self.ui.Login_Button.clicked.connect(lambda: self.loguserin())
            self.ui.SignUpbutton.clicked.connect(lambda: self.signupuser())
            self.ui.PassSignupEdit.textChanged.connect(self.update_passwordstrength)
        else:
            self.ui.OptionsWidget.setCurrentWidget(self.ui.LoggedInPage)
            self.ui.usernameLoggedinlabel.setText(f"Logged in as {user_name}")
            self.ui.LogoutButton.clicked.connect(lambda: self.logoutuser())

    def show_settingsMenu(self):
        self.ui.ExpandableSideMenu.expandMenu()
        self.ui.Sidemenulabel.setText("Settings")
        self.ui.OptionsWidget.setCurrentWidget(self.ui.SettingsPage)

    def loguserin(self):
        username = self.ui.UsernameLoginEdit.text()
        password = self.ui.PassLoginEdit.text()
        msg = Account.Login(username,password)
        self.ui.OptionsWidget.setCurrentWidget(self.ui.LoggedInPage)

    def logoutuser(self):
        config_user.set_username(None)
        self.ui.OptionsWidget.setCurrentWidget(self.ui.Account_pg)

    
    def signupuser(self):
        username = self.ui.UsernameSignupEdit.text()
        password = self.ui.PassSignupEdit.text()
        confirm_Password = self.ui.ConfirmPassEdit.text()
        if password == confirm_Password:
            if self.ui.Strengthmeter.value()>50:
                Account.create_User(username,password)
            else:
                print("Password isn't Strong enough")

        else:
            print("passwords don't match")

    def update_passwordstrength(self,password):
        score, rating = Account.password_strength(password)
        self.ui.Strengthmeter.setValue(score*25)
        self.ui.Strengthmeter.setFormat(f"Strength: {rating}")

        
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
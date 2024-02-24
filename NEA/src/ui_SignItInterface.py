# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_SignItInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLayout, QLineEdit, QMainWindow,
    QProgressBar, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.Theme import (QLabelThemed, QPushButtonThemed)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 545)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"\n"
"#Main_body{\n"
"	background-color: rgb(54, 69, 79);\n"
"}\n"
"\n"
"#LeftMenu{\n"
"	background-color: rgb(79, 64, 54);\n"
"}\n"
"\n"
"#LeftMenu QPushButton {\n"
"    text-align: left;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    border-color:  rgb(79, 64, 54);\n"
"    font: bold 14px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"#ExpandableSideMenu{\n"
"	background-color: rgb(75, 95, 109);\n"
"}\n"
"#AccountPanel{\n"
"	background-color: rgb(54, 69, 79);\n"
"}\n"
"#ExpandableSideMenu QPushButton {\n"
"    text-align: centre;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    border-color:   rgb(54, 69, 79);\n"
"  "
                        "  font: bold 14px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QLineEdit{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"    border-color:   rgb(54, 69, 79);\n"
"    font: bold 14px;\n"
"    padding: 5px 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenu = QCustomSlideMenu(self.centralwidget)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.horizontalLayout_2 = QHBoxLayout(self.LeftMenu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.LeftSideBar = QWidget(self.LeftMenu)
        self.LeftSideBar.setObjectName(u"LeftSideBar")
        self.verticalLayout = QVBoxLayout(self.LeftSideBar)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 0, -1)
        self.LeftMenuFrame = QFrame(self.LeftSideBar)
        self.LeftMenuFrame.setObjectName(u"LeftMenuFrame")
        self.LeftMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 0, 0)
        self.MenuButton = QPushButtonThemed(self.LeftMenuFrame)
        self.MenuButton.setObjectName(u"MenuButton")
        self.MenuButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/png2svg/menu-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/png2svg/menu-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u":/icons/png2svg/menu-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.MenuButton.setIcon(icon)
        self.MenuButton.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.MenuButton)


        self.verticalLayout.addWidget(self.LeftMenuFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.LeftOptionsFrame = QFrame(self.LeftSideBar)
        self.LeftOptionsFrame.setObjectName(u"LeftOptionsFrame")
        self.LeftOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftOptionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.LeftOptionsFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 0, 0, 0)
        self.HomeButton = QPushButtonThemed(self.LeftOptionsFrame)
        self.HomeButton.setObjectName(u"HomeButton")
        self.HomeButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/png2svg/home-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/png2svg/home-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon1.addFile(u":/icons/png2svg/home-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.HomeButton.setIcon(icon1)
        self.HomeButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.HomeButton)

        self.ProfileButton = QPushButtonThemed(self.LeftOptionsFrame)
        self.ProfileButton.setObjectName(u"ProfileButton")
        self.ProfileButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/png2svg/profile-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/png2svg/profile-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon2.addFile(u":/icons/png2svg/profile-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.ProfileButton.setIcon(icon2)
        self.ProfileButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.ProfileButton)

        self.LiveButton = QPushButtonThemed(self.LeftOptionsFrame)
        self.LiveButton.setObjectName(u"LiveButton")
        self.LiveButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/png2svg/camera-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/png2svg/camera-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon3.addFile(u":/icons/png2svg/camera-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.LiveButton.setIcon(icon3)
        self.LiveButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.LiveButton)


        self.verticalLayout.addWidget(self.LeftOptionsFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.LeftSettingsFrame = QFrame(self.LeftSideBar)
        self.LeftSettingsFrame.setObjectName(u"LeftSettingsFrame")
        self.LeftSettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftSettingsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.LeftSettingsFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 2)
        self.SettingsButton = QPushButtonThemed(self.LeftSettingsFrame)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/png2svg/settings-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/png2svg/settings-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon4.addFile(u":/icons/png2svg/settings-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.SettingsButton.setIcon(icon4)
        self.SettingsButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.SettingsButton)

        self.MinimiseButton = QPushButtonThemed(self.LeftSettingsFrame)
        self.MinimiseButton.setObjectName(u"MinimiseButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/png2svg/minimise-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/png2svg/minimise-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon5.addFile(u":/icons/png2svg/minimise-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.MinimiseButton.setIcon(icon5)
        self.MinimiseButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.MinimiseButton)

        self.ExitButton = QPushButtonThemed(self.LeftSettingsFrame)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/png2svg/exit-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/png2svg/exit-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon6.addFile(u":/icons/png2svg/exit-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.ExitButton.setIcon(icon6)
        self.ExitButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.ExitButton)


        self.verticalLayout.addWidget(self.LeftSettingsFrame)


        self.horizontalLayout_2.addWidget(self.LeftSideBar)


        self.horizontalLayout.addWidget(self.LeftMenu)

        self.ExpandableSideMenu = QCustomSlideMenu(self.centralwidget)
        self.ExpandableSideMenu.setObjectName(u"ExpandableSideMenu")
        self.verticalLayout_5 = QVBoxLayout(self.ExpandableSideMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 0)
        self.SideMenuFrame = QFrame(self.ExpandableSideMenu)
        self.SideMenuFrame.setObjectName(u"SideMenuFrame")
        self.SideMenuFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.SideMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.SideMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.SideMenuFrame)
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.Sidemenulabel = QLabelThemed(self.SideMenuFrame)
        self.Sidemenulabel.setObjectName(u"Sidemenulabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sidemenulabel.sizePolicy().hasHeightForWidth())
        self.Sidemenulabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.Sidemenulabel)

        self.ExitSideMenu = QPushButtonThemed(self.SideMenuFrame)
        self.ExitSideMenu.setObjectName(u"ExitSideMenu")
        self.ExitSideMenu.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ExitSideMenu.sizePolicy().hasHeightForWidth())
        self.ExitSideMenu.setSizePolicy(sizePolicy1)
        self.ExitSideMenu.setMinimumSize(QSize(0, 0))
        self.ExitSideMenu.setCursor(QCursor(Qt.OpenHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/png2svg/quitmenu-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/png2svg/quitmenu-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon7.addFile(u":/icons/png2svg/quitmenu-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.ExitSideMenu.setIcon(icon7)
        self.ExitSideMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.ExitSideMenu)


        self.verticalLayout_5.addWidget(self.SideMenuFrame)

        self.OptionsWidget = QStackedWidget(self.ExpandableSideMenu)
        self.OptionsWidget.setObjectName(u"OptionsWidget")
        self.Account_pg = QWidget()
        self.Account_pg.setObjectName(u"Account_pg")
        self.verticalLayout_17 = QVBoxLayout(self.Account_pg)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.AccountFrame = QFrame(self.Account_pg)
        self.AccountFrame.setObjectName(u"AccountFrame")
        self.AccountFrame.setFrameShape(QFrame.StyledPanel)
        self.AccountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.AccountFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.AccountNavWidget = QCustomQStackedWidget(self.AccountFrame)
        self.AccountNavWidget.setObjectName(u"AccountNavWidget")
        self.LoginnavWidget = QWidget()
        self.LoginnavWidget.setObjectName(u"LoginnavWidget")
        self.verticalLayout_26 = QVBoxLayout(self.LoginnavWidget)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(2, 0, 0, 0)
        self.loginnav = QFrame(self.LoginnavWidget)
        self.loginnav.setObjectName(u"loginnav")
        self.loginnav.setFrameShape(QFrame.StyledPanel)
        self.loginnav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.loginnav)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 38, 5, 24)
        self.welcomelabel = QLabelThemed(self.loginnav)
        self.welcomelabel.setObjectName(u"welcomelabel")

        self.verticalLayout_27.addWidget(self.welcomelabel)

        self.frame_5 = QFrame(self.loginnav)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_5)
        self.verticalLayout_63.setSpacing(19)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, -1, 0, 0)
        self.detailstologinlabel = QLabelThemed(self.frame_5)
        self.detailstologinlabel.setObjectName(u"detailstologinlabel")
        self.detailstologinlabel.setWordWrap(False)

        self.verticalLayout_63.addWidget(self.detailstologinlabel)

        self.notregisteredlabel = QLabelThemed(self.frame_5)
        self.notregisteredlabel.setObjectName(u"notregisteredlabel")

        self.verticalLayout_63.addWidget(self.notregisteredlabel)


        self.verticalLayout_27.addWidget(self.frame_5, 0, Qt.AlignVCenter)

        self.toSignupbutton = QPushButtonThemed(self.loginnav)
        self.toSignupbutton.setObjectName(u"toSignupbutton")
        self.toSignupbutton.setCursor(QCursor(Qt.OpenHandCursor))

        self.verticalLayout_27.addWidget(self.toSignupbutton, 0, Qt.AlignHCenter)


        self.verticalLayout_26.addWidget(self.loginnav)

        self.AccountNavWidget.addWidget(self.LoginnavWidget)
        self.SignUpnavWidget = QWidget()
        self.SignUpnavWidget.setObjectName(u"SignUpnavWidget")
        self.verticalLayout_28 = QVBoxLayout(self.SignUpnavWidget)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(2, 0, 1, 0)
        self.signupnav = QFrame(self.SignUpnavWidget)
        self.signupnav.setObjectName(u"signupnav")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.signupnav.sizePolicy().hasHeightForWidth())
        self.signupnav.setSizePolicy(sizePolicy2)
        self.signupnav.setFrameShape(QFrame.StyledPanel)
        self.signupnav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.signupnav)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 21, 4, 10)
        self.welcomelabel_2 = QLabelThemed(self.signupnav)
        self.welcomelabel_2.setObjectName(u"welcomelabel_2")

        self.verticalLayout_29.addWidget(self.welcomelabel_2)

        self.frame_3 = QFrame(self.signupnav)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_3)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.detailstosignuplabel = QLabelThemed(self.frame_3)
        self.detailstosignuplabel.setObjectName(u"detailstosignuplabel")
        self.detailstosignuplabel.setWordWrap(False)

        self.verticalLayout_61.addWidget(self.detailstosignuplabel)

        self.alreadyaccountlabel = QLabelThemed(self.frame_3)
        self.alreadyaccountlabel.setObjectName(u"alreadyaccountlabel")

        self.verticalLayout_61.addWidget(self.alreadyaccountlabel)


        self.verticalLayout_29.addWidget(self.frame_3)

        self.toLoginbutton = QPushButtonThemed(self.signupnav)
        self.toLoginbutton.setObjectName(u"toLoginbutton")
        self.toLoginbutton.setCursor(QCursor(Qt.OpenHandCursor))

        self.verticalLayout_29.addWidget(self.toLoginbutton)


        self.verticalLayout_28.addWidget(self.signupnav)

        self.AccountNavWidget.addWidget(self.SignUpnavWidget)

        self.horizontalLayout_7.addWidget(self.AccountNavWidget)

        self.AccountCreationWidget = QCustomQStackedWidget(self.AccountFrame)
        self.AccountCreationWidget.setObjectName(u"AccountCreationWidget")
        self.AccountCreationWidget.setFrameShadow(QFrame.Plain)
        self.LoginWidget = QWidget()
        self.LoginWidget.setObjectName(u"LoginWidget")
        self.verticalLayout_30 = QVBoxLayout(self.LoginWidget)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.loginFrame = QFrame(self.LoginWidget)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.loginFrame)
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 32, 0, 20)
        self.loginlabel = QLabelThemed(self.loginFrame)
        self.loginlabel.setObjectName(u"loginlabel")

        self.verticalLayout_31.addWidget(self.loginlabel)

        self.frame_4 = QFrame(self.loginFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_4)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.UsernameLoginEdit = QLineEdit(self.frame_4)
        self.UsernameLoginEdit.setObjectName(u"UsernameLoginEdit")
        self.UsernameLoginEdit.setAutoFillBackground(False)
        self.UsernameLoginEdit.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_62.addWidget(self.UsernameLoginEdit)

        self.PassLoginEdit = QLineEdit(self.frame_4)
        self.PassLoginEdit.setObjectName(u"PassLoginEdit")
        self.PassLoginEdit.setFrame(True)
        self.PassLoginEdit.setEchoMode(QLineEdit.Normal)
        self.PassLoginEdit.setReadOnly(False)

        self.verticalLayout_62.addWidget(self.PassLoginEdit)


        self.verticalLayout_31.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.forgotpasslabel = QLabelThemed(self.loginFrame)
        self.forgotpasslabel.setObjectName(u"forgotpasslabel")
        self.forgotpasslabel.setCursor(QCursor(Qt.OpenHandCursor))

        self.verticalLayout_31.addWidget(self.forgotpasslabel)

        self.Login_Button = QPushButtonThemed(self.loginFrame)
        self.Login_Button.setObjectName(u"Login_Button")
        self.Login_Button.setCursor(QCursor(Qt.OpenHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/png2svg/login-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/png2svg/login-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon8.addFile(u":/icons/png2svg/login-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.Login_Button.setIcon(icon8)
        self.Login_Button.setIconSize(QSize(24, 24))

        self.verticalLayout_31.addWidget(self.Login_Button)


        self.verticalLayout_30.addWidget(self.loginFrame)

        self.AccountCreationWidget.addWidget(self.LoginWidget)
        self.SignUpWidget = QWidget()
        self.SignUpWidget.setObjectName(u"SignUpWidget")
        self.verticalLayout_32 = QVBoxLayout(self.SignUpWidget)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.SignUpFrame = QFrame(self.SignUpWidget)
        self.SignUpFrame.setObjectName(u"SignUpFrame")
        sizePolicy2.setHeightForWidth(self.SignUpFrame.sizePolicy().hasHeightForWidth())
        self.SignUpFrame.setSizePolicy(sizePolicy2)
        self.SignUpFrame.setFrameShape(QFrame.StyledPanel)
        self.SignUpFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.SignUpFrame)
        self.verticalLayout_33.setSpacing(7)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 21, 0, 7)
        self.SignUplabel = QLabelThemed(self.SignUpFrame)
        self.SignUplabel.setObjectName(u"SignUplabel")

        self.verticalLayout_33.addWidget(self.SignUplabel)

        self.frame = QFrame(self.SignUpFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.UsernameSignupEdit = QLineEdit(self.frame)
        self.UsernameSignupEdit.setObjectName(u"UsernameSignupEdit")
        self.UsernameSignupEdit.setAutoFillBackground(False)

        self.verticalLayout_9.addWidget(self.UsernameSignupEdit)

        self.PassSignupEdit = QLineEdit(self.frame)
        self.PassSignupEdit.setObjectName(u"PassSignupEdit")
        self.PassSignupEdit.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_9.addWidget(self.PassSignupEdit)

        self.ConfirmPassEdit = QLineEdit(self.frame)
        self.ConfirmPassEdit.setObjectName(u"ConfirmPassEdit")
        self.ConfirmPassEdit.setEchoMode(QLineEdit.Normal)
        self.ConfirmPassEdit.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.ConfirmPassEdit)

        self.Strengthmeter = QProgressBar(self.frame)
        self.Strengthmeter.setObjectName(u"Strengthmeter")
        self.Strengthmeter.setValue(0)
        self.Strengthmeter.setTextVisible(True)
        self.Strengthmeter.setInvertedAppearance(False)
        self.Strengthmeter.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_9.addWidget(self.Strengthmeter)


        self.verticalLayout_33.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.SignUpbutton = QPushButtonThemed(self.SignUpFrame)
        self.SignUpbutton.setObjectName(u"SignUpbutton")
        self.SignUpbutton.setCursor(QCursor(Qt.OpenHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/png2svg/signup-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/png2svg/signup-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon9.addFile(u":/icons/png2svg/signup-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.SignUpbutton.setIcon(icon9)
        self.SignUpbutton.setIconSize(QSize(24, 24))

        self.verticalLayout_33.addWidget(self.SignUpbutton)


        self.verticalLayout_32.addWidget(self.SignUpFrame)

        self.AccountCreationWidget.addWidget(self.SignUpWidget)

        self.horizontalLayout_7.addWidget(self.AccountCreationWidget)


        self.verticalLayout_17.addWidget(self.AccountFrame)

        self.OptionsWidget.addWidget(self.Account_pg)
        self.LoggedInPage = QWidget()
        self.LoggedInPage.setObjectName(u"LoggedInPage")
        self.verticalLayout_6 = QVBoxLayout(self.LoggedInPage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.LoggedIn = QFrame(self.LoggedInPage)
        self.LoggedIn.setObjectName(u"LoggedIn")
        self.LoggedIn.setFrameShape(QFrame.StyledPanel)
        self.LoggedIn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.LoggedIn)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.LogoutButton = QPushButtonThemed(self.LoggedIn)
        self.LogoutButton.setObjectName(u"LogoutButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/png2svg/logout-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/png2svg/logout-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon10.addFile(u":/icons/png2svg/logout-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.LogoutButton.setIcon(icon10)
        self.LogoutButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.LogoutButton)


        self.verticalLayout_6.addWidget(self.LoggedIn, 0, Qt.AlignTop)

        self.LoggedInframe = QFrame(self.LoggedInPage)
        self.LoggedInframe.setObjectName(u"LoggedInframe")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LoggedInframe.sizePolicy().hasHeightForWidth())
        self.LoggedInframe.setSizePolicy(sizePolicy3)
        self.LoggedInframe.setFrameShape(QFrame.StyledPanel)
        self.LoggedInframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.LoggedInframe)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.LoggedInLabel = QLabelThemed(self.LoggedInframe)
        self.LoggedInLabel.setObjectName(u"LoggedInLabel")

        self.verticalLayout_7.addWidget(self.LoggedInLabel)

        self.usernameLoggedinlabel = QLabelThemed(self.LoggedInframe)
        self.usernameLoggedinlabel.setObjectName(u"usernameLoggedinlabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.usernameLoggedinlabel.setFont(font)

        self.verticalLayout_7.addWidget(self.usernameLoggedinlabel)

        self.label_5 = QLabelThemed(self.LoggedInframe)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabelThemed(self.LoggedInframe)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)


        self.verticalLayout_6.addWidget(self.LoggedInframe)

        self.OptionsWidget.addWidget(self.LoggedInPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.horizontalLayout_6 = QHBoxLayout(self.SettingsPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SettingsIconFrame = QFrame(self.SettingsPage)
        self.SettingsIconFrame.setObjectName(u"SettingsIconFrame")
        self.SettingsIconFrame.setFrameShape(QFrame.StyledPanel)
        self.SettingsIconFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.SettingsIconFrame)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.camerasettingthread = QFrame(self.SettingsIconFrame)
        self.camerasettingthread.setObjectName(u"camerasettingthread")
        self.camerasettingthread.setFrameShape(QFrame.StyledPanel)
        self.camerasettingthread.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.camerasettingthread)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_9 = QLabelThemed(self.camerasettingthread)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/icons/png2svg/SwitchCamera.svg"))

        self.horizontalLayout_25.addWidget(self.label_9)

        self.CameraSettingComboBox = QComboBox(self.camerasettingthread)
        self.CameraSettingComboBox.addItem("")
        self.CameraSettingComboBox.setObjectName(u"CameraSettingComboBox")
        self.CameraSettingComboBox.setEditable(False)
        self.CameraSettingComboBox.setMaxVisibleItems(10)

        self.horizontalLayout_25.addWidget(self.CameraSettingComboBox)


        self.verticalLayout_42.addWidget(self.camerasettingthread)

        self.CameraRescan = QPushButtonThemed(self.SettingsIconFrame)
        self.CameraRescan.setObjectName(u"CameraRescan")

        self.verticalLayout_42.addWidget(self.CameraRescan, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.SettingsIconFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_42.addWidget(self.frame_2)


        self.horizontalLayout_6.addWidget(self.SettingsIconFrame)

        self.OptionsWidget.addWidget(self.SettingsPage)

        self.verticalLayout_5.addWidget(self.OptionsWidget)

        self.NotificationsWidget = QWidget(self.ExpandableSideMenu)
        self.NotificationsWidget.setObjectName(u"NotificationsWidget")
        sizePolicy3.setHeightForWidth(self.NotificationsWidget.sizePolicy().hasHeightForWidth())
        self.NotificationsWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_14 = QVBoxLayout(self.NotificationsWidget)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.NotFrame = QFrame(self.NotificationsWidget)
        self.NotFrame.setObjectName(u"NotFrame")
        self.NotFrame.setFrameShape(QFrame.StyledPanel)
        self.NotFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.NotFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 7, 0)
        self.iconNot = QLabelThemed(self.NotFrame)
        self.iconNot.setObjectName(u"iconNot")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.iconNot.sizePolicy().hasHeightForWidth())
        self.iconNot.setSizePolicy(sizePolicy4)
        self.iconNot.setPixmap(QPixmap(u":/icons/png2svg/notifications_icon.svg"))

        self.horizontalLayout_5.addWidget(self.iconNot, 0, Qt.AlignLeft)

        self.labelNot = QLabelThemed(self.NotFrame)
        self.labelNot.setObjectName(u"labelNot")

        self.horizontalLayout_5.addWidget(self.labelNot, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.AcknowledgeNotifications = QPushButtonThemed(self.NotFrame)
        self.AcknowledgeNotifications.setObjectName(u"AcknowledgeNotifications")

        self.horizontalLayout_5.addWidget(self.AcknowledgeNotifications, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.NotFrame, 0, Qt.AlignTop)

        self.Notification_Frame = QFrame(self.NotificationsWidget)
        self.Notification_Frame.setObjectName(u"Notification_Frame")
        sizePolicy3.setHeightForWidth(self.Notification_Frame.sizePolicy().hasHeightForWidth())
        self.Notification_Frame.setSizePolicy(sizePolicy3)
        self.Notification_Frame.setFrameShape(QFrame.StyledPanel)
        self.Notification_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Notification_Frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.Notification_Frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.Notifications_Panel = QWidget()
        self.Notifications_Panel.setObjectName(u"Notifications_Panel")
        self.Notifications_Panel.setGeometry(QRect(0, 0, 401, 173))
        self.verticalLayout_41 = QVBoxLayout(self.Notifications_Panel)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2.setWidget(self.Notifications_Panel)

        self.verticalLayout_15.addWidget(self.scrollArea_2)


        self.verticalLayout_14.addWidget(self.Notification_Frame)


        self.verticalLayout_5.addWidget(self.NotificationsWidget)


        self.horizontalLayout.addWidget(self.ExpandableSideMenu, 0, Qt.AlignLeft)

        self.Main_body = QWidget(self.centralwidget)
        self.Main_body.setObjectName(u"Main_body")
        sizePolicy.setHeightForWidth(self.Main_body.sizePolicy().hasHeightForWidth())
        self.Main_body.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.Main_body)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.MainWidget = QCustomQStackedWidget(self.Main_body)
        self.MainWidget.setObjectName(u"MainWidget")
        sizePolicy4.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy4)
        self.Translator = QWidget()
        self.Translator.setObjectName(u"Translator")
        self.verticalLayout_23 = QVBoxLayout(self.Translator)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 10)
        self.UpperTranslatorFrame = QFrame(self.Translator)
        self.UpperTranslatorFrame.setObjectName(u"UpperTranslatorFrame")
        self.UpperTranslatorFrame.setFrameShape(QFrame.StyledPanel)
        self.UpperTranslatorFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.UpperTranslatorFrame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label = QLabelThemed(self.UpperTranslatorFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_24.addWidget(self.label)


        self.verticalLayout_23.addWidget(self.UpperTranslatorFrame, 0, Qt.AlignTop)

        self.MainTranslatorWidget = QWidget(self.Translator)
        self.MainTranslatorWidget.setObjectName(u"MainTranslatorWidget")
        sizePolicy3.setHeightForWidth(self.MainTranslatorWidget.sizePolicy().hasHeightForWidth())
        self.MainTranslatorWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_13 = QHBoxLayout(self.MainTranslatorWidget)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.LiveTranslationWidget = QWidget(self.MainTranslatorWidget)
        self.LiveTranslationWidget.setObjectName(u"LiveTranslationWidget")
        sizePolicy.setHeightForWidth(self.LiveTranslationWidget.sizePolicy().hasHeightForWidth())
        self.LiveTranslationWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.LiveTranslationWidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.LiveTranslationTop = QFrame(self.LiveTranslationWidget)
        self.LiveTranslationTop.setObjectName(u"LiveTranslationTop")
        self.LiveTranslationTop.setFrameShape(QFrame.StyledPanel)
        self.LiveTranslationTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.LiveTranslationTop)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.livecameradisplay = QLabelThemed(self.LiveTranslationTop)
        self.livecameradisplay.setObjectName(u"livecameradisplay")
        sizePolicy4.setHeightForWidth(self.livecameradisplay.sizePolicy().hasHeightForWidth())
        self.livecameradisplay.setSizePolicy(sizePolicy4)
        self.livecameradisplay.setLineWidth(0)
        self.livecameradisplay.setPixmap(QPixmap(u":/icons/png2svg/Camera.svg"))
        self.livecameradisplay.setScaledContents(True)
        self.livecameradisplay.setIndent(1)

        self.horizontalLayout_10.addWidget(self.livecameradisplay, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.livelabel = QLabelThemed(self.LiveTranslationTop)
        self.livelabel.setObjectName(u"livelabel")

        self.horizontalLayout_10.addWidget(self.livelabel)


        self.verticalLayout_10.addWidget(self.LiveTranslationTop, 0, Qt.AlignTop)

        self.LiveTranslationInfo = QFrame(self.LiveTranslationWidget)
        self.LiveTranslationInfo.setObjectName(u"LiveTranslationInfo")
        self.LiveTranslationInfo.setFrameShape(QFrame.StyledPanel)
        self.LiveTranslationInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.LiveTranslationInfo)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.LiveTranDescription = QLabelThemed(self.LiveTranslationInfo)
        self.LiveTranDescription.setObjectName(u"LiveTranDescription")

        self.verticalLayout_12.addWidget(self.LiveTranDescription)


        self.verticalLayout_10.addWidget(self.LiveTranslationInfo)

        self.LiveTranslationBottom = QFrame(self.LiveTranslationWidget)
        self.LiveTranslationBottom.setObjectName(u"LiveTranslationBottom")
        self.LiveTranslationBottom.setFrameShape(QFrame.StyledPanel)
        self.LiveTranslationBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.LiveTranslationBottom)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.StartLiveTranslationbutton = QPushButtonThemed(self.LiveTranslationBottom)
        self.StartLiveTranslationbutton.setObjectName(u"StartLiveTranslationbutton")
        self.StartLiveTranslationbutton.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.StartLiveTranslationbutton)


        self.verticalLayout_10.addWidget(self.LiveTranslationBottom, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.LiveTranslationWidget)

        self.SpellingBeeWidget = QWidget(self.MainTranslatorWidget)
        self.SpellingBeeWidget.setObjectName(u"SpellingBeeWidget")
        sizePolicy.setHeightForWidth(self.SpellingBeeWidget.sizePolicy().hasHeightForWidth())
        self.SpellingBeeWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.SpellingBeeWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, -1)
        self.BeeTopFrame = QFrame(self.SpellingBeeWidget)
        self.BeeTopFrame.setObjectName(u"BeeTopFrame")
        self.BeeTopFrame.setFrameShape(QFrame.StyledPanel)
        self.BeeTopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.BeeTopFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabelThemed(self.BeeTopFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icons/png2svg/SpellingBee.svg"))

        self.horizontalLayout_11.addWidget(self.label_4)

        self.label_2 = QLabelThemed(self.BeeTopFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_11.addWidget(self.label_2)


        self.verticalLayout_13.addWidget(self.BeeTopFrame, 0, Qt.AlignTop)

        self.BeeInfoFrame = QFrame(self.SpellingBeeWidget)
        self.BeeInfoFrame.setObjectName(u"BeeInfoFrame")
        self.BeeInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.BeeInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.BeeInfoFrame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.BeeTranDescription = QLabelThemed(self.BeeInfoFrame)
        self.BeeTranDescription.setObjectName(u"BeeTranDescription")

        self.verticalLayout_22.addWidget(self.BeeTranDescription)


        self.verticalLayout_13.addWidget(self.BeeInfoFrame)

        self.BeeTranBottomFrame = QFrame(self.SpellingBeeWidget)
        self.BeeTranBottomFrame.setObjectName(u"BeeTranBottomFrame")
        sizePolicy4.setHeightForWidth(self.BeeTranBottomFrame.sizePolicy().hasHeightForWidth())
        self.BeeTranBottomFrame.setSizePolicy(sizePolicy4)
        self.BeeTranBottomFrame.setFrameShape(QFrame.StyledPanel)
        self.BeeTranBottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.BeeTranBottomFrame)
        self.verticalLayout_20.setSpacing(28)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.SpellingBeenotificationlabel = QLabelThemed(self.BeeTranBottomFrame)
        self.SpellingBeenotificationlabel.setObjectName(u"SpellingBeenotificationlabel")
        self.SpellingBeenotificationlabel.setFont(font)
        self.SpellingBeenotificationlabel.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.SpellingBeenotificationlabel)

        self.SpellingBeeWordEntry = QLineEdit(self.BeeTranBottomFrame)
        self.SpellingBeeWordEntry.setObjectName(u"SpellingBeeWordEntry")

        self.verticalLayout_20.addWidget(self.SpellingBeeWordEntry)

        self.StartSpellingBeeButton = QPushButtonThemed(self.BeeTranBottomFrame)
        self.StartSpellingBeeButton.setObjectName(u"StartSpellingBeeButton")
        self.StartSpellingBeeButton.setIconSize(QSize(24, 24))

        self.verticalLayout_20.addWidget(self.StartSpellingBeeButton)


        self.verticalLayout_13.addWidget(self.BeeTranBottomFrame, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.SpellingBeeWidget, 0, Qt.AlignHCenter)

        self.CatalogueTranWidget = QWidget(self.MainTranslatorWidget)
        self.CatalogueTranWidget.setObjectName(u"CatalogueTranWidget")
        sizePolicy.setHeightForWidth(self.CatalogueTranWidget.sizePolicy().hasHeightForWidth())
        self.CatalogueTranWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_18 = QVBoxLayout(self.CatalogueTranWidget)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.CatalogueTranUpperframe = QFrame(self.CatalogueTranWidget)
        self.CatalogueTranUpperframe.setObjectName(u"CatalogueTranUpperframe")
        self.CatalogueTranUpperframe.setFrameShape(QFrame.StyledPanel)
        self.CatalogueTranUpperframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.CatalogueTranUpperframe)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabelThemed(self.CatalogueTranUpperframe)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/icons/png2svg/Catalogue.svg"))

        self.horizontalLayout_12.addWidget(self.label_8)

        self.label_7 = QLabelThemed(self.CatalogueTranUpperframe)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)


        self.verticalLayout_18.addWidget(self.CatalogueTranUpperframe, 0, Qt.AlignTop)

        self.CatalogueDescription = QFrame(self.CatalogueTranWidget)
        self.CatalogueDescription.setObjectName(u"CatalogueDescription")
        self.CatalogueDescription.setFrameShape(QFrame.StyledPanel)
        self.CatalogueDescription.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.CatalogueDescription)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabelThemed(self.CatalogueDescription)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_19.addWidget(self.label_10)


        self.verticalLayout_18.addWidget(self.CatalogueDescription)

        self.TranCatBottomFrame = QFrame(self.CatalogueTranWidget)
        self.TranCatBottomFrame.setObjectName(u"TranCatBottomFrame")
        self.TranCatBottomFrame.setFrameShape(QFrame.StyledPanel)
        self.TranCatBottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.TranCatBottomFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.OpenCatalogueButton = QPushButtonThemed(self.TranCatBottomFrame)
        self.OpenCatalogueButton.setObjectName(u"OpenCatalogueButton")
        self.OpenCatalogueButton.setIconSize(QSize(24, 24))

        self.verticalLayout_21.addWidget(self.OpenCatalogueButton)


        self.verticalLayout_18.addWidget(self.TranCatBottomFrame, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.CatalogueTranWidget)


        self.verticalLayout_23.addWidget(self.MainTranslatorWidget)

        self.MainWidget.addWidget(self.Translator)
        self.Catalogue = QWidget()
        self.Catalogue.setObjectName(u"Catalogue")
        self.verticalLayout_34 = QVBoxLayout(self.Catalogue)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.CatalogueUpperMenuFrame = QFrame(self.Catalogue)
        self.CatalogueUpperMenuFrame.setObjectName(u"CatalogueUpperMenuFrame")
        self.CatalogueUpperMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.CatalogueUpperMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.CatalogueUpperMenuFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.CatalogueMenuLabel = QLabelThemed(self.CatalogueUpperMenuFrame)
        self.CatalogueMenuLabel.setObjectName(u"CatalogueMenuLabel")

        self.horizontalLayout_8.addWidget(self.CatalogueMenuLabel)

        self.CatalogueToTranslatorButton = QPushButtonThemed(self.CatalogueUpperMenuFrame)
        self.CatalogueToTranslatorButton.setObjectName(u"CatalogueToTranslatorButton")
        icon11 = QIcon()
        icon11.addFile(u":/icons/png2svg/goback-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/png2svg/goback-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon11.addFile(u":/icons/png2svg/goback-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.CatalogueToTranslatorButton.setIcon(icon11)
        self.CatalogueToTranslatorButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.CatalogueToTranslatorButton, 0, Qt.AlignRight)


        self.verticalLayout_34.addWidget(self.CatalogueUpperMenuFrame, 0, Qt.AlignTop)

        self.CatalogueMainWidget = QWidget(self.Catalogue)
        self.CatalogueMainWidget.setObjectName(u"CatalogueMainWidget")
        sizePolicy3.setHeightForWidth(self.CatalogueMainWidget.sizePolicy().hasHeightForWidth())
        self.CatalogueMainWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_35 = QVBoxLayout(self.CatalogueMainWidget)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.CatalogueOptionsframe = QFrame(self.CatalogueMainWidget)
        self.CatalogueOptionsframe.setObjectName(u"CatalogueOptionsframe")
        self.CatalogueOptionsframe.setFrameShape(QFrame.StyledPanel)
        self.CatalogueOptionsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.CatalogueOptionsframe)
        self.horizontalLayout_9.setSpacing(44)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SearchingOptionFrame = QFrame(self.CatalogueOptionsframe)
        self.SearchingOptionFrame.setObjectName(u"SearchingOptionFrame")
        self.SearchingOptionFrame.setFrameShape(QFrame.StyledPanel)
        self.SearchingOptionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.SearchingOptionFrame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 0, 0, 0)
        self.SearchIconLabel = QLabelThemed(self.SearchingOptionFrame)
        self.SearchIconLabel.setObjectName(u"SearchIconLabel")
        self.SearchIconLabel.setPixmap(QPixmap(u":/icons/png2svg/search-white.svg"))
        self.SearchIconLabel.setScaledContents(False)
        self.SearchIconLabel.setWordWrap(False)

        self.horizontalLayout_24.addWidget(self.SearchIconLabel)

        self.CatalogueSearchBar = QLineEdit(self.SearchingOptionFrame)
        self.CatalogueSearchBar.setObjectName(u"CatalogueSearchBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.CatalogueSearchBar.sizePolicy().hasHeightForWidth())
        self.CatalogueSearchBar.setSizePolicy(sizePolicy5)
        self.CatalogueSearchBar.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_24.addWidget(self.CatalogueSearchBar)


        self.horizontalLayout_9.addWidget(self.SearchingOptionFrame, 0, Qt.AlignTop)

        self.categorySearchLabel = QLabelThemed(self.CatalogueOptionsframe)
        self.categorySearchLabel.setObjectName(u"categorySearchLabel")

        self.horizontalLayout_9.addWidget(self.categorySearchLabel, 0, Qt.AlignRight)

        self.CatagoryChooserFrame = QFrame(self.CatalogueOptionsframe)
        self.CatagoryChooserFrame.setObjectName(u"CatagoryChooserFrame")
        self.CatagoryChooserFrame.setFrameShape(QFrame.StyledPanel)
        self.CatagoryChooserFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.CatagoryChooserFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.CatalogueCategoryselector = QComboBox(self.CatagoryChooserFrame)
        self.CatalogueCategoryselector.addItem("")
        self.CatalogueCategoryselector.setObjectName(u"CatalogueCategoryselector")
        sizePolicy2.setHeightForWidth(self.CatalogueCategoryselector.sizePolicy().hasHeightForWidth())
        self.CatalogueCategoryselector.setSizePolicy(sizePolicy2)
        self.CatalogueCategoryselector.setEditable(False)

        self.verticalLayout_8.addWidget(self.CatalogueCategoryselector)


        self.horizontalLayout_9.addWidget(self.CatagoryChooserFrame)


        self.verticalLayout_35.addWidget(self.CatalogueOptionsframe, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.CatalogueMainWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.CatalogueWidget = QWidget()
        self.CatalogueWidget.setObjectName(u"CatalogueWidget")
        self.CatalogueWidget.setGeometry(QRect(0, 0, 638, 447))
        self.gridLayout = QGridLayout(self.CatalogueWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.CatalogueWidget)

        self.verticalLayout_35.addWidget(self.scrollArea)


        self.verticalLayout_34.addWidget(self.CatalogueMainWidget)

        self.MainWidget.addWidget(self.Catalogue)
        self.Overview = QWidget()
        self.Overview.setObjectName(u"Overview")
        self.verticalLayout_36 = QVBoxLayout(self.Overview)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.UpperOverviewFrame = QFrame(self.Overview)
        self.UpperOverviewFrame.setObjectName(u"UpperOverviewFrame")
        self.UpperOverviewFrame.setFrameShape(QFrame.StyledPanel)
        self.UpperOverviewFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.UpperOverviewFrame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabelThemed(self.UpperOverviewFrame)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.OverviewToCatalogueButton = QPushButtonThemed(self.UpperOverviewFrame)
        self.OverviewToCatalogueButton.setObjectName(u"OverviewToCatalogueButton")
        self.OverviewToCatalogueButton.setIcon(icon11)
        self.OverviewToCatalogueButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.OverviewToCatalogueButton, 0, Qt.AlignRight)


        self.verticalLayout_36.addWidget(self.UpperOverviewFrame, 0, Qt.AlignTop)

        self.MainOverviewWidget = QWidget(self.Overview)
        self.MainOverviewWidget.setObjectName(u"MainOverviewWidget")
        sizePolicy3.setHeightForWidth(self.MainOverviewWidget.sizePolicy().hasHeightForWidth())
        self.MainOverviewWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_15 = QHBoxLayout(self.MainOverviewWidget)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.OverviewInfoFrame = QFrame(self.MainOverviewWidget)
        self.OverviewInfoFrame.setObjectName(u"OverviewInfoFrame")
        self.OverviewInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.OverviewInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.OverviewInfoFrame)
        self.verticalLayout_37.setSpacing(14)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.WordOverviewFrame = QFrame(self.OverviewInfoFrame)
        self.WordOverviewFrame.setObjectName(u"WordOverviewFrame")
        self.WordOverviewFrame.setFrameShape(QFrame.StyledPanel)
        self.WordOverviewFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.WordOverviewFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.OverviewWordLabel = QLabelThemed(self.WordOverviewFrame)
        self.OverviewWordLabel.setObjectName(u"OverviewWordLabel")

        self.horizontalLayout_29.addWidget(self.OverviewWordLabel)

        self.WordOverviewlabel = QLabelThemed(self.WordOverviewFrame)
        self.WordOverviewlabel.setObjectName(u"WordOverviewlabel")
        self.WordOverviewlabel.setFont(font)

        self.horizontalLayout_29.addWidget(self.WordOverviewlabel)


        self.verticalLayout_37.addWidget(self.WordOverviewFrame)

        self.CategoryOverviewFrame = QFrame(self.OverviewInfoFrame)
        self.CategoryOverviewFrame.setObjectName(u"CategoryOverviewFrame")
        self.CategoryOverviewFrame.setFrameShape(QFrame.StyledPanel)
        self.CategoryOverviewFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.CategoryOverviewFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 10, 0, 0)
        self.OverviewCategoryLabel = QLabelThemed(self.CategoryOverviewFrame)
        self.OverviewCategoryLabel.setObjectName(u"OverviewCategoryLabel")

        self.horizontalLayout_27.addWidget(self.OverviewCategoryLabel)

        self.CategoryOverviewLabel = QLabelThemed(self.CategoryOverviewFrame)
        self.CategoryOverviewLabel.setObjectName(u"CategoryOverviewLabel")
        self.CategoryOverviewLabel.setFont(font)

        self.horizontalLayout_27.addWidget(self.CategoryOverviewLabel)


        self.verticalLayout_37.addWidget(self.CategoryOverviewFrame)

        self.AttemptsOverviewFrame = QFrame(self.OverviewInfoFrame)
        self.AttemptsOverviewFrame.setObjectName(u"AttemptsOverviewFrame")
        self.AttemptsOverviewFrame.setFrameShape(QFrame.StyledPanel)
        self.AttemptsOverviewFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.AttemptsOverviewFrame)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 6, 0, 0)
        self.OverviewNoAttemptsLabel = QLabelThemed(self.AttemptsOverviewFrame)
        self.OverviewNoAttemptsLabel.setObjectName(u"OverviewNoAttemptsLabel")

        self.horizontalLayout_28.addWidget(self.OverviewNoAttemptsLabel)

        self.NoAttemptsOverviewLabel = QLabelThemed(self.AttemptsOverviewFrame)
        self.NoAttemptsOverviewLabel.setObjectName(u"NoAttemptsOverviewLabel")
        self.NoAttemptsOverviewLabel.setFont(font)

        self.horizontalLayout_28.addWidget(self.NoAttemptsOverviewLabel)


        self.verticalLayout_37.addWidget(self.AttemptsOverviewFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_3)


        self.horizontalLayout_15.addWidget(self.OverviewInfoFrame, 0, Qt.AlignLeft)

        self.VideoWidget = QWidget(self.MainOverviewWidget)
        self.VideoWidget.setObjectName(u"VideoWidget")
        sizePolicy.setHeightForWidth(self.VideoWidget.sizePolicy().hasHeightForWidth())
        self.VideoWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_38 = QVBoxLayout(self.VideoWidget)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.VideoPlayingWidget = QWidget(self.VideoWidget)
        self.VideoPlayingWidget.setObjectName(u"VideoPlayingWidget")
        sizePolicy3.setHeightForWidth(self.VideoPlayingWidget.sizePolicy().hasHeightForWidth())
        self.VideoPlayingWidget.setSizePolicy(sizePolicy3)
        self.verticalLayout_65 = QVBoxLayout(self.VideoPlayingWidget)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")

        self.verticalLayout_38.addWidget(self.VideoPlayingWidget)

        self.VideoControlsFrane = QFrame(self.VideoWidget)
        self.VideoControlsFrane.setObjectName(u"VideoControlsFrane")
        self.VideoControlsFrane.setFrameShape(QFrame.StyledPanel)
        self.VideoControlsFrane.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.VideoControlsFrane)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.SeekerFrame = QFrame(self.VideoControlsFrane)
        self.SeekerFrame.setObjectName(u"SeekerFrame")
        self.SeekerFrame.setFrameShape(QFrame.StyledPanel)
        self.SeekerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.SeekerFrame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.DurationWatchedlabel = QLabelThemed(self.SeekerFrame)
        self.DurationWatchedlabel.setObjectName(u"DurationWatchedlabel")
        self.DurationWatchedlabel.setFont(font)

        self.horizontalLayout_31.addWidget(self.DurationWatchedlabel)

        self.Vidlengthlabel = QLabelThemed(self.SeekerFrame)
        self.Vidlengthlabel.setObjectName(u"Vidlengthlabel")
        self.Vidlengthlabel.setFont(font)

        self.horizontalLayout_31.addWidget(self.Vidlengthlabel)

        self.VideoSeekerSlider = QSlider(self.SeekerFrame)
        self.VideoSeekerSlider.setObjectName(u"VideoSeekerSlider")
        self.VideoSeekerSlider.setCursor(QCursor(Qt.OpenHandCursor))
        self.VideoSeekerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_31.addWidget(self.VideoSeekerSlider)

        self.PlayVideoButton = QPushButtonThemed(self.SeekerFrame)
        self.PlayVideoButton.setObjectName(u"PlayVideoButton")
        icon12 = QIcon()
        icon12.addFile(u":/icons/png2svg/play_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icons/png2svg/play_white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon12.addFile(u":/icons/png2svg/play_green.svg", QSize(), QIcon.Active, QIcon.On)
        self.PlayVideoButton.setIcon(icon12)
        self.PlayVideoButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_31.addWidget(self.PlayVideoButton)


        self.verticalLayout_64.addWidget(self.SeekerFrame, 0, Qt.AlignBottom)


        self.verticalLayout_38.addWidget(self.VideoControlsFrane, 0, Qt.AlignBottom)

        self.label_11 = QLabelThemed(self.VideoWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_38.addWidget(self.label_11)


        self.horizontalLayout_15.addWidget(self.VideoWidget)


        self.verticalLayout_36.addWidget(self.MainOverviewWidget)

        self.StartSigningButton = QPushButtonThemed(self.Overview)
        self.StartSigningButton.setObjectName(u"StartSigningButton")
        self.StartSigningButton.setCursor(QCursor(Qt.OpenHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/png2svg/Signit-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icons/png2svg/Signit-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon13.addFile(u":/icons/png2svg/Signit-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.StartSigningButton.setIcon(icon13)
        self.StartSigningButton.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.StartSigningButton, 0, Qt.AlignHCenter)

        self.MainWidget.addWidget(self.Overview)
        self.Live_pg = QWidget()
        self.Live_pg.setObjectName(u"Live_pg")
        self.verticalLayout_43 = QVBoxLayout(self.Live_pg)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.LiveTopFrame = QFrame(self.Live_pg)
        self.LiveTopFrame.setObjectName(u"LiveTopFrame")
        self.LiveTopFrame.setFrameShape(QFrame.StyledPanel)
        self.LiveTopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.LiveTopFrame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Livetoplabel = QLabelThemed(self.LiveTopFrame)
        self.Livetoplabel.setObjectName(u"Livetoplabel")

        self.horizontalLayout_17.addWidget(self.Livetoplabel, 0, Qt.AlignLeft)

        self.LiveModeLabel = QLabelThemed(self.LiveTopFrame)
        self.LiveModeLabel.setObjectName(u"LiveModeLabel")
        sizePolicy.setHeightForWidth(self.LiveModeLabel.sizePolicy().hasHeightForWidth())
        self.LiveModeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.LiveModeLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)


        self.verticalLayout_43.addWidget(self.LiveTopFrame)

        self.CameraStatus = QLabelThemed(self.Live_pg)
        self.CameraStatus.setObjectName(u"CameraStatus")

        self.verticalLayout_43.addWidget(self.CameraStatus, 0, Qt.AlignTop)

        self.LiveMainWidget = QWidget(self.Live_pg)
        self.LiveMainWidget.setObjectName(u"LiveMainWidget")
        self.horizontalLayout_18 = QHBoxLayout(self.LiveMainWidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.leftframe = QFrame(self.LiveMainWidget)
        self.leftframe.setObjectName(u"leftframe")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.leftframe.sizePolicy().hasHeightForWidth())
        self.leftframe.setSizePolicy(sizePolicy6)
        self.leftframe.setFrameShape(QFrame.StyledPanel)
        self.leftframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.leftframe)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, -1)
        self.LiveCVframe = QFrame(self.leftframe)
        self.LiveCVframe.setObjectName(u"LiveCVframe")
        sizePolicy6.setHeightForWidth(self.LiveCVframe.sizePolicy().hasHeightForWidth())
        self.LiveCVframe.setSizePolicy(sizePolicy6)
        self.LiveCVframe.setFrameShape(QFrame.StyledPanel)
        self.LiveCVframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.LiveCVframe)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.LiveFootageLabel = QLabelThemed(self.LiveCVframe)
        self.LiveFootageLabel.setObjectName(u"LiveFootageLabel")
        sizePolicy6.setHeightForWidth(self.LiveFootageLabel.sizePolicy().hasHeightForWidth())
        self.LiveFootageLabel.setSizePolicy(sizePolicy6)

        self.verticalLayout_50.addWidget(self.LiveFootageLabel)


        self.verticalLayout_45.addWidget(self.LiveCVframe)

        self.bottomLiveFrame = QFrame(self.leftframe)
        self.bottomLiveFrame.setObjectName(u"bottomLiveFrame")
        self.bottomLiveFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomLiveFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.bottomLiveFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.LiveBottomInfoFrame = QFrame(self.bottomLiveFrame)
        self.LiveBottomInfoFrame.setObjectName(u"LiveBottomInfoFrame")
        self.LiveBottomInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.LiveBottomInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.LiveBottomInfoFrame)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_7 = QFrame(self.LiveBottomInfoFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.LivePredictionLabel = QLabelThemed(self.frame_7)
        self.LivePredictionLabel.setObjectName(u"LivePredictionLabel")

        self.horizontalLayout_32.addWidget(self.LivePredictionLabel)

        self.predictionlabel = QLabelThemed(self.frame_7)
        self.predictionlabel.setObjectName(u"predictionlabel")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.predictionlabel.setFont(font1)

        self.horizontalLayout_32.addWidget(self.predictionlabel)


        self.verticalLayout_47.addWidget(self.frame_7)


        self.horizontalLayout_19.addWidget(self.LiveBottomInfoFrame)

        self.LiveButtonsFrame = QFrame(self.bottomLiveFrame)
        self.LiveButtonsFrame.setObjectName(u"LiveButtonsFrame")
        self.LiveButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.LiveButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.LiveButtonsFrame)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.LiveAddtoTypedButton = QPushButtonThemed(self.LiveButtonsFrame)
        self.LiveAddtoTypedButton.setObjectName(u"LiveAddtoTypedButton")
        self.LiveAddtoTypedButton.setIconSize(QSize(24, 24))

        self.verticalLayout_46.addWidget(self.LiveAddtoTypedButton)

        self.LiveContinueButton = QPushButtonThemed(self.LiveButtonsFrame)
        self.LiveContinueButton.setObjectName(u"LiveContinueButton")
        icon14 = QIcon()
        icon14.addFile(u":/icons/png2svg/continue-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/icons/png2svg/continue-white.svg", QSize(), QIcon.Active, QIcon.Off)
        icon14.addFile(u":/icons/png2svg/continue-green.svg", QSize(), QIcon.Active, QIcon.On)
        self.LiveContinueButton.setIcon(icon14)
        self.LiveContinueButton.setIconSize(QSize(24, 24))

        self.verticalLayout_46.addWidget(self.LiveContinueButton)


        self.horizontalLayout_19.addWidget(self.LiveButtonsFrame)


        self.verticalLayout_45.addWidget(self.bottomLiveFrame, 0, Qt.AlignBottom)


        self.horizontalLayout_18.addWidget(self.leftframe)

        self.LiveRightFrame = QFrame(self.LiveMainWidget)
        self.LiveRightFrame.setObjectName(u"LiveRightFrame")
        self.LiveRightFrame.setFrameShape(QFrame.StyledPanel)
        self.LiveRightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.LiveRightFrame)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.LiveToTranslatorButton = QPushButtonThemed(self.LiveRightFrame)
        self.LiveToTranslatorButton.setObjectName(u"LiveToTranslatorButton")
        self.LiveToTranslatorButton.setIcon(icon7)
        self.LiveToTranslatorButton.setIconSize(QSize(24, 24))

        self.verticalLayout_44.addWidget(self.LiveToTranslatorButton)

        self.scrollArea_3 = QScrollArea(self.LiveRightFrame)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy2.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy2)
        self.scrollArea_3.setMinimumSize(QSize(200, 0))
        self.scrollArea_3.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 200, 92))
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.typedinfolabel = QLabelThemed(self.scrollAreaWidgetContents)
        self.typedinfolabel.setObjectName(u"typedinfolabel")

        self.verticalLayout_39.addWidget(self.typedinfolabel)

        self.typedinputlabel = QLabelThemed(self.scrollAreaWidgetContents)
        self.typedinputlabel.setObjectName(u"typedinputlabel")
        self.typedinputlabel.setFont(font)

        self.verticalLayout_39.addWidget(self.typedinputlabel)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_44.addWidget(self.scrollArea_3)

        self.frame_6 = QFrame(self.LiveRightFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_6)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(6, 7, 0, 0)
        self.LiveLabel = QLabelThemed(self.frame_6)
        self.LiveLabel.setObjectName(u"LiveLabel")

        self.verticalLayout_25.addWidget(self.LiveLabel)

        self.CurrentWordLabel = QLabelThemed(self.frame_6)
        self.CurrentWordLabel.setObjectName(u"CurrentWordLabel")
        sizePolicy3.setHeightForWidth(self.CurrentWordLabel.sizePolicy().hasHeightForWidth())
        self.CurrentWordLabel.setSizePolicy(sizePolicy3)
        self.CurrentWordLabel.setFont(font)

        self.verticalLayout_25.addWidget(self.CurrentWordLabel)


        self.verticalLayout_44.addWidget(self.frame_6, 0, Qt.AlignVCenter)

        self.ScoreFrame = QFrame(self.LiveRightFrame)
        self.ScoreFrame.setObjectName(u"ScoreFrame")
        self.ScoreFrame.setFrameShape(QFrame.StyledPanel)
        self.ScoreFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.ScoreFrame)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.ScoreInfoLabel = QLabelThemed(self.ScoreFrame)
        self.ScoreInfoLabel.setObjectName(u"ScoreInfoLabel")

        self.verticalLayout_48.addWidget(self.ScoreInfoLabel)

        self.ScoreLabel = QLabelThemed(self.ScoreFrame)
        self.ScoreLabel.setObjectName(u"ScoreLabel")

        self.verticalLayout_48.addWidget(self.ScoreLabel)


        self.verticalLayout_44.addWidget(self.ScoreFrame, 0, Qt.AlignVCenter)

        self.frame_8 = QFrame(self.LiveRightFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.ToggleCamera = QPushButtonThemed(self.frame_8)
        self.ToggleCamera.setObjectName(u"ToggleCamera")
        icon15 = QIcon()
        icon15.addFile(u":/icons/png2svg/camera-On.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/icons/png2svg/Camera-Off.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ToggleCamera.setIcon(icon15)
        self.ToggleCamera.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.ToggleCamera)


        self.verticalLayout_44.addWidget(self.frame_8, 0, Qt.AlignTop)


        self.horizontalLayout_18.addWidget(self.LiveRightFrame, 0, Qt.AlignRight)


        self.verticalLayout_43.addWidget(self.LiveMainWidget)

        self.MainWidget.addWidget(self.Live_pg)

        self.verticalLayout_16.addWidget(self.MainWidget)


        self.horizontalLayout.addWidget(self.Main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.OptionsWidget.setCurrentIndex(0)
        self.AccountNavWidget.setCurrentIndex(1)
        self.AccountCreationWidget.setCurrentIndex(1)
        self.MainWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.MenuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuButton.setText("")
#if QT_CONFIG(tooltip)
        self.HomeButton.setToolTip(QCoreApplication.translate("MainWindow", u"To Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.ProfileButton.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.ProfileButton.setText(QCoreApplication.translate("MainWindow", u"My Profile", None))
#if QT_CONFIG(tooltip)
        self.LiveButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Live Translation- SHORTCUT</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LiveButton.setText(QCoreApplication.translate("MainWindow", u"Live", None))
#if QT_CONFIG(tooltip)
        self.SettingsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.MinimiseButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimise", None))
#endif // QT_CONFIG(tooltip)
        self.MinimiseButton.setText(QCoreApplication.translate("MainWindow", u"Minimise", None))
#if QT_CONFIG(tooltip)
        self.ExitButton.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.ExitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.Sidemenulabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Account</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.ExitSideMenu.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Close Account Menu</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ExitSideMenu.setText("")
        self.welcomelabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Welcome Back</span></p></body></html>", None))
        self.detailstologinlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Enter details to Login</span></p></body></html>", None))
        self.notregisteredlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Not registered?</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Click below to register.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toSignupbutton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">To Signup</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toSignupbutton.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.welcomelabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Welcome !!</span></p></body></html>", None))
        self.detailstosignuplabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Enter details to Sign Up</span></p></body></html>", None))
        self.alreadyaccountlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Already have an Account?</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Click below to Login</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toLoginbutton.setToolTip(QCoreApplication.translate("MainWindow", u"To login", None))
#endif // QT_CONFIG(tooltip)
        self.toLoginbutton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Login</span></p></body></html>", None))
        self.UsernameLoginEdit.setText("")
        self.UsernameLoginEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.PassLoginEdit.setInputMask("")
        self.PassLoginEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.forgotpasslabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://www.google.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Forgot your password?</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Login_Button.setToolTip(QCoreApplication.translate("MainWindow", u"Log In", None))
#endif // QT_CONFIG(tooltip)
        self.Login_Button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.SignUplabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Sign Up</span></p></body></html>", None))
        self.UsernameSignupEdit.setText("")
        self.UsernameSignupEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.PassSignupEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.ConfirmPassEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.Strengthmeter.setFormat(QCoreApplication.translate("MainWindow", u"Strength:", None))
#if QT_CONFIG(tooltip)
        self.SignUpbutton.setToolTip(QCoreApplication.translate("MainWindow", u"Sign Up", None))
#endif // QT_CONFIG(tooltip)
        self.SignUpbutton.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
#if QT_CONFIG(tooltip)
        self.LogoutButton.setToolTip(QCoreApplication.translate("MainWindow", u"LogOut", None))
#endif // QT_CONFIG(tooltip)
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.LoggedInLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Logged in as:</span></p></body></html>", None))
        self.usernameLoggedinlabel.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_9.setText("")
        self.CameraSettingComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Main Camera", None))

        self.CameraSettingComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Main Camera", None))
        self.CameraSettingComboBox.setPlaceholderText("")
        self.CameraRescan.setText(QCoreApplication.translate("MainWindow", u"Rescan for Cameras", None))
#if QT_CONFIG(tooltip)
        self.NotificationsWidget.setToolTip(QCoreApplication.translate("MainWindow", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.iconNot.setText("")
        self.labelNot.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Notifications:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.AcknowledgeNotifications.setToolTip(QCoreApplication.translate("MainWindow", u"Acknowledge all notifications", None))
#endif // QT_CONFIG(tooltip)
        self.AcknowledgeNotifications.setText(QCoreApplication.translate("MainWindow", u"Acknowledge All", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; text-decoration: underline;\">| Translator</span></p></body></html>", None))
        self.livecameradisplay.setText("")
        self.livelabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Live</span></p></body></html>", None))
        self.LiveTranDescription.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.LiveTranslationBottom.setToolTip(QCoreApplication.translate("MainWindow", u"Open Live", None))
#endif // QT_CONFIG(tooltip)
        self.StartLiveTranslationbutton.setText(QCoreApplication.translate("MainWindow", u"Open ", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Spelling </span></p><p><span style=\" font-size:16pt; font-weight:700;\">       Bee</span></p></body></html>", None))
        self.BeeTranDescription.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.SpellingBeenotificationlabel.setText("")
        self.SpellingBeeWordEntry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Word for bee", None))
#if QT_CONFIG(tooltip)
        self.StartSpellingBeeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Start Spelling Bee", None))
#endif // QT_CONFIG(tooltip)
        self.StartSpellingBeeButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_8.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Catalogue</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.TranCatBottomFrame.setToolTip(QCoreApplication.translate("MainWindow", u"Open Catalogue", None))
#endif // QT_CONFIG(tooltip)
        self.OpenCatalogueButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.CatalogueMenuLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; text-decoration: underline;\">| Catalogue</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CatalogueToTranslatorButton.setToolTip(QCoreApplication.translate("MainWindow", u"Back to Translator", None))
#endif // QT_CONFIG(tooltip)
        self.CatalogueToTranslatorButton.setText("")
        self.SearchIconLabel.setText("")
#if QT_CONFIG(tooltip)
        self.CatalogueSearchBar.setToolTip(QCoreApplication.translate("MainWindow", u"Search Words", None))
#endif // QT_CONFIG(tooltip)
        self.categorySearchLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Category:</span></p></body></html>", None))
        self.CatalogueCategoryselector.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))

#if QT_CONFIG(tooltip)
        self.CatalogueCategoryselector.setToolTip(QCoreApplication.translate("MainWindow", u"Search by Category", None))
#endif // QT_CONFIG(tooltip)
        self.CatalogueCategoryselector.setCurrentText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; text-decoration: underline;\">| Overview:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.OverviewToCatalogueButton.setToolTip(QCoreApplication.translate("MainWindow", u"Back to Catalogue", None))
#endif // QT_CONFIG(tooltip)
        self.OverviewToCatalogueButton.setText("")
        self.OverviewWordLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Word:</span></p></body></html>", None))
        self.WordOverviewlabel.setText("")
        self.OverviewCategoryLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Category</span></p></body></html>", None))
        self.CategoryOverviewLabel.setText("")
        self.OverviewNoAttemptsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Number of </span></p><p><span style=\" font-size:12pt; font-weight:700;\">Attempts:</span></p></body></html>", None))
        self.NoAttemptsOverviewLabel.setText("")
        self.DurationWatchedlabel.setText("")
        self.Vidlengthlabel.setText("")
#if QT_CONFIG(tooltip)
        self.PlayVideoButton.setToolTip(QCoreApplication.translate("MainWindow", u"Start Video", None))
#endif // QT_CONFIG(tooltip)
        self.PlayVideoButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Press Play to start the video", None))
        self.StartSigningButton.setText(QCoreApplication.translate("MainWindow", u"Sign It", None))
        self.Livetoplabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">| Live: </span></p></body></html>", None))
        self.LiveModeLabel.setText("")
        self.CameraStatus.setText("")
        self.LiveFootageLabel.setText("")
        self.LivePredictionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Prediction:</span></p></body></html>", None))
        self.predictionlabel.setText("")
        self.LiveAddtoTypedButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.LiveContinueButton.setText(QCoreApplication.translate("MainWindow", u"Ready?", None))
#if QT_CONFIG(tooltip)
        self.LiveToTranslatorButton.setToolTip(QCoreApplication.translate("MainWindow", u"To Translator", None))
#endif // QT_CONFIG(tooltip)
        self.LiveToTranslatorButton.setText("")
        self.typedinfolabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Typed:</span></p></body></html>", None))
        self.typedinputlabel.setText("")
        self.LiveLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Word:</span></p></body></html>", None))
        self.CurrentWordLabel.setText("")
        self.ScoreInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Score</span></p></body></html>", None))
        self.ScoreLabel.setText("")
        self.ToggleCamera.setText(QCoreApplication.translate("MainWindow", u"Turn Camera On", None))
    # retranslateUi


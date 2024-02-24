from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTimer, QUrl, Qt, Signal, QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget, QLabel, QPushButton)

class Notification:
    def __init__(cls, message, priority=0, notification_type="info"):
        cls.message = message
        cls.priority = priority
        cls.type = notification_type

class NotificationHandler():
    _existingNotifications = []
    notification_queue = []

    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance

    @classmethod
    def createNotification(cls,notification):
        frame = QFrame(cls.UI.Notifications_Panel)
        frame.setObjectName(u"frame")
        frame.setGeometry(QRect(110, 230, 250, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
        frame.setSizePolicy(sizePolicy)
        frame.setMinimumSize(QSize(300, 50))
        frame.setMaximumSize(QSize(350, 50))
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        cls.UI.Notifications_Panel.layout().addWidget(frame)
        horizontalLayout = QHBoxLayout(frame)
        horizontalLayout.setSpacing(14)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(0, 0, 0, 0)

        notificationiconpriority = QLabel(frame)
        notificationiconpriority.setObjectName(u"notificationiconpriority")
        if (notification.type=="warning"):
            errorpixmap = QPixmap(u"/qss/icons/png2svg/warning-icon.svg")
            notificationiconpriority.setPixmap(errorpixmap)
        else:
            infopixmap = QPixmap(u"/qss/icons/png2svg/info-icon.svg")
            notificationiconpriority.setPixmap(infopixmap)

        horizontalLayout.addWidget(notificationiconpriority)

        notification_label = QLabel(frame)
        notification_label.setObjectName(u"notification_label")
        notification_label.setWordWrap(True)
        notification_label.setText(notification.message)
        horizontalLayout.addWidget(notification_label)

        AcknowledgeNotificationbutton = QPushButton(frame)
        AcknowledgeNotificationbutton.setObjectName(u"AcknowledgeNotificationbutton")
        sizePolicy.setHeightForWidth(AcknowledgeNotificationbutton.sizePolicy().hasHeightForWidth())
        AcknowledgeNotificationbutton.setSizePolicy(sizePolicy)
        AcknowledgeNotificationbutton.setText("Acknowledge")
        AcknowledgeNotificationbutton.clicked.connect(lambda: cls.Delete_Notification(notification))

        horizontalLayout.addWidget(AcknowledgeNotificationbutton)
        cls._existingNotifications.append(frame)

    @classmethod
    def NotiCreator(cls):
        cls.clear_notifications()
        for notification in cls.notification_queue:
            cls.createNotification(notification)

    @classmethod
    def Queue_Notification(cls, notification):
        cls.notification_queue.append(notification)
        cls.notification_queue.sort(key=lambda n: (n.priority, n.type))
        cls.NotiCreator()

    @classmethod
    def Delete_Notification(cls,notification):
        cls.notification_queue.remove(notification)
        cls.NotiCreator()

    @classmethod
    def Dequeue_All_Notification(cls):
        if cls.notification_queue:
            cls.notification_queue.pop(0)
            cls.Dequeue_All_Notification()
        else:
            cls.NotiCreator()

    @classmethod
    def clear_notifications(cls):
        for frame in cls._existingNotifications:
                frame.setParent(None)
                frame.deleteLater()
        cls._existingNotifications =[]

    @classmethod
    def trigger_notification(cls, message, priority, type):
        notification = Notification(message, priority, type)
        cls.Queue_Notification(notification)
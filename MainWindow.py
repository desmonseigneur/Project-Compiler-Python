from PyQt6 import QtCore, QtGui, QtWidgets  # Retain only relevant imports
from PyQt6.QtCore import QDate  # QDate is used in the code
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime  # Required for date handling
import os  # For file system operations
import shutil  # For file copying
import sys
from ProjectsList import Ui_Project_Window

class Ui_Main_Window(object):
    def __init__(self):
        self.project_window = None  # To hold the instance of the project window if opened

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.setFixedSize(380, 670)  # Fix the size of the window
        Main_Window.setWindowFlags(Main_Window.windowFlags() & ~QtCore.Qt.WindowType.WindowMaximizeButtonHint)  # Remove maximize button
        Main_Window.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        bg_image_path = Ui_Main_Window.resource_path("BGP.jpg")
        Main_Window.setStyleSheet(f"""
               QMainWindow {{
                   background-image: url("{bg_image_path.replace('\\', '/')}");
                   background-repeat: no-repeat;
                   background-position: center;
                   background-size: cover;
               }}
           """)
        self.WM_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.WM_lb.setGeometry(QtCore.QRect(3, 2, 150, 20))
        self.WM_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.WM_lb.setObjectName("WM_lb")
        self.Enc_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Enc_lb.setGeometry(QtCore.QRect(148, 463, 200, 16))
        self.Enc_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Enc_lb.setObjectName("Enc_lb")
        self.Title_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Title_lb.setGeometry(QtCore.QRect(54, 54, 200, 25)) #104,
        self.Title_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Title_lb.setObjectName("Title_lb")
        self.Loc_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Loc_lb.setGeometry(QtCore.QRect(145, 85, 200, 16)) #41,
        self.Loc_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Loc_lb.setObjectName("Loc_lb")
        self.ProjCoord_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.ProjCoord_lb.setGeometry(QtCore.QRect(60, 112, 200, 16)) #102,
        self.ProjCoord_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ProjCoord_lb.setObjectName("ProjCoord_lb")
        self.Cont_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Cont_lb.setGeometry(QtCore.QRect(128, 139, 200, 16)) #43,
        self.Cont_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Cont_lb.setObjectName("Cont_lb")
        self.SOF_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.SOF_lb.setGeometry(QtCore.QRect(96, 166, 200, 16)) #96,
        self.SOF_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.SOF_lb.setObjectName("SOF_lb")
        self.TC_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.TC_lb.setGeometry(QtCore.QRect(147, 193, 200, 16)) #67,
        self.TC_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.TC_lb.setObjectName("TC_lb")
        self.AB_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.AB_lb.setGeometry(QtCore.QRect(178, 220, 200, 16)) #95,
        self.AB_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.AB_lb.setObjectName("AB_lb")
        self.DON_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.DON_lb.setGeometry(QtCore.QRect(87, 247, 200, 16)) #53,
        self.DON_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.DON_lb.setObjectName("DON_lb")
        self.DS_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.DS_lb.setGeometry(QtCore.QRect(115, 274, 200, 16)) #70,
        self.DS_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.DS_lb.setObjectName("DS_lb")
        self.DTC_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.DTC_lb.setGeometry(QtCore.QRect(10, 297, 210, 25)) #81,
        self.DTC_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.DTC_lb.setObjectName("DTC_lb")
        self.CD_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.CD_lb.setGeometry(QtCore.QRect(11, 328, 210, 16)) #7,
        self.CD_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.CD_lb.setObjectName("CD_lb")
        self.Ext_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Ext_lb.setGeometry(QtCore.QRect(71, 355, 150, 16)) #35,
        self.Ext_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Ext_lb.setObjectName("Ext_lb")
        self.ProjStat_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.ProjStat_lb.setGeometry(QtCore.QRect(75, 378, 200, 25)) #50,
        self.ProjStat_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ProjStat_lb.setObjectName("ProjStat_lb")
        self.TCI_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.TCI_lb.setGeometry(QtCore.QRect(7, 409, 220, 16)) #54,
        self.TCI_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.TCI_lb.setObjectName("TCI_lb")
        self.ID_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.ID_lb.setGeometry(QtCore.QRect(42, 432, 200, 25))
        self.ID_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ID_lb.setObjectName("ID_lb")
        self.Photos_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Photos_lb.setGeometry(QtCore.QRect(157, 490, 100, 16))
        self.Photos_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Photos_lb.setObjectName("Photos_lb")
        self.Documents_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Documents_lb.setGeometry(QtCore.QRect(124, 519, 100, 16))
        self.Documents_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Documents_lb.setObjectName("Documents_lb")
        self.Remarks_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.Remarks_lb.setGeometry(QtCore.QRect(145, 550, 100, 16))
        self.Remarks_lb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Remarks_lb.setObjectName("Remarks_lb")
        self.ProjectsList_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ProjectsList_btn.setGeometry(QtCore.QRect(275, 6, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ProjectsList_btn.setFont(font)
        self.ProjectsList_btn.setObjectName("ProjectsList_btn")
        self.ProjectsList_btn.clicked.connect(self.show_project_window)
        self.Upload_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Upload_btn.setGeometry(QtCore.QRect(215, 490, 75, 24))
        self.Upload_btn.setObjectName("Upload_btn")
        self.Upload_btn.clicked.connect(self.upload_images)
        self.UploadDoc_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.UploadDoc_btn.setGeometry(QtCore.QRect(215, 519, 75, 24))
        self.UploadDoc_btn.setObjectName("UploadDoc_btn")
        self.UploadDoc_btn.clicked.connect(self.upload_documents)
        self.Open_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Open_btn.setGeometry(QtCore.QRect(290, 490, 75, 24))
        self.Open_btn.setObjectName("Open_btn")
        self.Open_btn.clicked.connect(self.open_project_folder)
        self.OpenDoc_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OpenDoc_btn.setGeometry(QtCore.QRect(290, 519, 75, 24))
        self.OpenDoc_btn.setObjectName("OpenDoc_btn")
        self.OpenDoc_btn.clicked.connect(self.open_document_folder)
        self.ClearAll_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ClearAll_btn.setGeometry(QtCore.QRect(170, 634, 101, 31))
        self.ClearAll_btn.clicked.connect(self.clear_all_fields)  # Connect the clear button to the handler
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ClearAll_btn.setFont(font)
        self.ClearAll_btn.setObjectName("ClearAll_btn")
        self.Submit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Submit_btn.setGeometry(QtCore.QRect(275, 634, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Submit_btn.setFont(font)
        self.Submit_btn.setObjectName("Submit_btn")
        self.Submit_btn.clicked.connect(self.submit_data)  # Connect the submit button to the handler
        self.Edit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Edit_btn.setGeometry(QtCore.QRect(275, 634, 101, 31))  # Same position and size as Submit_btn
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Edit_btn.setFont(font)
        self.Edit_btn.setObjectName("Edit_btn")
        self.Edit_btn.clicked.connect(self.save_edit_data)
        self.Edit_btn.setVisible(False)
        self.CancelEdit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CancelEdit_btn.setGeometry(QtCore.QRect(170, 634, 101, 31))  # Aligned beside ClearAll_btn
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CancelEdit_btn.setFont(font)
        self.CancelEdit_btn.setObjectName("CancelEdit_btn")
        self.CancelEdit_btn.clicked.connect(self.cancel_edit)
        self.CancelEdit_btn.setVisible(False)
        self.Id_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Id_Line.setGeometry(QtCore.QRect(1, 1, 1, 1))
        self.Id_Line.setObjectName("Id_Line")
        self.Enc_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Enc_Line.setGeometry(QtCore.QRect(215, 463, 161, 21)) #
        self.Enc_Line.setObjectName("Enc_Line")
        self.Title_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Title_Line.setGeometry(QtCore.QRect(215, 58, 161, 21)) #
        self.Title_Line.setObjectName("Title_Line")
        self.Loc_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Loc_cb.setGeometry(QtCore.QRect(215, 85, 161, 21)) #
        self.Loc_cb.setEditable(True)
        self.Loc_cb.setCurrentText("")
        self.Loc_cb.setMaxVisibleItems(10)
        self.Loc_cb.setMaxCount(64)
        self.Loc_cb.setObjectName("Loc_cb")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.Loc_cb.addItem("")
        self.ProjCoord_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.ProjCoord_Line.setGeometry(QtCore.QRect(215, 112, 161, 21)) #
        self.ProjCoord_Line.setObjectName("ProjCoord_Line")
        self.Cont_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Cont_Line.setGeometry(QtCore.QRect(215, 139, 161, 21)) #
        self.Cont_Line.setObjectName("Cont_Line")
        self.SOF_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SOF_cb.setGeometry(QtCore.QRect(215, 166, 161, 21))  #
        self.SOF_cb.setObjectName("SOF_cb")
        self.SOF_cb.setEditable(False)
        self.SOF_cb.addItems([
            "20% Development Fund", "By Admin", "Emergency/Disaster Fund",
            "For Funding", "General Fund", "IRA", "LSB", "Municipal Fund"
        ])
        self.TC_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TC_Line.setGeometry(QtCore.QRect(215, 193, 161, 21)) #
        self.TC_Line.setObjectName("TC_Line")
        self.TC_Line.textChanged.connect(lambda: self.format_line_text(self.TC_Line))
        self.AB_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.AB_Line.setGeometry(QtCore.QRect(215, 220, 161, 21)) #
        self.AB_Line.setObjectName("AB_Line")
        self.AB_Line.textChanged.connect(lambda: self.format_line_text(self.AB_Line))
        self.DON_Date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.DON_Date.setGeometry(QtCore.QRect(215, 247, 161, 21)) #215, 247
        self.DON_Date.setCurrentSection(QtWidgets.QDateTimeEdit.Section.MonthSection)
        self.DON_Date.setCalendarPopup(True)
        self.DON_Date.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.DON_Date.setDate(QDate.currentDate())
        self.DON_Date.setObjectName("DON_Date")
        self.DS_Date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.DS_Date.setGeometry(QtCore.QRect(215, 274, 161, 21)) #
        self.DS_Date.setCalendarPopup(True)
        self.DS_Date.setCurrentSectionIndex(0)
        self.DS_Date.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.DS_Date.setDate(QDate.currentDate())
        self.DS_Date.setObjectName("DS_Date")
        self.DTC_Date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.DTC_Date.setGeometry(QtCore.QRect(215, 301, 161, 21)) #
        self.DTC_Date.setCalendarPopup(True)
        self.DTC_Date.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.DTC_Date.setDate(QDate.currentDate())
        self.DTC_Date.setObjectName("DTC_Date")
        self.CD_sb = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.CD_sb.setGeometry(QtCore.QRect(215, 328, 49, 21)) #
        self.CD_sb.setMaximum(3650)
        self.CD_sb.setProperty("value", 0)
        self.CD_sb.setObjectName("CD_sb")
        self.CD_sb.editingFinished.connect(self.update_dtc_date_from_cd)
        self.Ext_sb = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.Ext_sb.setGeometry(QtCore.QRect(215, 355, 49, 21)) #
        self.Ext_sb.setMaximum(3650)
        self.Ext_sb.setProperty("value", 0)
        self.Ext_sb.setObjectName("Ext_sb")
        self.ProjStat_sb = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.ProjStat_sb.setGeometry(QtCore.QRect(215, 382, 49, 21)) #
        self.ProjStat_sb.setMaximum(100)
        self.ProjStat_sb.setProperty("value", 0)
        self.ProjStat_sb.setObjectName("ProjStat_sb")
        self.TCI_Line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.TCI_Line.setGeometry(QtCore.QRect(215, 409, 161, 21)) #
        self.TCI_Line.setObjectName("TCI_Line")
        self.TCI_Line.textChanged.connect(lambda: self.format_line_text(self.TCI_Line))
        self.ID_Date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.ID_Date.setGeometry(QtCore.QRect(215, 436, 161, 21)) #
        self.ID_Date.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.ID_Date.setDate(QDate.currentDate())
        self.ID_Date.setObjectName("ID_Date")
        self.ID_Date.setCalendarPopup(True)
        self.Remarks_Line = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.Remarks_Line.setGeometry(QtCore.QRect(215, 550, 161, 75))
        self.Remarks_Line.setObjectName("plainTextEdit")
        Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Window)
        self.Loc_cb.setCurrentIndex(-1)
        self.SOF_cb.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)
        self.apply_font_border(self.Enc_lb, "Encoder:", font_size=12)
        self.apply_font_border(self.Title_lb, "Project/Activity Title:", font_size=12)
        self.apply_font_border(self.Loc_lb, "Location:", font_size=12)
        self.apply_font_border(self.ProjCoord_lb, "Project Coordinator:", font_size=12)
        self.apply_font_border(self.Cont_lb, "Contractor:", font_size=12)
        self.apply_font_border(self.SOF_lb, "Source of Fund:", font_size=12)
        self.apply_font_border(self.TC_lb, "Bid Cost:", font_size=12)
        self.apply_font_border(self.AB_lb, "ABC:", font_size=12)
        self.apply_font_border(self.DON_lb, "Notice of Award:", font_size=12)
        self.apply_font_border(self.DS_lb, "Date Started:", font_size=12)
        self.apply_font_border(self.DTC_lb, "Date of Target Completion:", font_size=12)
        self.apply_font_border(self.CD_lb, "Duration of Calendar Days:", font_size=12)
        self.apply_font_border(self.Ext_lb, "No. of Extension/s:", font_size=12)
        self.apply_font_border(self.ProjStat_lb, "Project Status (%):", font_size=12)
        self.apply_font_border(self.TCI_lb, "Total Cost Incurred to Date:", font_size=12)
        self.apply_font_border(self.ID_lb, "Latest Inspection Date:", font_size=12)
        self.apply_font_border(self.Photos_lb, "Photos:", font_size=12)
        self.apply_font_border(self.Documents_lb, "Documents:", font_size=12)
        self.apply_font_border(self.Remarks_lb, "Remarks:", font_size=12)

        self.setupDatabase()

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "Municipal\'s Project Compiler"))
        self.WM_lb.setText(_translate("Main_Window", "Developed by: J. Masunsong"))
        self.Enc_lb.setText(_translate("Main_Window", "Encoder:"))
        self.Title_lb.setText(_translate("Main_Window", "Project/Activity Title:"))
        self.Loc_lb.setText(_translate("Main_Window", "Location:"))
        self.ProjCoord_lb.setText(_translate("Main_Window", "Project Coordinator:"))
        self.Cont_lb.setText(_translate("Main_Window", "Contrator:"))
        self.SOF_lb.setText(_translate("Main_Window", "Source of Fund:"))
        self.TC_lb.setText(_translate("Main_Window", "Bid Cost:"))
        self.AB_lb.setText(_translate("Main_Window", "ABC:"))
        self.DON_lb.setText(_translate("Main_Window", "Notice of Award:"))
        self.DS_lb.setText(_translate("Main_Window", "Date Started:"))
        self.DTC_lb.setText(_translate("Main_Window", "Date of Target Completion:"))
        self.CD_lb.setText(_translate("Main_Window", "Duration of Calendar Days:"))
        self.Ext_lb.setText(_translate("Main_Window", "No. of Extension/s:"))
        self.ProjStat_lb.setText(_translate("Main_Window", "Project Status (%):"))
        self.TCI_lb.setText(_translate("Main_Window", "Total Cost Incurred to Date:"))
        self.ID_lb.setText(_translate("Main_Window", "Latest Inspection Date:"))
        self.Photos_lb.setText(_translate("Main_Window", "Photos:"))
        self.Documents_lb.setText(_translate("Main_Window", "Documents:"))
        self.Remarks_lb.setText(_translate("Main_Window", "Remarks:"))
        self.ProjectsList_btn.setText(_translate("Main_Window", "Projects List"))
        self.Upload_btn.setText(_translate("Main_Window", "Upload"))
        self.UploadDoc_btn.setText(_translate("Main_Window", "Upload"))
        self.Open_btn.setText(_translate("Main_Window", "Open"))
        self.OpenDoc_btn.setText(_translate("Main_Window", "Open"))
        self.ClearAll_btn.setText(_translate("Main_Window", "Clear All"))
        self.Submit_btn.setText(_translate("Main_Window", "Submit"))
        self.Edit_btn.setText(_translate("Main_Window", "Edit"))
        self.CancelEdit_btn.setText(_translate("Main_Window", "Cancel Edit"))
        self.Loc_cb.setItemText(0, _translate("Main_Window", "ACACIA"))
        self.Loc_cb.setItemText(1, _translate("Main_Window", "ADLAS"))
        self.Loc_cb.setItemText(2, _translate("Main_Window", "ANAHAW 1"))
        self.Loc_cb.setItemText(3, _translate("Main_Window", "ANAHAW 2"))
        self.Loc_cb.setItemText(4, _translate("Main_Window", "BALITE 1"))
        self.Loc_cb.setItemText(5, _translate("Main_Window", "BALITE 2"))
        self.Loc_cb.setItemText(6, _translate("Main_Window", "BALUBAD"))
        self.Loc_cb.setItemText(7, _translate("Main_Window", "BANABA"))
        self.Loc_cb.setItemText(8, _translate("Main_Window", "BATAS"))
        self.Loc_cb.setItemText(9, _translate("Main_Window", "BIGA 1"))
        self.Loc_cb.setItemText(10, _translate("Main_Window", "BIGA 2"))
        self.Loc_cb.setItemText(11, _translate("Main_Window", "BILUSO"))
        self.Loc_cb.setItemText(12, _translate("Main_Window", "BUCAL"))
        self.Loc_cb.setItemText(13, _translate("Main_Window", "BUHO"))
        self.Loc_cb.setItemText(14, _translate("Main_Window", "BULIHAN"))
        self.Loc_cb.setItemText(15, _translate("Main_Window", "CABANGAAN"))
        self.Loc_cb.setItemText(16, _translate("Main_Window", "CARMEN"))
        self.Loc_cb.setItemText(17, _translate("Main_Window", "HOYO"))
        self.Loc_cb.setItemText(18, _translate("Main_Window", "HUKAY"))
        self.Loc_cb.setItemText(19, _translate("Main_Window", "IBA"))
        self.Loc_cb.setItemText(20, _translate("Main_Window", "INCHICAN"))
        self.Loc_cb.setItemText(21, _translate("Main_Window", "IPIL 1"))
        self.Loc_cb.setItemText(22, _translate("Main_Window", "IPIIL 2"))
        self.Loc_cb.setItemText(23, _translate("Main_Window", "KALUBKOB"))
        self.Loc_cb.setItemText(24, _translate("Main_Window", "KAONG"))
        self.Loc_cb.setItemText(25, _translate("Main_Window", "LALAAN 1"))
        self.Loc_cb.setItemText(26, _translate("Main_Window", "LALAAN 2"))
        self.Loc_cb.setItemText(27, _translate("Main_Window", "LITLIT"))
        self.Loc_cb.setItemText(28, _translate("Main_Window", "LUCSUHIN"))
        self.Loc_cb.setItemText(29, _translate("Main_Window", "LUMIL"))
        self.Loc_cb.setItemText(30, _translate("Main_Window", "MAGUYAM"))
        self.Loc_cb.setItemText(31, _translate("Main_Window", "MALABAG"))
        self.Loc_cb.setItemText(32, _translate("Main_Window", "MALAKING TATIAO"))
        self.Loc_cb.setItemText(33, _translate("Main_Window", "MATAAS NA BUROL"))
        self.Loc_cb.setItemText(34, _translate("Main_Window", "MUNTING ILOG"))
        self.Loc_cb.setItemText(35, _translate("Main_Window", "NARRA 1"))
        self.Loc_cb.setItemText(36, _translate("Main_Window", "NARRA 2"))
        self.Loc_cb.setItemText(37, _translate("Main_Window", "NARRA 3"))
        self.Loc_cb.setItemText(38, _translate("Main_Window", "PALIGAWAN"))
        self.Loc_cb.setItemText(39, _translate("Main_Window", "PASONG LANGKA"))
        self.Loc_cb.setItemText(40, _translate("Main_Window", "POBLACION 1"))
        self.Loc_cb.setItemText(41, _translate("Main_Window", "POBLACION 2"))
        self.Loc_cb.setItemText(42, _translate("Main_Window", "POBLACION 3"))
        self.Loc_cb.setItemText(43, _translate("Main_Window", "POBLACION 4"))
        self.Loc_cb.setItemText(44, _translate("Main_Window", "POBLACION 5"))
        self.Loc_cb.setItemText(45, _translate("Main_Window", "POOK 1"))
        self.Loc_cb.setItemText(46, _translate("Main_Window", "POOK 2"))
        self.Loc_cb.setItemText(47, _translate("Main_Window", "PULONG BUNGA"))
        self.Loc_cb.setItemText(48, _translate("Main_Window", "PULONG SAGING"))
        self.Loc_cb.setItemText(49, _translate("Main_Window", "PUTING KAHOY"))
        self.Loc_cb.setItemText(50, _translate("Main_Window", "SANTOL"))
        self.Loc_cb.setItemText(51, _translate("Main_Window", "SABUTAN"))
        self.Loc_cb.setItemText(52, _translate("Main_Window", "SAN MIGUEL 1"))
        self.Loc_cb.setItemText(53, _translate("Main_Window", "SAN MIGUEL 2"))
        self.Loc_cb.setItemText(54, _translate("Main_Window", "SAN VICENTE 1"))
        self.Loc_cb.setItemText(55, _translate("Main_Window", "SAN VICENTE 2"))
        self.Loc_cb.setItemText(56, _translate("Main_Window", "TARTARIA"))
        self.Loc_cb.setItemText(57, _translate("Main_Window", "TIBIG"))
        self.Loc_cb.setItemText(58, _translate("Main_Window", "TOLEDO"))
        self.Loc_cb.setItemText(59, _translate("Main_Window", "TUBUAN 1"))
        self.Loc_cb.setItemText(60, _translate("Main_Window", "TUBUAN 2"))
        self.Loc_cb.setItemText(61, _translate("Main_Window", "TUBUAN 3"))
        self.Loc_cb.setItemText(62, _translate("Main_Window", "ULAT"))
        self.Loc_cb.setItemText(63, _translate("Main_Window", "YAKAL"))
        self.SOF_cb.setItemText(0, _translate("Main_Window", "20% Development Fund"))
        self.SOF_cb.setItemText(1, _translate("Main_Window", "By Admin"))
        self.SOF_cb.setItemText(2, _translate("Main_Window", "Emergency/Disaster Fund"))
        self.SOF_cb.setItemText(3, _translate("Main_Window", "For Funding"))
        self.SOF_cb.setItemText(4, _translate("Main_Window", "General Fund"))
        self.SOF_cb.setItemText(5, _translate("Main_Window", "IRA"))
        self.SOF_cb.setItemText(6, _translate("Main_Window", "LSB"))
        self.SOF_cb.setItemText(7, _translate("Main_Window", "Municipal Fund"))
        self.DON_Date.setDisplayFormat(_translate("Main_Window", "MMMM  dd  yyyy"))
        self.DS_Date.setDisplayFormat(_translate("Main_Window", "MMMM  dd  yyyy"))
        self.DTC_Date.setDisplayFormat(_translate("Main_Window", "MMMM  dd  yyyy"))
        self.ID_Date.setDisplayFormat(_translate("Main_Window", "MMMM  dd  yyyy"))

    @staticmethod
    def resource_path(relative_path):
        """ Get the absolute path to a resource, works for PyInstaller """
        try:
            base_path = sys._MEIPASS  # PyInstaller temporary directory
        except AttributeError:
            base_path = os.path.abspath(".")  # Fallback to current directory (for development)
        return os.path.join(base_path, relative_path)

    def apply_font_border(self, label, text, font_size=14, text_color="white", border_color="black"):
        """
        Apply a simulated font border by layering QLabel objects for a border-like effect.
        """
        font = QtGui.QFont()
        font.setPointSize(font_size)
        font.setBold(True)

        # Create the outline QLabel
        outline_label = QtWidgets.QLabel(parent=self.centralwidget)
        outline_label.setText(text)
        outline_label.setFont(font)
        outline_label.setStyleSheet(f"color: {border_color};")
        outline_label.setGeometry(label.geometry())  # Position it like the main label
        outline_label.move(label.x() - 1, label.y() - 1)  # Offset for top-left border
        outline_label.show()

        # Repeat for other edges of the border
        for dx, dy in [(1, -1), (-1, 1), (1, 1)]:
            shadow = QtWidgets.QLabel(parent=self.centralwidget)
            shadow.setText(text)
            shadow.setFont(font)
            shadow.setStyleSheet(f"color: {border_color};")
            shadow.setGeometry(label.geometry())
            shadow.move(label.x() + dx, label.y() + dy)  # Offset for emulating the edges
            shadow.show()

        # Original QLabel for the main text (on top of border layers)
        label.setText(text)
        label.setFont(font)
        label.setStyleSheet(f"color: {text_color};")
        label.raise_()
        label.show()

    def setupDatabase(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('192.168.141.214')
        self.db.setDatabaseName('dmedb')
        self.db.setUserName('appuser')
        self.db.setPassword('StrongPassword123!')
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, "Database Error", self.db.lastError().text())

    def show_message(self, title, message, message_type="info"):
        if message_type == "info":
            QMessageBox.information(None, title, message)
        elif message_type == "warning":
            QMessageBox.warning(None, title, message)
        elif message_type == "error":
            QMessageBox.critical(None, title, message)

    def show_project_window(self):
        if not self.project_window:
            self.project_window = QtWidgets.QMainWindow()
            self.ui = Ui_Project_Window()
            self.ui.setupUi(self.project_window)

            self.ui.row_data_signal.connect(self.populate_fields_from_row)
            print("Signal connected to populate_fields_from_row")  ######### DEBUGGER #########
            self.project_window.closeEvent = self.on_project_window_close

        self.project_window.show()

    def on_project_window_close(self, event):
        self.project_window = None
        event.accept()

    def update_dtc_date_from_cd(self):
        try:
            # Get the number of calendar days from CD_sb
            calendar_days = self.CD_sb.value()

            # Get the base date from DS_Date
            base_date = self.DS_Date.date()

            # Calculate the new target completion date
            new_date = base_date.addDays(calendar_days)

            # Update the DTC_Date field with the calculated date
            self.DTC_Date.setDate(new_date)

        except Exception as e:
            self.show_message("Error", f"Failed to update target completion date: {str(e)}", "error")

    def format_line_text(self, line_edit):
        text = line_edit.text().replace("Php.", "").replace(",", "").strip()
        if text.isdigit():
            formatted_text = "Php. {:,}".format(int(text))
            line_edit.blockSignals(True)
            line_edit.setText(formatted_text)
            line_edit.blockSignals(False)

    def clear_all_fields(self):
        self.Enc_Line.clear()
        self.Title_Line.clear()
        self.ProjCoord_Line.clear()
        self.Cont_Line.clear()
        self.TC_Line.clear()
        self.AB_Line.clear()
        self.TCI_Line.clear()
        self.Remarks_Line.clear()
        self.CD_sb.setValue(0)
        self.Ext_sb.setValue(0)
        self.ProjStat_sb.setValue(0)
        self.DON_Date.setDate(QDate.currentDate())
        self.DS_Date.setDate(QDate.currentDate())
        self.DTC_Date.setDate(QDate.currentDate())
        self.ID_Date.setDate(QDate.currentDate())

        # Clear QComboBox field and keep it functional
        self.SOF_cb.setCurrentIndex(-1)
        self.Loc_cb.setCurrentIndex(-1)
        self.Loc_cb.setEditText("")

    def get_shared_folder_path(self, folder_type="Pictures"):
        base_shared_folder_path = r"\\DESKTOP-AEI2HOG\Shared MPC Files"
        shared_folder_path = os.path.join(base_shared_folder_path, folder_type)
        if not os.path.exists(shared_folder_path):
            raise Exception(f"The shared folder '{shared_folder_path}' does not exist!")
        if not os.access(shared_folder_path, os.R_OK | os.W_OK):
            raise Exception(f"The shared folder '{shared_folder_path}' is not accessible! Please check permissions.")
        return shared_folder_path

    @staticmethod
    def get_unique_folder_path(base_path):
        if not os.path.exists(base_path):
            return base_path
        counter = 1
        unique_path = base_path
        while os.path.exists(unique_path):
            unique_path = f"{base_path} ({counter})"
            counter += 1
        return unique_path

    def get_fallback_folder(self, base_path):
        fallback_folder = os.path.join(os.environ["USERPROFILE"], "Fallback Storage")
        if not os.path.exists(fallback_folder):
            os.makedirs(fallback_folder)
        return fallback_folder

    @staticmethod
    def sanitize_string(input_string):
        return "".join(c for c in input_string if c not in r'\/:*?"<>|')

    def upload_images(self):
        project_title = self.Title_Line.text().strip()
        if not project_title:
            QMessageBox.warning(None, "Warning", "Please enter a Project/Activity Title before uploading!")
            return
        sanitized_title = self.sanitize_string(project_title)

        try:
            shared_pictures_path = self.get_shared_folder_path(folder_type="Pictures")
            output_folder = os.path.join(shared_pictures_path, sanitized_title)
            output_folder = self.get_unique_folder_path(output_folder)  # Reuse the helper method
            os.makedirs(output_folder)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            file_dialog.setNameFilters(["Image Files (*.jpg *.jpeg *.png)"])
            selected_files, _ = file_dialog.getOpenFileNames(self.centralwidget, "Select Images")
            if not selected_files:
                return
            for file_path in selected_files:
                try:
                    shutil.copy(file_path, output_folder)
                except Exception as e:
                    QMessageBox.critical(None, "Error", f"Could not copy file {file_path}: {str(e)}")
                    return
            QMessageBox.information(None, "Success", f"Images uploaded successfully to folder: {output_folder}")
        except Exception as e:
            error_message = f"Error in upload_images with title '{project_title}': {str(e)}"
            QMessageBox.critical(None, "Error", error_message)

    def upload_documents(self):
        project_title = self.Title_Line.text().strip()
        if not project_title:
            QMessageBox.warning(None, "Warning", "Please enter a Project/Activity Title before uploading!")
            return
        sanitized_title = self.sanitize_string(project_title)
        try:
            shared_folder_path = self.get_shared_folder_path(folder_type="Documents")
            folder_path = os.path.join(shared_folder_path, sanitized_title)
            folder_path = self.get_unique_folder_path(folder_path)  # Reuse the helper method
            os.makedirs(folder_path)

            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            file_dialog.setNameFilters(["All Files (*.*)"])
            selected_files, _ = file_dialog.getOpenFileNames(self.centralwidget, "Select Documents")

            if not selected_files:
                return

            excluded_extensions = {".png", ".gif", ".bmp", ".tiff", ".webp"}
            filtered_files = [
                file for file in selected_files
                if os.path.splitext(file)[1].lower() not in excluded_extensions
            ]

            if not filtered_files:
                QMessageBox.warning(None, "Warning", "No valid document files selected!")
                return

            for file_path in filtered_files:
                try:
                    shutil.copy(file_path, folder_path)
                except Exception as e:
                    QMessageBox.critical(None, "Error", f"Could not copy file {file_path}: {str(e)}")
                    return

            QMessageBox.information(None, "Success", f"Documents uploaded successfully to folder: {folder_path}")

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to upload documents: {str(e)}")

    def open_project_folder(self):
        project_title = self.Title_Line.text().strip()
        if not project_title:
            QMessageBox.warning(None, "Warning", "Please enter a Project/Activity Title first!")
            return
        sanitized_title = "".join(c for c in project_title if c not in r'\/:*?"<>|')
        possible_titles = [sanitized_title]
        folder_to_open = None
        local_pictures_path = os.path.join(os.environ.get("USERPROFILE", ""), "Pictures")
        for title in possible_titles:
            folder_path = os.path.join(local_pictures_path, title)
            if os.path.exists(folder_path):
                folder_to_open = folder_path
                break

        if not folder_to_open:
            try:
                shared_pictures_path = self.get_shared_folder_path()
                for title in possible_titles:
                    folder_path = os.path.join(shared_pictures_path, title)
                    if os.path.exists(folder_path):
                        folder_to_open = folder_path
                        break
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Could not resolve shared folder path: {str(e)}")
                return

        if not folder_to_open:
            QMessageBox.critical(None, "Error",
                                 f"No folder found locally or in the shared folders for: '{project_title}'.")
            return

        # Open the folder
        try:
            if os.name == "nt":  # Windows
                os.startfile(folder_to_open)
            elif os.name == "posix":  # macOS/Linux
                subprocess.Popen(["xdg-open", folder_to_open])
            else:
                QMessageBox.critical(None, "Error", "Unsupported operating system.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to open folder: {str(e)}")

    def open_document_folder(self):
        project_title = self.Title_Line.text().strip()
        if not project_title:
            QMessageBox.warning(None, "Warning", "Please enter a Project/Activity Title first!")
            return
        sanitized_title = "".join(c for c in project_title if c not in r'\/:*?"<>|')

        try:
            shared_folder_path = self.get_shared_folder_path(folder_type="Documents")
            folder_to_open = os.path.join(shared_folder_path, sanitized_title)
            if not os.path.exists(folder_to_open):
                QMessageBox.warning(None, "Error", f"No folder found in 'Documents' for: '{project_title}'.")
                return
            if os.name == "nt":  # For Windows systems
                os.startfile(folder_to_open)
            elif os.name == "posix":  # For macOS/Linux systems
                subprocess.Popen(["xdg-open", folder_to_open])
            else:
                QMessageBox.critical(None, "Error", "Unsupported operating system.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to open folder: {str(e)}")

    def submit_data(self):
        # Collect data from UI elements
        project_encoder = self.Enc_Line.text()
        project_title = self.Title_Line.text()
        project_location = self.Loc_cb.currentText()
        project_coordinator = self.ProjCoord_Line.text()
        project_contractor = self.Cont_Line.text()
        project_source = self.SOF_cb.currentText()

        # Extract only numeric values and remove the prefix ("Php.") from monetary fields
        project_totalcost = self.TC_Line.text().replace("Php.", "").replace(",", "").strip()
        project_budget = self.AB_Line.text().replace("Php.", "").replace(",", "").strip()
        project_incurred = self.TCI_Line.text().replace("Php.", "").replace(",", "").strip()

        # Date fields and other values
        date_notice = self.DON_Date.date().toString("yyyy-MM-dd")
        date_start = self.DS_Date.date().toString("yyyy-MM-dd")
        date_target = self.DTC_Date.date().toString("yyyy-MM-dd")
        date_days = self.CD_sb.value()
        date_extension = self.Ext_sb.value()
        project_status = self.ProjStat_sb.value()
        date_inspection = self.ID_Date.date().toString("yyyy-MM-dd")
        project_remarks = self.Remarks_Line.toPlainText()
        project_year = datetime.now().year  # Get the current year
        project_month = datetime.now().month  # Get the current month

        # Generate tracking number
        # Extract initials from 'Source of Fund'
        sof_initials = ''.join(word[0].upper() for word in project_source.split() if word[0].isalpha())

        # Placeholder for ID (it will be generated after the insert if auto-increment is used)
        tracking_number = f"{sof_initials}-{project_year}-{project_month:02d}-"  # ID will be appended later

        # Prepare the SQL query to insert the data and fetch the inserted ID
        query = QSqlQuery()
        query.prepare("""
                    INSERT INTO project_tb (
                        project_encoder, project_title, project_location, project_coordinator, 
                        project_contractor, project_source, project_totalcost, project_budget, 
                        date_notice, date_start, date_target, date_days, date_extension, 
                        project_status, project_incurred, date_inspection, project_remarks, project_year, tracking_number
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """)

        # Bind values to the query
        query.addBindValue(project_encoder)
        query.addBindValue(project_title)
        query.addBindValue(project_location)
        query.addBindValue(project_coordinator)
        query.addBindValue(project_contractor)
        query.addBindValue(project_source)
        query.addBindValue(project_totalcost)  # Only numeric part
        query.addBindValue(project_budget)  # Only numeric part
        query.addBindValue(date_notice)
        query.addBindValue(date_start)
        query.addBindValue(date_target)
        query.addBindValue(date_days)
        query.addBindValue(date_extension)
        query.addBindValue(project_status)
        query.addBindValue(project_incurred)  # Only numeric part
        query.addBindValue(date_inspection)
        query.addBindValue(project_remarks)
        query.addBindValue(project_year)
        query.addBindValue(tracking_number)  # Add placeholder for tracking number (to be updated later)

        # Execute the query and check for errors
        if query.exec():
            # Retrieve the auto-incremented ID of the inserted record
            last_inserted_id = query.lastInsertId()
            full_tracking_number = f"{tracking_number}{last_inserted_id}"

            # Update the tracking number in the database
            update_query = QSqlQuery()
            update_query.prepare("""
                UPDATE project_tb SET tracking_number = ? WHERE project_id = ?
            """)
            update_query.addBindValue(full_tracking_number)
            update_query.addBindValue(last_inserted_id)
            if not update_query.exec():
                QtWidgets.QMessageBox.critical(None, "Database Error", update_query.lastError().text())
            else:
                QtWidgets.QMessageBox.information(None, "Success",
                                                  f"Data submitted successfully! Tracking Number: {full_tracking_number}")
        else:
            QtWidgets.QMessageBox.critical(None, "Database Error", query.lastError().text())

        # Clear fields after submission
        self.clear_all_fields()

    def populate_fields_from_row(self, row_data):
        try:
            # Debugging print to check data being received
            print(f"Received row data: {row_data}")

            # Populate fields with safety checks for types and defaults
            self.Id_Line.setText(str(row_data.get("project_id", "")))
            self.Title_Line.setText(row_data.get("Project/Activity Title", "") or "")
            self.Loc_cb.setEditText(row_data.get("Location", "") or "")
            self.SOF_cb.setCurrentText(row_data.get("Source of Fund", "") or "")

            # Add "Php." prefix and format
            self.TC_Line.setText(
                f"Php. {float(row_data.get('Bid Cost', 0.00)):,}" if row_data.get("Bid Cost") else "Php. 0.00")
            self.AB_Line.setText(
                f"Php. {float(row_data.get('Approved Budget of Contract (ABC)', 0.00)):,}" if row_data.get(
                    "Approved Budget of Contract (ABC)") else "Php. 0.00")
            self.TCI_Line.setText(f"Php. {float(row_data.get('Total Cost Incurred to Date', 0.00)):,}" if row_data.get(
                "Total Cost Incurred to Date") else "Php. 0.00")

            # Handle Date Fields
            def safe_date(value):
                if isinstance(value, QDate):
                    return value
                elif isinstance(value, str):
                    return QDate.fromString(value, "yyyy-MM-dd") or QDate.currentDate()  # Handle string dates
                return QDate.currentDate()

            self.DON_Date.setDate(safe_date(row_data.get("Notice of Award")))
            self.DS_Date.setDate(safe_date(row_data.get("Date Started")))
            self.DTC_Date.setDate(safe_date(row_data.get("Target Completion Date")))
            self.ID_Date.setDate(safe_date(row_data.get("Latest Inspection Date")))
            self.CD_sb.setValue(int(row_data.get("Duration of Calendar Days", 0)))
            self.Ext_sb.setValue(int(row_data.get("No. of Extension", 0)))
            self.ProjStat_sb.setValue(int(row_data.get("Project Status (%)", 0)))
            self.Remarks_Line.setPlainText(row_data.get("Remarks", "") or "N/A")
            self.ProjCoord_Line.setText(row_data.get("Project Coordinator", "") or "")
            self.Cont_Line.setText(row_data.get("Contractor", "") or "")
            self.Enc_Line.setText(row_data.get("Encoder", "") or "")

            # Visually make fields non-editable
            non_editable_style = "background-color: lightgray; color: black;"
            non_editable_widgets = [
                self.Title_Line, self.Loc_cb, self.SOF_cb, self.TC_Line, self.AB_Line,
                self.DON_Date, self.DS_Date, self.DTC_Date, self.CD_sb, self.TCI_Line,
                self.ProjCoord_Line, self.Cont_Line, self.Enc_Line, self.Ext_sb, self.ProjStat_sb,
                self.ID_Date,
            ]

            # Apply read-only properties and styles
            for widget in non_editable_widgets:
                if isinstance(widget, QtWidgets.QLineEdit):
                    widget.setReadOnly(True)
                    widget.setStyleSheet(non_editable_style)
                elif isinstance(widget, QtWidgets.QComboBox):
                    widget.setEnabled(False)  # Disables interaction
                    widget.setStyleSheet(non_editable_style)
                elif isinstance(widget, QtWidgets.QDateEdit):
                    widget.setReadOnly(True)
                    widget.setStyleSheet(non_editable_style)
                elif isinstance(widget, QtWidgets.QSpinBox):
                    widget.setReadOnly(True)
                    widget.setStyleSheet(non_editable_style)

            # Toggle visibility of buttons (if necessary)
            self.Submit_btn.setVisible(False)
            self.Edit_btn.setVisible(True)
            self.CancelEdit_btn.setVisible(True)
            self.ClearAll_btn.setVisible(False)

        except Exception as e:
            print(f"Error populating fields: {e}")
            QtWidgets.QMessageBox.critical(None, "Error", f"Error populating fields: {str(e)}")

    def enable_all_fields(self):
        # Define a list of all the widgets to enable for editing
        widgets_to_enable = [
            self.Title_Line, self.Loc_cb, self.SOF_cb, self.TC_Line, self.AB_Line,
            self.DON_Date, self.DS_Date, self.DTC_Date, self.ID_Date, self.CD_sb, self.Ext_sb,
            self.ProjStat_sb, self.TCI_Line, self.Remarks_Line, self.ProjCoord_Line,
            self.Cont_Line, self.Enc_Line
        ]

        # Loop through the widgets and make them editable or enabled
        for widget in widgets_to_enable:
            if isinstance(widget, QtWidgets.QLineEdit):
                widget.setReadOnly(False)
                widget.setStyleSheet("")  # Reset style
            elif isinstance(widget, QtWidgets.QComboBox):
                widget.setEnabled(True)  # Enable interaction
                widget.setStyleSheet("")  # Reset style
            elif isinstance(widget, QtWidgets.QDateEdit):
                widget.setReadOnly(False)
                widget.setStyleSheet("")  # Reset style
            elif isinstance(widget, QtWidgets.QSpinBox):
                widget.setReadOnly(False)
                widget.setStyleSheet("")  # Reset style
            elif isinstance(widget, QtWidgets.QPlainTextEdit):
                widget.setReadOnly(False)
                widget.setStyleSheet("")  # Reset style

    def cancel_edit(self):
        self.clear_all_fields()
        self.enable_all_fields()
        self.Edit_btn.setVisible(False)
        self.Submit_btn.setVisible(True)
        self.CancelEdit_btn.setVisible(False)
        self.ClearAll_btn.setVisible(True)

    def save_edit_data(self):
        project_id = self.Id_Line.text()  # Assuming the hidden ID field holds the primary key
        project_encoder = self.Enc_Line.text()
        project_title = self.Title_Line.text()
        project_location = self.Loc_cb.currentText()
        project_coordinator = self.ProjCoord_Line.text()
        project_contractor = self.Cont_Line.text()
        project_source = self.SOF_cb.currentText()
        project_totalcost = self.TC_Line.text().replace("Php.", "").replace(",", "").strip()
        project_budget = self.AB_Line.text().replace("Php.", "").replace(",", "").strip()
        date_notice = self.DON_Date.date().toString("yyyy-MM-dd")
        date_start = self.DS_Date.date().toString("yyyy-MM-dd")
        date_target = self.DTC_Date.date().toString("yyyy-MM-dd")
        date_days = self.CD_sb.value()
        date_extension = self.Ext_sb.value()
        project_status = self.ProjStat_sb.value()
        project_incurred = self.TCI_Line.text().replace("Php.", "").replace(",", "").strip()
        date_inspection = self.ID_Date.date().toString("yyyy-MM-dd")
        project_remarks = self.Remarks_Line.toPlainText()

        # Prepare the SQL query for updating (instead of inserting)
        query = QSqlQuery()
        query.prepare("""
            UPDATE project_tb
            SET
                project_encoder = ?, project_title = ?, project_location = ?,
                project_coordinator = ?, project_contractor = ?, project_source = ?,
                project_totalcost = ?, project_budget = ?, date_notice = ?, date_start = ?,
                date_target = ?, date_days = ?, date_extension = ?, project_status = ?,
                project_incurred = ?, date_inspection = ?, project_remarks = ?
            WHERE project_id = ?
        """)
        query.addBindValue(project_encoder)
        query.addBindValue(project_title)
        query.addBindValue(project_location)
        query.addBindValue(project_coordinator)
        query.addBindValue(project_contractor)
        query.addBindValue(project_source)
        query.addBindValue(project_totalcost)
        query.addBindValue(project_budget)
        query.addBindValue(date_notice)
        query.addBindValue(date_start)
        query.addBindValue(date_target)
        query.addBindValue(date_days)
        query.addBindValue(date_extension)
        query.addBindValue(project_status)
        query.addBindValue(project_incurred)
        query.addBindValue(date_inspection)
        query.addBindValue(project_remarks)
        query.addBindValue(project_id)

        # Execute the query and check for errors
        if not query.exec():
            QtWidgets.QMessageBox.critical(None, "Database Error", query.lastError().text())
        else:
            QtWidgets.QMessageBox.information(None, "Success", "Data updated successfully!")

        self.clear_all_fields()
        self.enable_all_fields()
        self.Edit_btn.setVisible(False)
        self.Submit_btn.setVisible(True)
        self.CancelEdit_btn.setVisible(False)
        self.ClearAll_btn.setVisible(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)

    icon_path = os.path.join(os.path.dirname(__file__),"OME.ico")  # Make sure the .ico is included in the same directory as the .exe
    app.setWindowIcon(QtGui.QIcon(icon_path))  # Set application-wide icon
    Main_Window.setWindowIcon(QtGui.QIcon(icon_path))  # Set window-specific icon

    Main_Window.show()
    sys.exit(app.exec())
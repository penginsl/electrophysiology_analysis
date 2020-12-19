# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_process.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parent_folder_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.parent_folder_edit.setGeometry(QtCore.QRect(130, 20, 511, 31))
        self.parent_folder_edit.setObjectName("parent_folder_edit")
        self.parent_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.parent_folder_label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.parent_folder_label.setObjectName("parent_folder_label")
        self.open_parent_folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_parent_folder_btn.setGeometry(QtCore.QRect(660, 20, 113, 32))
        self.open_parent_folder_btn.setObjectName("open_parent_folder_btn")
        self.para_excel_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.para_excel_edit.setGeometry(QtCore.QRect(130, 70, 511, 31))
        self.para_excel_edit.setObjectName("para_excel_edit")
        self.para_excel_label = QtWidgets.QLabel(self.centralwidget)
        self.para_excel_label.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.para_excel_label.setObjectName("para_excel_label")
        self.browse_para_excel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_para_excel_btn.setGeometry(QtCore.QRect(660, 70, 113, 32))
        self.browse_para_excel_btn.setObjectName("browse_para_excel_btn")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(20, 120, 31, 21))
        self.date_label.setObjectName("date_label")
        self.date_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_edit.setGeometry(QtCore.QRect(60, 110, 141, 31))
        self.date_edit.setObjectName("date_edit")
        self.ch_num_label = QtWidgets.QLabel(self.centralwidget)
        self.ch_num_label.setGeometry(QtCore.QRect(250, 120, 51, 21))
        self.ch_num_label.setObjectName("ch_num_label")
        self.ch_num_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ch_num_edit.setGeometry(QtCore.QRect(320, 110, 101, 31))
        self.ch_num_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ch_num_edit.setObjectName("ch_num_edit")
        self.fs_label = QtWidgets.QLabel(self.centralwidget)
        self.fs_label.setGeometry(QtCore.QRect(480, 120, 51, 21))
        self.fs_label.setObjectName("fs_label")
        self.fs_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fs_edit.setGeometry(QtCore.QRect(540, 110, 101, 31))
        self.fs_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_edit.setObjectName("fs_edit")
        self.load_para_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_para_btn.setGeometry(QtCore.QRect(660, 110, 113, 32))
        self.load_para_btn.setObjectName("load_para_btn")
        self.rawdata_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.rawdata_folder_label.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.rawdata_folder_label.setObjectName("rawdata_folder_label")
        self.rawdata_folder_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.rawdata_folder_edit.setGeometry(QtCore.QRect(130, 150, 511, 31))
        self.rawdata_folder_edit.setObjectName("rawdata_folder_edit")
        self.open_rawdata_folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_rawdata_folder_btn.setGeometry(QtCore.QRect(660, 150, 113, 32))
        self.open_rawdata_folder_btn.setObjectName("open_rawdata_folder_btn")
        self.prev_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prev_data_btn.setGeometry(QtCore.QRect(280, 190, 113, 32))
        self.prev_data_btn.setObjectName("prev_data_btn")
        self.ori_rawdatas_label = QtWidgets.QLabel(self.centralwidget)
        self.ori_rawdatas_label.setGeometry(QtCore.QRect(20, 230, 101, 16))
        self.ori_rawdatas_label.setObjectName("ori_rawdatas_label")
        self.ori_rawdatas_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ori_rawdatas_edit.setGeometry(QtCore.QRect(130, 220, 511, 31))
        self.ori_rawdatas_edit.setObjectName("ori_rawdatas_edit")
        self.multisel_rawdatas_btn = QtWidgets.QPushButton(self.centralwidget)
        self.multisel_rawdatas_btn.setGeometry(QtCore.QRect(660, 220, 113, 32))
        self.multisel_rawdatas_btn.setObjectName("multisel_rawdatas_btn")
        self.trial_n_label = QtWidgets.QLabel(self.centralwidget)
        self.trial_n_label.setGeometry(QtCore.QRect(420, 320, 41, 16))
        self.trial_n_label.setObjectName("trial_n_label")
        self.trial_n_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.trial_n_edit.setGeometry(QtCore.QRect(460, 310, 181, 31))
        self.trial_n_edit.setText("")
        self.trial_n_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.trial_n_edit.setObjectName("trial_n_edit")
        self.rawdata_outputname_label = QtWidgets.QLabel(self.centralwidget)
        self.rawdata_outputname_label.setGeometry(QtCore.QRect(20, 280, 91, 16))
        self.rawdata_outputname_label.setObjectName("rawdata_outputname_label")
        self.rawdata_outputname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.rawdata_outputname_edit.setGeometry(QtCore.QRect(130, 270, 511, 31))
        self.rawdata_outputname_edit.setObjectName("rawdata_outputname_edit")
        self.rawdata_comb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rawdata_comb_btn.setGeometry(QtCore.QRect(660, 270, 113, 32))
        self.rawdata_comb_btn.setObjectName("rawdata_comb_btn")
        self.rec_len_label = QtWidgets.QLabel(self.centralwidget)
        self.rec_len_label.setGeometry(QtCore.QRect(20, 320, 71, 16))
        self.rec_len_label.setObjectName("rec_len_label")
        self.rec_len_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.rec_len_edit.setGeometry(QtCore.QRect(130, 310, 191, 31))
        self.rec_len_edit.setText("")
        self.rec_len_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.rec_len_edit.setObjectName("rec_len_edit")
        self.del_trial_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_trial_btn.setGeometry(QtCore.QRect(660, 310, 113, 32))
        self.del_trial_btn.setObjectName("del_trial_btn")
        self.bin_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.bin_folder_label.setGeometry(QtCore.QRect(20, 370, 81, 16))
        self.bin_folder_label.setObjectName("bin_folder_label")
        self.bin_folder_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.bin_folder_edit.setGeometry(QtCore.QRect(130, 360, 71, 31))
        self.bin_folder_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.bin_folder_edit.setObjectName("bin_folder_edit")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 410, 101, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(130, 400, 71, 31))
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.site_label = QtWidgets.QLabel(self.centralwidget)
        self.site_label.setGeometry(QtCore.QRect(420, 370, 31, 16))
        self.site_label.setObjectName("site_label")
        self.site_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.site_edit.setGeometry(QtCore.QRect(460, 360, 181, 31))
        self.site_edit.setText("")
        self.site_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.site_edit.setObjectName("site_edit")
        self.to_plxbin_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_plxbin_btn.setGeometry(QtCore.QRect(660, 360, 113, 32))
        self.to_plxbin_btn.setObjectName("to_plxbin_btn")
        self.to_mat_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_mat_btn.setGeometry(QtCore.QRect(660, 390, 113, 32))
        self.to_mat_btn.setObjectName("to_mat_btn")
        self.to_json_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_json_btn.setGeometry(QtCore.QRect(660, 420, 113, 32))
        self.to_json_btn.setObjectName("to_json_btn")
        self.to_nwb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_nwb_btn.setGeometry(QtCore.QRect(660, 450, 113, 32))
        self.to_nwb_btn.setObjectName("to_nwb_btn")
        self.comb_site_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.comb_site_chk.setGeometry(QtCore.QRect(220, 360, 131, 20))
        self.comb_site_chk.setObjectName("comb_site_chk")
        self.selfiles_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.selfiles_chk.setGeometry(QtCore.QRect(220, 390, 111, 20))
        self.selfiles_chk.setObjectName("selfiles_chk")
        self.sep_tet_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.sep_tet_chk.setGeometry(QtCore.QRect(220, 420, 111, 20))
        self.sep_tet_chk.setObjectName("sep_tet_chk")
        self.ele_map_10cm_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.ele_map_10cm_chk.setGeometry(QtCore.QRect(440, 400, 151, 20))
        self.ele_map_10cm_chk.setObjectName("ele_map_10cm_chk")
        self.rem_com_chk = QtWidgets.QCheckBox(self.centralwidget)
        self.rem_com_chk.setGeometry(QtCore.QRect(440, 430, 171, 20))
        self.rem_com_chk.setObjectName("rem_com_chk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parent_folder_label.setText(_translate("MainWindow", "Parent Folder"))
        self.open_parent_folder_btn.setText(_translate("MainWindow", "Open Folder"))
        self.para_excel_label.setText(_translate("MainWindow", "Paradigm Excel"))
        self.browse_para_excel_btn.setText(_translate("MainWindow", "Browse"))
        self.date_label.setText(_translate("MainWindow", "Date"))
        self.ch_num_label.setText(_translate("MainWindow", "Ch_Num"))
        self.ch_num_edit.setText(_translate("MainWindow", "16"))
        self.fs_label.setText(_translate("MainWindow", "Fs(Hz)"))
        self.fs_edit.setText(_translate("MainWindow", "30000"))
        self.load_para_btn.setText(_translate("MainWindow", "Load Param"))
        self.rawdata_folder_label.setText(_translate("MainWindow", "Rawdata Folder"))
        self.open_rawdata_folder_btn.setText(_translate("MainWindow", "Open Folder"))
        self.prev_data_btn.setText(_translate("MainWindow", "Preview Data"))
        self.ori_rawdatas_label.setText(_translate("MainWindow", "Original Rawdata"))
        self.multisel_rawdatas_btn.setText(_translate("MainWindow", "Multi-Sel"))
        self.trial_n_label.setText(_translate("MainWindow", "Trial #"))
        self.rawdata_outputname_label.setText(_translate("MainWindow", "Output name"))
        self.rawdata_comb_btn.setText(_translate("MainWindow", "Combine"))
        self.rec_len_label.setText(_translate("MainWindow", "Rec Len(s)"))
        self.del_trial_btn.setText(_translate("MainWindow", "Del Trial"))
        self.bin_folder_label.setText(_translate("MainWindow", "Binary Folder"))
        self.bin_folder_edit.setText(_translate("MainWindow", "Bin"))
        self.label_12.setText(_translate("MainWindow", "Saturation (mV)"))
        self.lineEdit_12.setText(_translate("MainWindow", "0.2"))
        self.site_label.setText(_translate("MainWindow", "Site"))
        self.to_plxbin_btn.setText(_translate("MainWindow", "ToPlxBin"))
        self.to_mat_btn.setText(_translate("MainWindow", "ToMat"))
        self.to_json_btn.setText(_translate("MainWindow", "ToJson"))
        self.to_nwb_btn.setText(_translate("MainWindow", "ToNWB"))
        self.comb_site_chk.setText(_translate("MainWindow", "Combine By Site"))
        self.selfiles_chk.setText(_translate("MainWindow", "Selected Files"))
        self.sep_tet_chk.setText(_translate("MainWindow", "1 file for 1 tet"))
        self.ele_map_10cm_chk.setText(_translate("MainWindow", "10 cm electrode map"))
        self.rem_com_chk.setText(_translate("MainWindow", "Remove Common Signal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

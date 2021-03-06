# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yogunlukDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv
import numpy as np
from skimage.exposure import rescale_intensity



class Ui_Dialog(object):

    path = None #Bu değişken resmin dizin yolunu tutacak
    img = None #bu değişken resmi tutacak

    def __init__(self,path) -> None:
        super().__init__()
        self.path = path


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 204)

        self.intensity_btn= QtWidgets.QPushButton(Dialog)
        self.intensity_btn.setGeometry(QtCore.QRect(40, 40, 121, 51))
        self.intensity_btn.setObjectName("intensity_in_range_btn")
        self.intensity_btn.clicked.connect(self.intensity_btn_clicked)

        self.min_spin = QtWidgets.QSpinBox(Dialog)
        self.min_spin.setGeometry(QtCore.QRect(240, 40, 42, 22))
        self.min_spin.setMaximum(255)
        self.min_spin.setObjectName("min_spin")

        self.max_spin = QtWidgets.QSpinBox(Dialog)
        self.max_spin.setGeometry(QtCore.QRect(240, 80, 42, 22))
        self.max_spin.setMaximum(255)
        self.max_spin.setObjectName("max_spin")

        self.kaydet = QtWidgets.QPushButton(Dialog)
        self.kaydet.setGeometry(QtCore.QRect(40, 100, 121, 51))
        self.kaydet.setObjectName("kaydet")
        self.kaydet.clicked.connect(self.kaydet_btn_clicked)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 40, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 80, 55, 16))
        self.label_2.setObjectName("label_2")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Yogunluk Donusum"))
        self.intensity_btn.setText(_translate("Dialog", "Rescale Intensity"))
        self.label.setText(_translate("Dialog", "Min:"))
        self.label_2.setText(_translate("Dialog", "Max:"))
        self.kaydet.setText(_translate("Dialog", "Kaydet"))

    def kaydet_btn_clicked(self):

        if(self.img is None):
            print("resim yüklenmedi")
        else:
            file_tuple = QFileDialog.getSaveFileName(None, 'Kaydet', '', '*.png')
            name = str(file_tuple[0]).replace("/","\\")
            cv.imwrite("rescaled_intensity.jpg", self.img)
            print("resim kaydedildi")

    #remin yoğunluğunu değiştirme işlevselliğini sağlayan fonksiyon.
    def intensity_btn_clicked(self):
        
        #Kullanıcının girdiği değerleri alıyoruz.
        min_value = self.min_spin.value()
        max_value = self.max_spin.value()

        #resmi okuyoruz.
        self.img = cv.imread(self.path)
        #rescale_intensity fonksiyonu ile resmin yoğunluğunu kullanıcının girdiği değerlere göre
        #değiştiriyoruz.
        self.img = rescale_intensity(self.img, in_range=(min_value,max_value))
        #Değişen resmi kullanıcıya gösteriyoruz.
        cv.imshow("rescaled intensity", self.img)
        cv.waitKey(0)
        cv.destroyAllWindows()





from PyQt5 import QtGui,QtCore
import cv2
import numpy as np


class CameraWidget:
    IMG_WIDTH=320
    IMG_HEIGHT=240

    def __init__(self,winParent):
        self.winParent=winParent
        self.labelImageLeft=winParent.imageLeft
        self.labelImageRight=winParent.imageRight
        self.labelImageRightFiltered = winParent.imageRightFiltered
        self.labelImageLeftFiltered = winParent.imageLeftFiltered


    def updateImage(self):

        imgLeft = self.winParent.getCameraL().getImage().data
        if imgLeft is not  None:
            resized = cv2.resize(imgLeft,(self.IMG_WIDTH,self.IMG_HEIGHT))
            image = QtGui.QImage(resized.data, resized.shape[1], resized.shape[0], resized.shape[1]*resized.shape[2], QtGui.QImage.Format_RGB888);
            size=QtCore.QSize(imgLeft.shape[1],imgLeft.shape[0])
            #self.label.resize(size)
            self.labelImageLeft.setPixmap(QtGui.QPixmap.fromImage(image))

        imgRight = self.winParent.getCameraR().getImage().data
        if imgRight is not None:
            resized = cv2.resize(imgRight,(self.IMG_WIDTH,self.IMG_HEIGHT))
            image = QtGui.QImage(resized.data, resized.shape[1], resized.shape[0], resized.shape[1]*resized.shape[2], QtGui.QImage.Format_RGB888);
            size=QtCore.QSize(imgRight.shape[1],imgRight.shape[0])
            #self.label.resize(size)
            self.labelImageRight.setPixmap(QtGui.QPixmap.fromImage(image))


        #print the filtered images

        imgLeftFiltered = self.winParent.getAlgorithm().getLeftImageFiltered()
        if imgLeftFiltered is not None:
            resized = cv2.resize(imgLeftFiltered,(self.IMG_WIDTH,self.IMG_HEIGHT))
            image = QtGui.QImage(resized.data, resized.shape[1], resized.shape[0], resized.shape[1]*resized.shape[2], QtGui.QImage.Format_RGB888);
            size=QtCore.QSize(imgLeftFiltered.shape[1],imgLeftFiltered.shape[0])
            #self.label.resize(size)
            self.labelImageLeftFiltered.setPixmap(QtGui.QPixmap.fromImage(image))
        else:
            image = np.zeros((self.IMG_WIDTH, self.IMG_HEIGHT,3), np.uint8)
            image.shape = self.IMG_HEIGHT, self.IMG_WIDTH,3
            blackimage = QtGui.QImage(image, image.shape[1], image.shape[0], image.shape[1]*image.shape[2], QtGui.QImage.Format_RGB888);
            size=QtCore.QSize(image.shape[1],image.shape[0])
            #self.label.resize(size)
            self.labelImageLeftFiltered.setPixmap(QtGui.QPixmap.fromImage(blackimage))

        imgRightFiltered = self.winParent.getAlgorithm().getRightImageFiltered()
        if imgRightFiltered is not None:
            resized = cv2.resize(imgRightFiltered,(self.IMG_WIDTH,self.IMG_HEIGHT))
            image = QtGui.QImage(resized.data, resized.shape[1], resized.shape[0], resized.shape[1]*resized.shape[2], QtGui.QImage.Format_RGB888);
            size=QtCore.QSize(imgRightFiltered.shape[1],imgRightFiltered.shape[0])
            #self.label.resize(size)
            self.labelImageRightFiltered.setPixmap(QtGui.QPixmap.fromImage(image))
        else:
            image = np.zeros((self.IMG_WIDTH, self.IMG_HEIGHT,3), np.uint8)
            image.shape = self.IMG_HEIGHT, self.IMG_WIDTH,3
            blackimage = QtGui.QImage(image, image.shape[1], image.shape[0], image.shape[1]*image.shape[2], QtGui.QImage.Format_RGB888);
            size=QtCore.QSize(image.shape[1],image.shape[0])
            #self.label.resize(size)
            self.labelImageRightFiltered.setPixmap(QtGui.QPixmap.fromImage(blackimage))

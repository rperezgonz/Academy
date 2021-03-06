#
#  Copyright (C) 1997-2016 JDE Developers Team
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/.
#  Authors :
#       Alberto Martin Florido <almartinflorido@gmail.com>
#       Aitor Martinez Fernandez <aitor.martinez.fernandez@gmail.com>
#
import numpy as np
import threading

class CameraFilter:

    def __init__(self, camera):
        self.lock = threading.Lock()
        self.client = camera

        img = self.client.getImage()

        self.height= img.height
        self.width = img.width


        if self.client.hasproxy():
            self.trackImage = np.zeros((self.height, self.width,3), np.uint8)
            self.trackImage.shape = self.height, self.width, 3

            self.filteredImage = np.zeros((self.height,self. width,3), np.uint8)
            self.filteredImage.shape = self.height, self.width, 3

        

    
    def getImage(self):
        self.lock.acquire()
        img = self.client.getImage()
        self.lock.release()
        return img

    def updateImage(self):
        if self.client.hasproxy():
            img = self.getImage().data
            self.lock.acquire()
            self.trackImage = img
            self.trackImage.shape = img.shape
            self.lock.release()

    def getColorImage(self):
        if self.client.hasproxy():
            self.lock.acquire()
            img = np.zeros((self.height, self.width,3), np.uint8)
            img = self.trackImage
            img.shape = self.trackImage.shape
            self.lock.release()
            return img
        return None

    def setColorImage(self,image):
        if self.client.hasproxy():
            self.lock.acquire()
            self.trackImage = image
            self.trackImage.shape = image.shape
            self.lock.release()

    def getFilteredImage(self):
        if self.client.hasproxy():
            self.lock.acquire()
            img = np.zeros((self.height, self.width,1), np.uint8)
            img = self.filteredImage
            img.shape = self.filteredImage.shape
            self.lock.release()
            return img
        return None

    def setFilteredImage(self,image):
        if self.client.hasproxy():
            self.lock.acquire()
            self.filteredImage = image
            self.filteredImage.shape = image.shape
            self.lock.release()

    def stop(self):
        self.client.stop()

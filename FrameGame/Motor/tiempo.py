#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      danielx
#
# Created:     26/12/2014
# Copyright:   (c) danielx 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time

CONT = 0.585

class Tiempo(object):

    def __init__ (self):
        self.contador = 0
        self.time_ac = 0
        self.time_save = 0

        self.segm = 0
        self.estado = False
        self.rapidez = CONT

    def gettime(self):
        return time.time()

    def modPasivo(self,):
        self.segm =self.time_save = self.time_ac = time.time()
        self.contador = 0
        self.estado = False
        return self.time_save

    def cronometroA(self,):
        self.time_ac = time.time()
        return self.time_ac - self.time_save

    def cronometroB(self,):
        self.time_ac = time.time()

        if self.time_ac != self.time_save:
            self.contador+=0.005
            self.time_ac = self.time_ac + self.contador
            print "---> "+str(self.time_ac - self.time_save)

        return self.time_ac - self.time_save

    def cronometroC(self,):
        tiempo = time.time()

        if tiempo != self.segm:
            self.contador+=self.rapidez
            self.segm = tiempo
            self.time_ac = tiempo + self.contador
            self.time_ac = self.time_ac - self.time_save
            #print "[]---> "+str(self.time_ac)
            return self.time_ac
        else:
            if self.estado == False:
                self.estado = True
                self.time_ac = 0.0
                return self.time_ac

        return self.time_ac

    def cronometroD(self):
        self.contador+= (1/120.0)+0.25
        return self.contador



def main():
    tem = Tiempo()
    tem.modPasivo()
    while True:
        tem.cronometroC()

if __name__ == '__main__':
    main()

from numpy import genfromtxt,interp,diff,zeros,mean,shape,copy,exp
from os import getcwd,chdir,path
import matplotlib.cm as cm
import matplotlib.colors as co
import datetime


class Constants():
    Quad = 4.3380E-4
    Lin = 3.6110E-2
    Const = 0.001440789

    Blow = 4.700000E-15

    ni  = 6.361283E+9       #this is the value from the QSSPL system

    q = 1.60217646e-19
    T = 300
    kb = 1.3806488e-23
    Vt = kb*T/q
    
    c = 299792458             #m/s
    h = 6.62606957e-34        #m^2 kg /s

    Wavelength = 808e-7 #nm


    def N_i(self,temp=300,BGN=False):
        #This needs to be changed by the bandgap narrowing term
        #This has only been confimed up to 340K
        
        self.T = temp
            
            #This is a modified version of Misiakos1993 
        self.ni = 5.29*10**19*(temp/300.)**2.54*exp(-6726./temp)
        if BGN!=False:
            self.ni *=exp(BGN/2/self.K/temp)

    def Binning(self,data,BinAmount):
        
        


        if len(data.shape)!=1:
            data2 = zeros((data.shape[0]//BinAmount,data.shape[1]))
        else:
            data2 = zeros((data.shape[0]//BinAmount))



        for i in range(data.shape[0]//BinAmount):         
            data2[i] = mean(data[i*BinAmount:(i+1)*BinAmount],axis=0)

        return data2

    def Binning_Named(self,data,BinAmount):
        



        if len(data.dtype.names)!= 1:
            data2 = copy(data)[::BinAmount]

        for i in data.dtype.names:
            for j in range(data.shape[0]//BinAmount):       
        #     #print mean(data[i*BinAmount:(i+1)*BinAmount,:],axis=0),data2[i,:]

                data2[i][j] = mean(data[i][j*BinAmount:(j+1)*BinAmount],axis=0)

        
        return data2

    def WavelengthToAlpha(self):
        #This file is in nm, so lets make it in cm and returns in /cm
        temp = getcwd()
        chdir('/home/mattias/Dropbox/CommonCode/Constants/')


        # print os.path.dirname()
        WavelengthToAlpha = genfromtxt('ExcitationWavelength.dat',usecols=(0,4))

        if (all(diff(WavelengthToAlpha[:,0]) > 0)==False):
            print 'Error in Alpha File, x col must be increasing'
            print WavelengthToAlpha[:,0]    



        self.alpha = interp(self.Wavelength*1e7,WavelengthToAlpha[:,0],WavelengthToAlpha[:,1])

        chdir(temp)

    def ColorRange(self,Number,colourmap='rainbow'):
        #http://www.physics.ox.ac.uk/Users/msshin/science/code/matplotlib_cm/
        a = co.Normalize(0,Number-1)
        b=  cm.ScalarMappable(norm=a,cmap=cm.get_cmap(colourmap))
        #To use need to write

        color_list = []
        for i in range(Number):
            color_list.append(b.to_rgba(i)) 

        return color_list

    def modification_date(self,filename):
        t = path.getmtime(filename)
        return datetime.datetime.fromtimestamp(t)

    def creation_date(self,filename):
        t = path.getctime(filename)
        return datetime.datetime.fromtimestamp(t)

if __name__ == "__main__":
    #This is for testing if the fucntions work
    a = Constants()
    print a.ni
    a.N_i(300)
    print a.ni
    # a.Wavelength = 1000
    # a.WavelengthToAlpha()
    # print a.Wavelength ,a.alpha

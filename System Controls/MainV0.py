#importing wx files
import wx,sys
 
#import the newly created GUI file
import Gui_Main_v2 as gui
 
sys.path.append('/home/mattias/Dropbox/CommonCode/Constants')
sys.path.append('C:\Users\mattias\Dropbox\CommonCode\Constants')
sys.path.append('C:\Users\Shanoot\Dropbox\CommonCode\Constants')
sys.path.append('C:\Users\z3186867\Dropbox\CommonCode\Constants')

from ConstantsClass import *
from CanvasClass import *

from matplotlib.pylab import *
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

import numpy as np

import ctypes
import threading
import matplotlib.pylab as plt
from math import pi
# load any DLLs
nidaq = ctypes.windll.nicaiu # load the DLL
##############################
# Setup some typedefs and constants
# to correspond with values in
# C:\Program Files\National Instruments\NI-DAQ\DAQmx ANSI C Dev\include\NIDAQmx.h
# the typedefs
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32
# the constants
DAQmx_Val_Cfg_Default = int32(-1)
DAQmx_Val_Volts = 10348
DAQmx_Val_Rising = 10280
DAQmx_Val_FiniteSamps = 10178
DAQmx_Val_ContSamps = 10123
DAQmx_Val_GroupByChannel = 0

DAQmx_Val_Diff = int32(-1)
DAQmx_Val_GroupByScanNumber = 0 #this places the points one at a time from each channel, I think
DAQmx_InputSampleRate = float64(1e6) #max is float64(1e6)
DAQmx_OutPutSampleRate = 25000 #No idea what the max is

class WaveformThread( threading.Thread ):
    """
    This class performs the necessary initialization of the DAQ hardware and
    spawns a thread to handle playback of the signal.
    It takes as input arguments the waveform to play and the sample rate at which
    to play it.
    This will play an arbitrary-length waveform file.
    """
    def __init__( self, waveform,Channel,Time):
        self.running = True
        self.sampleRate = DAQmx_OutPutSampleRate
        # self.periodLength = len( waveform )
        self.periodLength = int(Time*float32(DAQmx_OutPutSampleRate))
        self.waveform=waveform
        self.Channel = Channel
        self.taskHandle_Write = TaskHandle(0)
        self.taskHandle_Read = TaskHandle(1)
        self.Setup_Write()
        self.Setup_Read_Vals(Time)
    def Setup_Write(self):
        self.Write_data = numpy.zeros( ( self.periodLength, ), dtype=numpy.float64 )
        # convert waveform to a numpy array
        for i in range( self.periodLength ):
            self.Write_data[ i ] = self.waveform[ i ]
        # setup the DAQ hardware
        self.CHK(nidaq.DAQmxCreateTask("",
                          ctypes.byref( self.taskHandle_Write )))
        self.CHK(nidaq.DAQmxCreateAOVoltageChan( self.taskHandle_Write ,
                                   "Dev1/"+self.Channel,
                                   "",
                                   float64(-10.0),
                                   float64(10.0),
                                   DAQmx_Val_Volts,
                                   None))

        self.CHK(nidaq.DAQmxCfgSampClkTiming( self.taskHandle_Write ,
                                "", 
                                float64(self.sampleRate),   #samples per channel
                                DAQmx_Val_Rising,   #active edge
                                DAQmx_Val_FiniteSamps,
                                uInt64(self.periodLength)));
        self.CHK(nidaq.DAQmxWriteAnalogF64( self.taskHandle_Write ,
                              int32(self.periodLength),
                              0,
                              float64(-1),
                              DAQmx_Val_GroupByChannel,
                              self.Write_data.ctypes.data,
                              None,
                              None))
        threading.Thread.__init__( self )

    def CHK( self, err ):
        """a simple error checking routine"""
        if err < 0:
            buf_size = 100
            buf = ctypes.create_string_buffer('\000' * buf_size)
            nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)
            raise RuntimeError('nidaq call failed with error %d: %s'%(err,repr(buf.value)))
        if err > 0:
            buf_size = 100
            buf = ctypes.create_string_buffer('\000' * buf_size)
            nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)
            raise RuntimeError('nidaq generated warning %d: %s'%(err,repr(buf.value)))
    def run( self ):
        counter = 0
        self.CHK(nidaq.DAQmxStartTask( self.taskHandle_Write ))
    def stop( self ):
        self.running = False
        nidaq.DAQmxStopTask( self.taskHandle_Write )
        nidaq.DAQmxClearTask( self.taskHandle_Write )

    def Setup_Read_Vals(self,Time):
        

        self.max_num_samples = int(numpy.float32(DAQmx_InputSampleRate)*3*Time)
        # print Time
        self.CHK(nidaq.DAQmxCreateTask("",ctypes.byref(self.taskHandle_Read)))
        self.CHK(nidaq.DAQmxCreateAIVoltageChan(self.taskHandle_Read,"Dev1/ai0:2","",          
                                                   DAQmx_Val_Diff,            #DAQmx_Val_Diff,   #DAQmx_Val_RSE,       #DAQmx_Val_Cfg_Default, #this is the rise type
                                                   float64(-10.0),float64(10.0),
                                                   DAQmx_Val_Volts,
                                                   None))
        self.CHK(nidaq.DAQmxCfgSampClkTiming(self.taskHandle_Read,"",DAQmx_InputSampleRate, DAQmx_Val_Rising,DAQmx_Val_FiniteSamps,uInt64(self.max_num_samples)))
        # DAQmxCfgSampClkTiming(taskHandle,"",sampleRate,DAQmx_Val_Rising,DAQmx_Val_FiniteSamps,sampsPerChan);      
        #DAQmx Start Code
        self.Read_Data = numpy.zeros((self.max_num_samples,),dtype=numpy.float64)

    def Read_Vals(self):


        self.CHK(nidaq.DAQmxStartTask(self.taskHandle_Read))
        read = int32()
        #DAQmx Read Code
        self.CHK(nidaq.DAQmxReadAnalogF64(self.taskHandle_Read,
                                                 -1,
                                                 float64(10.0),    #Timeout in seconds
                                                 DAQmx_Val_GroupByScanNumber,       #DAQmx_Val_GroupByChannel,    #DAQmx_Val_GroupByScanNumber
                                                 self.Read_Data.ctypes.data, #the vairable being assinged?
                                                 self.max_num_samples,   #maximum number of samples
                                                 ctypes.byref(read),None))

        # print "Acquired %d points"%(read.value)
        if self.taskHandle_Read.value != 0:
            nidaq.DAQmxStopTask(self.taskHandle_Read)
            nidaq.DAQmxClearTask(self.taskHandle_Read)


        # print 'Number of poitns collected:',Data.shape
        return self.Read_Data




class LightPulse():
    def __init__( self,Waveform,Amplitude,Offset_Before,Offset_After,Time):
        self.Waveform = Waveform
        self.A = Amplitude
        self.Offset_Before= Offset_Before     #ms
        self.Offset_After=Offset_After        #ms
        self.Time = Time                      #ms

    def Define(self):
        V_before = np.zeros((int(DAQmx_OutPutSampleRate*self.Offset_Before/1000)))
        V_after = np.zeros((int(DAQmx_OutPutSampleRate*self.Offset_After/1000)))
        self.t = np.linspace(0,self.Time,DAQmx_OutPutSampleRate*self.Time)
        
        V = getattr(self,self.Waveform)(self.t)

        Voltage_waveform = np.concatenate((V_before,V,V_after))

        Total_Time = self.Offset_Before/1000+self.Offset_After/1000+self.Time
        self.t = np.linspace(0,Total_Time,Voltage_waveform.shape[0])
        
        return Voltage_waveform

    def Sin(self,t):
        return -self.A*np.abs(np.sin(pi*t/t[-1]))

    def Square(self,t):
        return -self.A*np.ones((t.shape[0]))    

    def Cos(self,t):

        return -self.A*np.abs(np.cos(pi*t/t[-1]))

    def Triangle(self,t):
        halfway = t.shape[0]/2
        return -1*np.concatenate((self.A*2/t[-1]*t[:halfway],-self.A*2/t[-1]*t[:halfway]+self.A))
        
    def MJ(self,t):
        fraction = 0.01
        t_shift = t.shape[0]*fraction
        t0_index = t.shape[0]*(0.5-fraction)
        t_halfway_index = t.shape[0]/2
        t_halfway = t[t_halfway_index]
        t0 = t[t0_index]
        
        #Funtions are:
        # G = C/t
        #G = Bx^4 + Amplitude
        #These are then spliced together at t0

        B,C = -self.A*t[t_shift]**(-4)/5.,4./5*self.A*t[t_shift]
        f = np.concatenate((-C/(t[:t0_index]-t_halfway),B*(t[t0_index:t_halfway_index]-t_halfway)**4+self.A))
        return -1*np.concatenate((f,f[::-1]))

class OutPutData():
    def __init__( self ):
        self.file_opt = options = {}
        options['title'] = 'Save you data Dude!'
        options['defaultextension'] = r'Raw Data.dat'
        options['filetypes'] = [('Raw Data Files', r"Raw Data.*"),('all files', '.*')]

    def Save(self,event):
        filename = tkFileDialog.asksaveasfilename(**self.file_opt)
        # print filename
        if not filename:
            print 'Canceled save'
        else:

            numpy.savetxt(filename,self.Data,delimiter='\t')

class TakeMeasurements():
    def __init__( self,OutPutVoltage,Averaging,Channel,Time):
        self.OutPutVoltage=OutPutVoltage
        self.SampleRate=DAQmx_OutPutSampleRate
        self.Time=Time
        # print self.Time,Time
        self.Averaging = int(Averaging)
        self.Channel = Channel

    def SingleMeasurement(self):
        
        mythread = WaveformThread( self.OutPutVoltage,self.Channel,self.Time)
        # start playing waveform
        mythread.start()
        #Starts reading the Values
        # self.data=mythread.Setup_Read_Vals(self.Time)
        self.data=mythread.Read_Vals()
        #Stops the wave form
        mythread.stop()
        return self.data

    def Average(self):
        RunningTotal =self.SingleMeasurement()       
        for i in range(self.Averaging-1):
                
            RunningTotal = np.vstack((self.SingleMeasurement(),RunningTotal))
            #The running total is weigged for the number of points inside it
            RunningTotal = np.average(RunningTotal,axis=0,weights =(1,i+1))
        return RunningTotal

    def Measure(self):
        
        if self.Averaging>0:

            
            data = self.Average()

            #Here the 3 stands for the number of channels what are going to be read
            Data = numpy.empty((int(data.shape[0]/3),3))
            # print Data.shape,data.shape
            for i in range(2):
                #The data should be outputted one of each other, so divide is up and roll it out
                # print data[i*Data.shape[0]:(i+1)*Data.shape[0]].shape
                Data[:,i]= data[i*Data.shape[0]:(i+1)*Data.shape[0]]

            return Data
        else:
            print 'Averaging Too low'




class Test(gui.MyFrame1,OutPutData):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MyFrame1.__init__(self,parent)

        self.Fig1 = CanvasPanel(self.Figure1_Panel)
        self.Fig1.labels('Raw Data','Time (a.u.)','Voltage (V)')
        # CanvasPanel(self.Figure2_Panel)
    
    def Determine_Digital_Output_Channel(self):
        #Just a simple function choosing the correct output channel based on the drop down box
        if self.m_Output.GetStringSelection()=='High (2A/V)':
            Channel = 'ao0'
        elif self.m_Output.GetStringSelection()=='Low (50mA/V)':
            Channel = 'ao1'
        return Channel



    def Perform_Measurement(self,event):
        #this is what happens when the go button is pressed

        #first thing is all the inputs are grabbed
        #A check is performed, and if failed, event is skipped
        Intensity = self.CHK_float(self.m_Intensity,event)
        Binning = self.CHK_int(self.m_Binning,event)
        Peroid = self.CHK_float(self.m_Period,event)
        Offset_Before= self.CHK_float(self.m_Offset_Before,event)
        Offset_After= self.CHK_float(self.m_Offset_After,event)

        #This the event hasn't been skipped then continue with the code.        
        if event.GetSkipped()==False:
            self.m_scrolledWindow1.Refresh()
            # self.TotalTime = Peroid+Offset_Before/1000+Offset_After/1000

            if  int(self.m_Averaging.GetValue()) >0:
                Averaging = int(self.m_Averaging.GetValue())
            else:
                print 'Averaging has to be a positive integer'
                self.m_Averaging.SetValue('1') 
                Averaging = self.m_Averaging.GetValue() 



            
            #Then the light pulse is defined, but the lightpulse class
            lightPulse = LightPulse(self.m_Waveform.GetStringSelection(),Intensity,Offset_Before,Offset_After,Peroid)
        

            #We determine what channel to output on
            Channel=self.Determine_Digital_Output_Channel()
            lightPulse.Define()
            t = lightPulse.t

            #We put all that info into the take measurement section, which is a instance definition. There are also global variables that go into this        
            Go = TakeMeasurements(lightPulse.Define(),Averaging,Channel,t[-1])

            # Go.Measure()
            # print 'here'
            #USing that instance we then run the lights, and measure the outputs
            self.Data = self.Binning(Go.Measure(),Binning)
            # self.Data = lightPulse.Define()
            #We then plot the datas, this has to be changed if the plots want to be updated on the fly.
            self.PlotData(t)
            event.Skip()
        else:
            
            self.m_scrolledWindow1.Refresh()

    def PlotData(self,t):
        self.Fig1.clear()
        labels = ['PC','Reference','PL']
        t = np.linspace(0,t[-1],self.Data.shape[0])
        colours = ['b','r','g']

        #this is done not to clog up the plot with many points
        if self.Data.shape[0]>1000:
            num = self.Data.shape[0]//1000
        else:
            num=1


        #This plots the figure
        # print self.Data
        # print self.Data.shape,t.shape
        for i,label,colour in zip(self.Data.T,labels,colours):
            # print i,label,colour,
            # print colour
            print i.shape,t.shape
            self.Fig1.draw_points(t[::num],i[::num],'.',Color=colour,Label = label)
            # self.Fig1.draw_line(t[::num],i[::num],'--',Color=colour,Label = label)
        self.Fig1.update()   



    def Binning(self,data,BinAmount):
    #print BinAmount,data.shape[0],data.shape[0]//BinAmount
        # print 
        if BinAmount ==1:
            return data
        if len(data.shape)==1:
            data2 = zeros((data.shape[0]//BinAmount))
        else:
            data2 = zeros((data.shape[0]//BinAmount,data.shape[1]))

        # print 'here'
        for i in range(data.shape[0]//BinAmount):
        #     #print mean(data[i*BinAmount:(i+1)*BinAmount,:],axis=0),data2[i,:]
            # print i
            data2[i] = mean(data[i*BinAmount:(i+1)*BinAmount],axis=0)

        return data2

    def onChar(self, event):
        #This function is for ensuring only numerical values are placed inside the textboxes
        key = event.GetKeyCode()
        # print key
        # print ord(key)
        acceptable_characters = "1234567890."
        if key<256 and key!=8:
            if chr(key) in acceptable_characters:
                event.Skip()
                return

            else:
                return False
        else:
            event.Skip()
            return 
    def onChar_int(self, event):
        #This function is for ensuring only numerical values are placed inside the textboxes
        key = event.GetKeyCode()
        # print key
        # print ord(key)
        acceptable_characters = "1234567890"
        if key<256 and key!=8:
            if chr(key) in acceptable_characters:
                event.Skip()
                return

            else:
                return False
        else:
            event.Skip()
            return 

    def CurrentLimits(self,event):
        # print self.m_Output.GetStringSelection(),self.m_Intensity.GetValue(),float(self.m_Intensity.GetValue())>1.5

        #This is function to determine the approiate current limit for the box
        #A 10V limit is imposed owing to limitations on the output voltage of the datcard
        try:
            if self.m_Output.GetStringSelection()=='Low (50mA/V)':
                if float(self.m_Intensity.GetValue())>10:
                    # self.m_Intensity.SetBackgroundColour('RED')
                    self.m_Intensity.SetValue('10')
                # else:
                #     self.m_Intensity.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ))
            #A 1.5V limit is imposed as a limit owing to the current limit of the power supply.
            elif self.m_Output.GetStringSelection()=='High (2A/V)':
                
                if float(self.m_Intensity.GetValue())>1.5:
                    # self.m_Intensity.SetBackgroundColour('RED')
                    self.m_Intensity.SetValue('1.5')
                
            return False
        except:
            
            return False

    def CHK_int(self,Textbox,event):
        try:
            return int(Textbox.GetValue())
            Textbox.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ))
        except:
            Textbox.SetBackgroundColour('RED') 
            event.Skip()
    def CHK_float(self,Textbox,event):
        try:
            # print Textbox.GetValue(),float(Textbox.GetValue())
            Textbox.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ))
            return float(Textbox.GetValue())
        except:
            # print'yeah'
            Textbox.SetBackgroundColour('RED')

            event.Skip()
            return 0

#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
# #create an object of CalcFrame
frame = Test(None)
#show the frame
frame.Show(True)
#start the applic
app.MainLoop()
# t = np.linspace(0,10,10000)
# a=LightPulse()
# a.A = 1
# V=a.Triangle(t)
# plot(t,V)
# V=a.MJ(t)
# plot(t,V)
# show()

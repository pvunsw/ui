import threading
import numpy as np

from config import device
from library import *

DAQmx_OutPutSampleRate = device["output_samplerate"]
DAQmx_InputSampleRate = device["input_samplerate"]

class WaveformThread( threading.Thread ):
    DAQmx_Val_Cfg_Default = int32(-1)
    DAQmx_Val_Volts = 10348
    DAQmx_Val_Rising = 10280
    DAQmx_Val_FiniteSamps = 10178
    DAQmx_Val_ContSamps = 10123
    DAQmx_Val_GroupByChannel = 0
    DAQmax_Channels_Number =3

    DAQmx_Val_Diff = int32(-1)
    InputVoltageRange = 10  #this controls the input voltage range. (=-10,=-5, =-2,+-1)
    OutputVoltageRange = 10 #this controls the  output voltage range. Minimum is -5 to 5
    DAQmx_Val_GroupByScanNumber = 0 #this places the points one at a time from each channel, I think

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
        self.periodLength = Time*DAQmx_OutPutSampleRate
        self.Time = Time

        self.Write_data = numpy.zeros( ( self.periodLength, ), dtype=numpy.float64 )

        for i in range( self.periodLength ):

            self.Write_data[ i ] = waveform[ i ]

        #plot(self.Write_data)
        #show()
        self.taskHandle_Write = TaskHandle(0)
        self.taskHandle_Read = TaskHandle(1)
        self.Channel = Channel



        self.Setup_Write()
        self.Setup_Read(Time)

    def Setup_Write(self):
        # convert waveform to a numpy array

        # setup the DAQ hardware
        self.CHK(nidaq.DAQmxCreateTask("",
                          ctypes.byref( self.taskHandle_Write )))

        self.CHK(nidaq.DAQmxCreateAOVoltageChan( self.taskHandle_Write ,
                                   device["name"]+self.Channel,
                                   "",
                                   float64(-self.OutputVoltageRange),
                                   float64(self.OutputVoltageRange),
                                   self.DAQmx_Val_Volts,
                                   None))

        self.CHK(nidaq.DAQmxCfgSampClkTiming( self.taskHandle_Write ,
                                "/TestDev_6251/ai/SampleClock",
                                self.sampleRate,   #samples per channel
                                self.DAQmx_Val_Rising,   #active edge
                                self.DAQmx_Val_FiniteSamps,
                                uInt64(self.periodLength)));

        self.CHK(nidaq.DAQmxWriteAnalogF64( self.taskHandle_Write , #TaskHandel
                              int32(self.periodLength),             #num of samples per channel
                              0,                                    #autostart, if this is not done, a NI-DAQmx Start function is requried
                              float64(-1),                          #Timeout
                              self.DAQmx_Val_GroupByChannel,             #Data layout
                              self.Write_data.ctypes.data,          #write array
                              None,                                 #samplers per channel written
                              None))                                #reserved
        threading.Thread.__init__( self )

    def Setup_Read(self,Time):


        self.max_num_samples = int(numpy.float32(DAQmx_InputSampleRate)*3*Time)
        # print Time
        self.CHK(nidaq.DAQmxCreateTask("",ctypes.byref(self.taskHandle_Read)))

        self.CHK(nidaq.DAQmxCreateAIVoltageChan(self.taskHandle_Read,"TestDev_6251/ai0:2","",
                                                   self.DAQmx_Val_Diff,            #DAQmx_Val_Diff,   #DAQmx_Val_RSE,       #DAQmx_Val_Cfg_Default, #this is the rise type
                                                   float64(-self.InputVoltageRange),float64(self.InputVoltageRange),
                                                   self.DAQmx_Val_Volts,
                                                   None))

        self.CHK(nidaq.DAQmxCfgSampClkTiming(self.taskHandle_Read,
                                            "",#"/Dev3/ao/SampleClock",#"ao/SampleClock",#"Dev3/"+self.Channel+"/SampleClock"-doesn;t work,
                                            DAQmx_InputSampleRate,
                                            self.DAQmx_Val_Rising,
                                            self.DAQmx_Val_FiniteSamps,
                                            uInt64(self.max_num_samples)
                                            ))
        # DAQmxCfgSampClkTiming(taskHandle,"",sampleRate,DAQmx_Val_Rising,DAQmx_Val_FiniteSamps,sampsPerChan);
        #DAQmx Start Code
        self.Read_Data = numpy.zeros((self.max_num_samples,),dtype=numpy.float64)
        self.read = int32()
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
        self.CHK(nidaq.DAQmxStartTask(self.taskHandle_Read))


        #DAQmx Read Code
        #tic = time.clock()



        self.CHK(nidaq.DAQmxReadAnalogF64(self.taskHandle_Read, #Task handle
                                                 -1,            #numSamples per channel, -1 reads as many samples as possible
                                                 float64(10.0),    #Timeout in seconds
                                                 self.DAQmx_Val_GroupByScanNumber,       #DAQmx_Val_GroupByChannel,    #DAQmx_Val_GroupByScanNumber
                                                 self.Read_Data.ctypes.data, #read array
                                                 self.max_num_samples,   #samples per channel
                                                 ctypes.byref(self.read), #The actual number of samples read per channel (its an output)
                                                 None)) #reserved for future use, pass none to this
        #toc = time.clock()
        # print self.Time
        self.time = np.linspace(0,self.Time,self.read.value)
        # print self.time[0]

        #This check was performed to drtermine if the set frequency was actually what was measured. It appears it is.
        ## print self.read.value
        ## print (toc - tic)*1e6
        ## print 'Minimum time reading',(toc - tic)*1e6/(self.read.value)
        # plot(self.Read_Data)
        # show()
        # print self.read
        return self.Read_Data

    def stop( self ):
        self.running = False
        if self.taskHandle_Write.value != 0:
            nidaq.DAQmxStopTask( self.taskHandle_Write )
            nidaq.DAQmxClearTask( self.taskHandle_Write )

        if self.taskHandle_Read.value != 0:
            nidaq.DAQmxStopTask(self.taskHandle_Read)
            nidaq.DAQmxClearTask(self.taskHandle_Read)
        # show()

    def clear(self):
        nidaq.DAQmxClearTask( self.taskHandle_Write )
        nidaq.DAQmxClearTask(self.taskHandle_Read)


if __name__=="__main__":
    #TODO: do stuff so we know it works
    print device["name"]

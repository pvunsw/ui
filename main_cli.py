class Test(gui.MyFrame1,OutPutData):
    #constructor
    measurement_type = 'Standard'
    def __init__(self,parent):
        #initialize parent class
        gui.MyFrame1.__init__(self,parent)

        self.Fig1 = CanvasPanel(self.Figure1_Panel)
        self.Fig1.labels('Raw Data','Time (s)','Voltage (V)')
        self.Data = array([ ])



        # CanvasPanel(self.Figure2_Panel)

    def Determine_Digital_Output_Channel(self):
        #Just a simple function choosing the correct output channel based on the drop down box
        if self.Channel=='High (2A/V)':
            Channel = r'ao0'
            Voltage_Threshold = self.Threshold/1840. #1840 comes from exp measurements


        elif self.Channel==r'Low (50mA/V)':
            Channel = r'ao1'
            Voltage_Threshold = self.Threshold/66. #66 comes from exp measurements
            # Voltage_Threshold = 0 #apparently this is an equiptment thing
        print self.Channel,self.Channel==r'Low (50mA/V)'

        return Channel,Voltage_Threshold

    def Save(self,event):
        #temp call to GetVAlues
        getattr(self,'GetValues_'+self.measurement_type)(event)

        self.Save_data(self.Data)
        data = self.Data
        # print info locals
        self.Save_Inf(self.Make_List_For_Inf_Save(event))

        event.Skip()


    def Load(self,event):

        List = self.Load_Inf()

        self.m_Intensity.SetValue(List['Intensity_v'])
        self.m_Threshold.SetValue(List['Threshold_mA'])
        self.m_Waveform.SetStringSelection(List['Waveform'])
        # print List['Waveform'],List['Channel']
        self.m_Output.SetStringSelection(List['Channel'])
        self.m_Averaging.SetValue(List['Averaging'])
        self.m_Binning.SetValue(List['Binning'])
        self.m_Offset_Before.SetValue(List['Offset_Before_ms'])
        self.m_Period.SetValue(List['Peroid_s'])
        self.m_Offset_After.SetValue(List['Offset_After_ms'])

        event.Skip()




    def GetValues_Standard(self,event):
        self.Intensity = self.CHK_float(self.m_Intensity,event)
        self.Binning = self.CHK_int(self.m_Binning,event)
        self.Averaging = self.CHK_int(self.m_Averaging,event)
        self.Peroid = self.CHK_float(self.m_Period,event) # TODO - spelling error? - dj
        self.Offset_Before= self.CHK_float(self.m_Offset_Before,event)
        self.Offset_After= self.CHK_float(self.m_Offset_After,event)
        self.Waveform = self.m_Waveform.GetStringSelection()
        self.Channel = self.m_Output.GetStringSelection()
        self.Threshold = self.CHK_float(self.m_Threshold,event)
        # print self.Binning
        # print self.lo
    def Make_List_For_Inf_Save(self,event):

        Intensity_v = self.CHK_float(self.m_Intensity,event)
        Threshold_mA = self.CHK_float(self.m_Threshold,event)
        Waveform = self.m_Waveform.GetStringSelection()
        Channel = self.m_Output.GetStringSelection()
        Averaging = self.CHK_int(self.m_Averaging,event)
        Binning = self.CHK_int(self.m_Binning,event)
        Offset_Before_ms= self.CHK_float(self.m_Offset_Before,event)
        Peroid_s = self.CHK_float(self.m_Period,event)
        Offset_After_ms= self.CHK_float(self.m_Offset_After,event)
        return locals()

    def Perform_Standard_Measurement(self,event):
        self.measurement_type = 'Standard'
        self.Perform_Measurement(event)
        self.PlotData()

    def Perform_Measurement(self,event):

        #this is what happens when the go button is pressed

        #first thing is all the inputs are grabbed
        #A check is performed, and if failed, event is skipped

        # print event.GetEventType()
        # print event.IsCommandEvent()
        # print event.GetId()


        getattr(self,'GetValues_'+self.measurement_type)(event)

        #find what channel we are using, and what the voltage offset then is
        Channel,Voltage_Threshold=self.Determine_Digital_Output_Channel()

        self.CHK_Voltage_Threshold(Voltage_Threshold,event)



        #This the event hasn't been skipped then continue with the code.
        self.m_scrolledWindow1.Refresh()
        if event.GetSkipped()==False:





            #Then the light pulse is defined, but the lightpulse class
            lightPulse = LightPulse(self.Waveform,self.Intensity,self.Offset_Before,self.Offset_After,self.Peroid,Voltage_Threshold)


            #We determine what channel to output on
            LP=lightPulse.Define()
            t = lightPulse.t

            #We put all that info into the take measurement section, which is a instance definition. There are also global variables that go into this
            Go = TakeMeasurements(LP,self.Averaging,Channel,t[-1])

            # Go.Measure()
            # print 'here'
            #USing that instance we then run the lights, and measure the outputs
            self.Data = self.Bin_Data(Go.Measure(),self.Binning)
            # self.Data = lightPulse.Define()
            #We then plot the datas, this has to be changed if the plots want to be updated on the fly.


            event.Skip()
        else:

            self.m_scrolledWindow1.Refresh()




    def PlotData(self,e=None):

        self.Fig1.clear()
        labels = ['Reference','PC','PL']
        # t = np.linspace(0,t[-1],self.Data.shape[0])
        colours = ['b','r','g']

        #this is done not to clog up the plot with many points
        if self.Data.shape[0]>1000:
            num = self.Data.shape[0]//1000
        else:
            num=1

        if self.ChkBox_PL.GetValue():
            self.Data[:,3] *=-1
        if self.ChkBox_PC.GetValue():
            self.Data[:,2] *=-1
        if self.ChkBox_Ref.GetValue():
            self.Data[:,1] *=-1


        #This plots the figure
        # print self.Data
        # print self.Data.shape,t.shape
        for i,label,colour in zip(self.Data[:,1:].T,labels,colours):
            # print i,label,colour,
            # print colour
            # print i.shape,t.shape
            self.Fig1.draw_points(self.Data[::num,0],i[::num],'.',Color=colour,Label = label)
            # self.Fig1.draw_line(t[::num],i[::num],'--',Color=colour,Label = label)
        self.Fig1.legend()
        self.Fig1.update()
        if e!=None:
            e.skip()



    def Bin_Data(self,data,BinAmount):


        if BinAmount ==1:
            return data
        #This is part of a generic binning class that I wrote.
        #IT lets binning occur of the first axis for any 2D or 1D array
        if len(data.shape)==1:
            data2 = zeros((data.shape[0]//BinAmount))
        else:
            data2 = zeros((data.shape[0]//BinAmount,data.shape[1]))


        for i in range(data.shape[0]//BinAmount):

            data2[i] = mean(data[i*BinAmount:(i+1)*BinAmount],axis=0)

        return data2

    def onChar(self, event):
        #This function is for ensuring only numerical values are placed inside the textboxes
        key = event.GetKeyCode()

        # print ord(key)
        acceptable_characters = "1234567890."
        if key<256 and key!=8:
            if chr(key) in acceptable_characters:
                event.Skip()
                return

            else:
                return False
        #This is for binding the F2 key to run
        elif key == 341:
            self.Run_Me(event)
            return
        else:
            event.Skip()
            return

    def Run_Me(self, event):
        #This function is for ensuring only numerical values are placed inside the textboxes
        key = event.GetKeyCode()

        if key==341:
            self.Perform_Measurement(event)
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
        elif key == 341:
            self.Run_Me(event)
            return
        else:
            event.Skip()
            return

    def Num_Data_Points_Update(self,event):
        #what is the point of this function?
        getattr(self,'GetValues_'+self.measurement_type)(event)
        time =self.Peroid+self.Offset_Before/1000+self.Offset_After/1000


        self.m_DataPoint.SetValue('{0:.2e}'.format((time*float32(DAQmx_InputSampleRate)/self.Binning)[0]))


        self.m_Frequency.SetValue('{0:3.3f}'.format(1./time))
        event.Skip()

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

    def CHK_Voltage_Threshold(self,Voltage_Threshold,event):
        if Voltage_Threshold > self.Intensity:
            self.m_Threshold.SetBackgroundColour('RED')
            event.Skip()
        else:
            self.m_Threshold.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ))

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

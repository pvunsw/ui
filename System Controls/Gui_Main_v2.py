# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Collect your data dude!", pos = wx.DefaultPosition, size = wx.Size( 1255,560 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"WaveForm" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Intensity (V)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Intensity = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u".5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Intensity, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"LED threshold\nCurrent (mA)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer1.Add( self.m_staticText9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_Threshold = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"150", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Threshold, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Voltage Current\nConverter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		m_OutputChoices = [ u"High (2A/V)", u"Low (50mA/V)" ]
		self.m_Output = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_OutputChoices, wx.CB_SORT )
		self.m_Output.SetSelection( 0 )
		gSizer1.Add( self.m_Output, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WaveFunction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_WaveformChoices = [ u"Cos", u"FrequencyScan", u"MJ", u"Sin", u"Square", u"Triangle" ]
		self.m_Waveform = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_WaveformChoices, wx.CB_SORT )
		self.m_Waveform.SetSelection( 2 )
		gSizer1.Add( self.m_Waveform, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Illumination\nperiod (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Period = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Period, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Frequency (Hz)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer1.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Frequency = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_Frequency.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer1.Add( self.m_Frequency, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Delay before\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Offset_Before = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Offset_Before, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Delta after\nillumination", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Offset_After = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Offset_After, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer2.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		sbSizer_Processing = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Processing" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Averaging", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer3.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Averaging = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_Averaging, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Binning", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Binning = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_Binning, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_Name = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Non Of Data\nPoints: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Name.Wrap( -1 )
		gSizer3.Add( self.m_Name, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DataPoint = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_DataPoint.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer3.Add( self.m_DataPoint, 0, wx.ALL, 5 )
		
		
		sbSizer_Processing.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer_Processing, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.GoButton = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GoButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.GoButton.SetBackgroundColour( wx.Colour( 98, 211, 22 ) )
		
		bSizer4.Add( self.GoButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_Save = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_Save, 0, wx.ALL, 5 )
		
		self.m_Load = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_Load, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Upside Down" ), wx.VERTICAL )
		
		gSizer31 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.ChkBox_Ref = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Reference Intensity", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.ChkBox_Ref, 0, wx.ALL, 5 )
		
		self.ChkBox_PC = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"PC Signal", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.ChkBox_PC, 0, wx.ALL, 5 )
		
		self.ChkBox_PL = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"PL Signal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ChkBox_PL.SetValue(True) 
		gSizer31.Add( self.ChkBox_PL, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( gSizer31, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer3 )
		self.m_scrolledWindow1.Layout()
		bSizer3.Fit( self.m_scrolledWindow1 )
		self.m_notebook1.AddPage( self.m_scrolledWindow1, u"Raw Measurement", True )
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"WaveForm" ), wx.VERTICAL )
		
		gSizer11 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText13 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Intensity (V)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer11.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Intensity1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_Intensity1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText111 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Voltage Current\nConverter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		gSizer11.Add( self.m_staticText111, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_Output1Choices = [ u"High (2A/V)", u"Low (50mA/V)" ]
		self.m_Output1 = wx.Choice( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_Output1Choices, wx.CB_SORT )
		self.m_Output1.SetSelection( 1 )
		gSizer11.Add( self.m_Output1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText101 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Wave Function", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		gSizer11.Add( self.m_staticText101, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		m_Waveform1Choices = [ u"Sin", u"Cos", u"MJ", u"Triangle", u"Square" ]
		self.m_Waveform1 = wx.Choice( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_Waveform1Choices, wx.CB_SORT )
		self.m_Waveform1.SetSelection( 0 )
		gSizer11.Add( self.m_Waveform1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText61 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Delay before\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gSizer11.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_Offset_Before1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_Offset_Before1, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )
		
		self.m_staticText71 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Delta after\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		gSizer11.Add( self.m_staticText71, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_Offset_After1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_Offset_After1, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )
		
		self.m_staticText51 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Illumination\nperiod Slow (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer11.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, 5 )
		
		self.m_Period1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_Period1, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Illumination\nPeriod Fast (us)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer11.Add( self.m_staticText34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, 5 )
		
		self.m_textCtrl28 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_textCtrl28, 0, wx.TOP, 5 )
		
		self.m_staticText121 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Frequency\nSlow (Hz)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		gSizer11.Add( self.m_staticText121, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_Frequency1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_Frequency1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer11.Add( self.m_Frequency1, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Frequency\nFast (Hz)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer11.Add( self.m_staticText35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_textCtrl29 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl29.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer11.Add( self.m_textCtrl29, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		sbSizer21.Add( gSizer11, 0, wx.EXPAND, 5 )
		
		
		bSizer31.Add( sbSizer21, 0, wx.EXPAND, 5 )
		
		sbSizer_Processing1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"Processing" ), wx.VERTICAL )
		
		gSizer32 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText81 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Averaging Slow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		gSizer32.Add( self.m_staticText81, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Averaging1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_Averaging1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText811 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Averaging Fast", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )
		gSizer32.Add( self.m_staticText811, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Averaging11 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_Averaging11, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Binning Slow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer32.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Binning1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_Binning1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText311 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Binning Fast", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		gSizer32.Add( self.m_staticText311, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Binning11 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_Binning11, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Name1 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Non Of Data\nPoints Slow: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Name1.Wrap( -1 )
		gSizer32.Add( self.m_Name1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DataPoint1 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_DataPoint1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer32.Add( self.m_DataPoint1, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_Name11 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Non Of Data\nPoints Fast: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Name11.Wrap( -1 )
		gSizer32.Add( self.m_Name11, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DataPoint11 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_DataPoint11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer32.Add( self.m_DataPoint11, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		sbSizer_Processing1.Add( gSizer32, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( sbSizer_Processing1, 0, wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button11 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button11.SetBackgroundColour( wx.Colour( 98, 211, 22 ) )
		
		bSizer41.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_Save1 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_Save1, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( bSizer41, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"Upside Down" ), wx.VERTICAL )
		
		gSizer311 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.ChkBox_Ref1 = wx.CheckBox( self.m_scrolledWindow5, wx.ID_ANY, u"Reference Intensity", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer311.Add( self.ChkBox_Ref1, 0, wx.ALL, 5 )
		
		self.ChkBox_PC1 = wx.CheckBox( self.m_scrolledWindow5, wx.ID_ANY, u"PC Signal", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer311.Add( self.ChkBox_PC1, 0, wx.ALL, 5 )
		
		self.ChkBox_PL1 = wx.CheckBox( self.m_scrolledWindow5, wx.ID_ANY, u"PL Signal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ChkBox_PL1.SetValue(True) 
		gSizer311.Add( self.ChkBox_PL1, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( gSizer311, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( sbSizer31, 0, wx.EXPAND, 5 )
		
		sbSizer_Processing11 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"Results" ), wx.VERTICAL )
		
		gSizer321 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.Static_text007 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Averaging Slow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Static_text007.Wrap( -1 )
		gSizer321.Add( self.Static_text007, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Averaging12 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_Averaging12, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText8111 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Averaging Fast", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8111.Wrap( -1 )
		gSizer321.Add( self.m_staticText8111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Averaging111 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_Averaging111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText312 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Binning Slow", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText312.Wrap( -1 )
		gSizer321.Add( self.m_staticText312, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Binning12 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_Binning12, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText3111 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Binning Fast", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )
		gSizer321.Add( self.m_staticText3111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Binning111 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_Binning111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Name12 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Non Of Data\nPoints Slow: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Name12.Wrap( -1 )
		gSizer321.Add( self.m_Name12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DataPoint12 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_DataPoint12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer321.Add( self.m_DataPoint12, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_Name111 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Non Of Data\nPoints Fast: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Name111.Wrap( -1 )
		gSizer321.Add( self.m_Name111, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DataPoint111 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"XX", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_DataPoint111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		gSizer321.Add( self.m_DataPoint111, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		sbSizer_Processing11.Add( gSizer321, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( sbSizer_Processing11, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow5.SetSizer( bSizer31 )
		self.m_scrolledWindow5.Layout()
		bSizer31.Fit( self.m_scrolledWindow5 )
		self.m_notebook1.AddPage( self.m_scrolledWindow5, u"PLCalibration-Self Cosistant", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.Figure1_Panel = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Figure1_Panel, 1, wx.ALIGN_CENTER_VERTICAL| wx.GROW ,5)
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
  
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_scrolledWindow1.Bind( wx.EVT_CHAR, self.Run_Me )
		self.m_Intensity.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Intensity.Bind( wx.EVT_TEXT, self.CurrentLimits )
		self.m_Output.Bind( wx.EVT_CHOICE, self.CurrentLimits )
		self.m_Period.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Period.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Offset_Before.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Offset_Before.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Offset_After.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Offset_After.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Averaging.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.GoButton.Bind( wx.EVT_BUTTON, self.Perform_Standard_Measurement )
		self.m_Save.Bind( wx.EVT_BUTTON, self.Save )
		self.m_Load.Bind( wx.EVT_BUTTON, self.Load )
		self.ChkBox_Ref.Bind( wx.EVT_CHECKBOX, self.PlotData )
		self.ChkBox_PC.Bind( wx.EVT_CHECKBOX, self.PlotData )
		self.ChkBox_PL.Bind( wx.EVT_CHECKBOX, self.PlotData )
		self.m_Intensity1.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Intensity1.Bind( wx.EVT_TEXT, self.CurrentLimits )
		self.m_Output1.Bind( wx.EVT_CHOICE, self.CurrentLimits )
		self.m_Offset_Before1.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Offset_Before1.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Offset_After1.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Offset_After1.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Period1.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Period1.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Averaging1.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Averaging11.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning1.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning1.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Binning11.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning11.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_button11.Bind( wx.EVT_BUTTON, self.Perform_Measurement )
		self.m_Save1.Bind( wx.EVT_BUTTON, self.Save )
		self.m_Averaging12.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Averaging111.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning12.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning12.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
		self.m_Binning111.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Binning111.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Run_Me( self, event ):
		event.Skip()
	
	def onChar( self, event ):
		event.Skip()
	
	def CurrentLimits( self, event ):
		event.Skip()
	
	
	
	def Num_Data_Points_Update( self, event ):
		event.Skip()
	
	
	
	
	
	def onChar_int( self, event ):
		event.Skip()
	
	
	
	def Perform_Standard_Measurement( self, event ):
		event.Skip()
	
	def Save( self, event ):
		event.Skip()
	
	def Load( self, event ):
		event.Skip()
	
	def PlotData( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def Perform_Measurement( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	


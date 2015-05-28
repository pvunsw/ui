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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Collect your data dude!", pos = wx.DefaultPosition, size = wx.Size( 1200,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer_WaferForm = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"WaveForm" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Voltage Current\nConverter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		m_OutputChoices = [ u"High (2A/V)", u"Low (50mA/V)" ]
		self.m_Output = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_OutputChoices, wx.CB_SORT )
		self.m_Output.SetSelection( 0 )
		gSizer2.Add( self.m_Output, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WaveFunction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer2.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		m_WaveformChoices = [ u"Sin", u"Cos", u"MJ", u"Triangle", u"Square" ]
		self.m_Waveform = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_WaveformChoices, wx.CB_SORT )
		self.m_Waveform.SetSelection( 0 )
		gSizer2.Add( self.m_Waveform, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Illumination\ndelay (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer2.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_Offset_Before = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Offset_Before.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gSizer2.Add( self.m_Offset_Before, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Measurement\noffset (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer2.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_Offset_After = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_Offset_After, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer_WaferForm.Add( gSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer_WaferForm, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Measurement" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Intensity (V)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Intensity = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u".5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Intensity, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Binning", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Binning = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Binning, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Illumination\nperiod (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Period = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Period, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Averaging", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer1.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
		
		self.m_Averaging = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_Averaging, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer2.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer2, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_button1 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button1.SetBackgroundColour( wx.Colour( 98, 211, 22 ) )
		
		bSizer4.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer4 )
		self.m_scrolledWindow1.Layout()
		bSizer4.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.Figure1_Panel = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Figure1_Panel, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_Offset_Before.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Offset_After.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Intensity.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Intensity.Bind( wx.EVT_TEXT, self.CurrentLimits )
		self.m_Binning.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_Period.Bind( wx.EVT_CHAR, self.onChar )
		self.m_Averaging.Bind( wx.EVT_CHAR, self.onChar_int )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Perform_Measurement )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onChar( self, event ):
		event.Skip()
	
	
	
	def CurrentLimits( self, event ):
		event.Skip()
	
	def onChar_int( self, event ):
		event.Skip()
	
	
	
	def Perform_Measurement( self, event ):
		event.Skip()
	


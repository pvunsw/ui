import sys,  os

from numpy import *
from matplotlib import  *


from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from matplotlib.colors import Normalize
from matplotlib.cm import  ScalarMappable,get_cmap

import wx


    ## Updates
    ##  1. Added          axes.set_autoscale_on(True)         axes.relim()         axes.autoscale_view(True,True,True) too log buttons to auto scale them
    ##



class CanvasPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()


        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.figure.tight_layout()
        
        # x = array([0,.5,1])
        # y = array([0,.5,1])
        # self.draw_points(x,y)
        
        #self.canvas.draw()
        #self.canvas.updateGeometry()



        self.chart_toolbar = MyCustomToolbar(self.canvas)
        tw, th = self.chart_toolbar.GetSizeTuple()
        fw, fh = self.canvas.GetSizeTuple()

        self.chart_toolbar.SetSize(wx.Size(fw, th))
        self.chart_toolbar.Realize()


        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.canvas, 0, wx.LEFT | wx.TOP | wx.BOTTOM| wx.GROW)
        self.sizer.Add(self.chart_toolbar, 1, wx.LEFT | wx.BOTTOM| wx.TOP | wx.GROW)



        self.SetSizerAndFit(self.sizer)

        self.Fit()
#        self.Layout()

        Cursor(self.axes, useblit=True, color='red', linewidth=1 )

    def draw_points(self,x,y,Plottype='^',Label='',Color='k',Linewidth=0):
        self.axes.plot(x, y,color=Color,marker=Plottype,linewidth=Linewidth,label=Label,markeredgecolor='k',markersize=5)

    def draw_line(self,x,y,Linestyle='-',Label='',Color='k',Linewidth=3):
        self.axes.plot(x, y,color=Color,linestyle=Linestyle,linewidth=Linewidth,label=Label,markeredgecolor='k',markersize=5)

    def legend(self):
        self.axes.legend(loc=0)

    def clear(self):
        
        xlabel = self.axes.get_xlabel()
        ylabel = self.axes.get_ylabel()
        title = self.axes.get_title()

        self.xscale = self.axes.get_xscale()
        self.yscale = self.axes.get_yscale()

        self.axes.cla()
        self.labels(title,xlabel,ylabel)


    def update(self):

        self.figure.tight_layout()
        self.axes.set_xscale(self.xscale)
        self.axes.set_yscale(self.yscale)
        self.canvas.draw()


    def loglog(self):
        self.axes.loglog()


    def semilogx(self):
        self.axes.semilogx()



    def labels(self,title, xlabel,ylabel):
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.grid(True,'both')

    def Axes(self,xmin,xmax,ymin,ymax):


        self.axes.set_xlim(xmin,xmax)

        self.axes.set_ylim(ymin,ymax)


class MyCustomToolbar(NavigationToolbar2Wx):
    X_SCALE_SWITCH  = wx.NewId()
    Y_SCALE_SWITCH = wx.NewId()

    def __init__(self, plotCanvas):
        # create the default toolbar
        NavigationToolbar2Wx.__init__(self, plotCanvas)
        # add new toolbar buttons
        temp =os.getcwd()

       
        self.AddSimpleTool(self.X_SCALE_SWITCH, wx.Image('Logy.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'x Log Lin Toggle', 'Switch the x-axis between log and linear scale',isToggle=0)
        wx.EVT_TOOL(self, self.X_SCALE_SWITCH, self._x_scale_Log_Lin)
        self.AddSimpleTool(self.Y_SCALE_SWITCH, wx.Image('Logx.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'y Log Lin Toggle', 'Switch the y-axis between log and linear scale',isToggle=0)
        os.chdir(temp)

        wx.EVT_TOOL(self, self.Y_SCALE_SWITCH, self._y_scale_Log_Lin)
        
    # pan the graph to the left
    def _x_scale_Log_Lin(self, evt):
        ONE_SCREEN = 1
        axes = self.canvas.figure.axes[0]
        if(axes.get_xscale()=='log'):
            axes.set_xscale("linear")

            xmin,xmax=axes.get_xlim()
            axes.set_xlim(0,xmax)

        else:
            axes.set_xscale("log")
            #autoscale(enable=True, axis='both', tight=True)
        axes.set_autoscale_on(True)
        axes.relim()
        axes.autoscale_view(True,True,True)
        self.canvas.draw()
        
    # pan the graph to the right
    def _y_scale_Log_Lin(self, evt):
        ONE_SCREEN = 1
        axes = self.canvas.figure.axes[0]
        if(axes.get_yscale()=='log'):
            axes.set_yscale("linear")
            ymin,ymax=axes.get_ylim()
            axes.set_ylim(0,ymax)

        else:
            axes.set_yscale("log")
        axes.set_autoscale_on(True)
        axes.relim()
        axes.autoscale_view(True,True,True)
        self.canvas.draw()


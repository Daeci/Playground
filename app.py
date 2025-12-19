import wx
from panels import HomePage, AoC2025Page

#globals
X_BORDER_PX = 5
Y_BORDER_PX = 5

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Playground', size=wx.Size(1280, 720))
        self.Center()
        navbar = wx.Notebook(self)

        # pages to add to navbar
        home_panel = HomePage(navbar)
        aoc2025_panel = AoC2025Page(navbar)
        bdo_panel = wx.Panel(navbar)
        ffxiv_panel = wx.Panel(navbar)

        # add all added pages to notebook with labels
        navbar.AddPage(home_panel, "Home")
        navbar.AddPage(aoc2025_panel, "AoC 2025")
        navbar.AddPage(bdo_panel, "BDO Market Info")
        navbar.AddPage(ffxiv_panel, "FFXIV Market Info")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(navbar, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SignCheckerGui:
    
  def __init__( self ):
    self.builder = Gtk.Builder()
    self.builder.add_from_file("SignFinderGui.glade")

    self.window = self.builder.get_object("MainWindow")
    self.window.connect("delete-event", Gtk.main_quit)

    self.number = self.builder.get_object("number")
    self.result = self.builder.get_object("result")
     
    signals = {
        "FindSign_clicked_cb" : self.FindSign_clicked_cb,
    }

    self.builder.connect_signals( signals)

  def FindSign_clicked_cb(self, widget):
    if (self.number.get_text() == ""):
       self.result.set_text("You didn't enter anything. Enter something before clicking 'Find Sign'")
    else: 
       numStr = self.number.get_text()
       try: 
         num = float(numStr)
         resultStr = "The number " + numStr + " is "   
         if (num > 0):
             resultStr += "positive"
         elif ( num < 0):
             resultStr += "negative"
         else:
             resultStr += "signless"
         resultStr += "!"
         self.result.set_text(resultStr)
       except ValueError:
           self.result.set_text("Your entry of " + numStr + "doesn't appear to be a number")

signCheckerGui = SignCheckerGui()
curWindow = signCheckerGui.window
curWindow.show_all()

Gtk.main()

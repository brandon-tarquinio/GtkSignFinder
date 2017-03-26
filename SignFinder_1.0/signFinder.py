from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Sign Finder 1.0")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)

        # instructions
        introMesg = Gtk.Label("Enter a number below and we will do the hard work of checking it's sign for you!")
        introMesg.set_line_wrap(True)
        vbox.pack_start(introMesg, True, True, 0)

        # Box for number and button
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        vbox.pack_start(hbox, True, True, 0)

        # Result area
        self.result = Gtk.Label()
        vbox.pack_start(self.result, True, True, 0)

        # number Input Box 
        self.number = Gtk.Entry()
        hbox.pack_start(self.number, True, True, 0)

        #Find sign button
        self.FindSign= Gtk.Button(label="Find Sign")
        self.FindSign.connect("clicked", self.findSign_cb)
        hbox.pack_start(self.FindSign, True, True, 0)

    def findSign_cb(self, widget):
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


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

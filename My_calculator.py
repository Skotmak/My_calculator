from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "600")
Config.set("graphics", "height", "300")

saveinput = ""
saveres=""
prom=""
f=""
t=""
class calcapp(App):
    def calculate(self, symbol):
        global saveinput
        global saveres
        global prom
        global t
        prom=self.result.text      
        f = open('calculations.txt', 'a')
        if symbol.text is 'C':
            saveinput = self.result.text = ""
        elif symbol.text is not '=':
            self.result.text += symbol.text
            saveinput += symbol.text
        else:
            try:
                saveinput = self.result.text = str(eval(saveinput))
                saveres = self.list.text = t+saveres + prom + "=" + str(eval(saveinput)) + "\n"
                f.write(t+saveres)
                f.close()
            except: saveinput = self.result.text = ""
            
    def build(self):
        global saveres
        global f
        global t
        root = BoxLayout(orientation = "horizontal", padding=5)
        bn = BoxLayout(orientation = "vertical", padding = 5)
            
        self.result = TextInput(
            text = "", readonly = True, font_size = 25,
            size_hint = [1,.75], background_color = [1,1,1,.8])
        bn.add_widget(self.result)

        allbuttons=GridLayout(cols=5)
        allbuttons.add_widget(Button(text="7", on_press=self.calculate))
        allbuttons.add_widget(Button(text="8", on_press=self.calculate))
        allbuttons.add_widget(Button(text="9", on_press=self.calculate))
        allbuttons.add_widget(Button(text="+", on_press=self.calculate))
        allbuttons.add_widget(Button(text="C", on_press=self.calculate, background_color=[1,.02,.03,1],background_normal=''))

        allbuttons.add_widget(Button(text="4", on_press=self.calculate))
        allbuttons.add_widget(Button(text="5", on_press=self.calculate))
        allbuttons.add_widget(Button(text="6", on_press=self.calculate))
        allbuttons.add_widget(Button(text="-", on_press=self.calculate))
        allbuttons.add_widget(Button(text="(", on_press=self.calculate))

        allbuttons.add_widget(Button(text="1", on_press=self.calculate))
        allbuttons.add_widget(Button(text="2", on_press=self.calculate))
        allbuttons.add_widget(Button(text="3", on_press=self.calculate))
        allbuttons.add_widget(Button(text="*", on_press=self.calculate))
        allbuttons.add_widget(Button(text=")", on_press=self.calculate))

        allbuttons.add_widget(Button(text="0", on_press=self.calculate))
        allbuttons.add_widget(Button(text=".", on_press=self.calculate))
        allbuttons.add_widget(Button(text="=", on_press=self.calculate,background_color=[.08,.5,0,1],background_normal=''))
        allbuttons.add_widget(Button(text="/", on_press=self.calculate))
        allbuttons.add_widget(Button(text="%", on_press=self.calculate))
        bn.add_widget(allbuttons)

        self.list = TextInput(
            text = "", readonly = True, font_size = 25,
            size_hint = [1,1], background_color = [1,1,1,1])        
        root.add_widget(bn)
        root.add_widget(self.list)
        f = open('calculations.txt', 'r')
        t=self.list.text=f.read()
        f.close()
        return root
        
if __name__ == "__main__":
    calcapp().run()
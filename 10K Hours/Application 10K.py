from kivy.app import App
from  kivy.uix.button import Button 
from kivy.config import Config
from  kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
Window.clearcolor = (.37,.50,.69, 1)
Config.set('graphics', 'width', '240')
Config.set('graphics', 'height', '240')

def on_enter(instance, value):
    return btn_press1(self)

class WayToTheTopApp(App):
	def build(self):
		f1 = BoxLayout(orientation='vertical', padding = [10], spacing = 5)
		self.st_label = Label(text = "Worked in Sublime today:")
		self.ct_label = Label(text = "C++ programmed today:")
		self.pt_label = Label(text = "Python programmed today:")
		self.pc_label = Label(text = "Common Python programming hours:")
		self.cc_label = Label(text = "Common C++ programming hours:")
		self.tc_label = Label(text = "Total programming hours:")
		f1.add_widget(self.st_label)
		f1.add_widget(self.ct_label)
		f1.add_widget(self.pt_label)
		f1.add_widget(self.pc_label)
		f1.add_widget(self.cc_label)
		f1.add_widget(self.tc_label)
		return f1

if __name__ == "__main__":
	WayToTheTopApp().run()
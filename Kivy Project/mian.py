from kivy.app import App
from  kivy.uix.button import Button 
from kivy.config import Config
from  kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
Window.clearcolor = (.37,.50,.69, 1)
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '920')

def on_enter(instance, value):
    return btn_press1(self)

class ToneApp(App):
	def build(self):
		mark = [0.0 , 0.0]
		f1 = BoxLayout(orientation='vertical', padding = [50], spacing = 25)
		f1.add_widget(Label(text = "[anchor=title1][size=24] Введите любую фразу (более одого слова), чтобы получить её эмоциональную оценку: [/size]"))
		self.text1 =TextInput(text = '', multiline = False)
		f1.add_widget(self.text1)
		f1.bind(on_text_validate=on_enter)
		f1.add_widget(Button(text = "Отправить", 
					font_size = 30, 
					on_press = self.btn_press1,
					background_color = [.17,.12,.69,1],
					background_normal = ''));
		self.main_label = Label(text = 'Здесь будет ваш результат {}'.format(mark))
		f1.add_widget(self.main_label)
		return f1

	def btn_press1(self, instance):
		from client import send_to_server
		mark = str(send_to_server(self.text1.text)).split(',')
		percent = mark[0].split('[')
		accuracity = mark[1].split(']')
		p = float(percent[1])*100
		a = float(accuracity[0])*100
		if(p > 10.):
			if(p > 40.):
				if(p > 60.):
					if(p > 75.):
						self.main_label.text = 'Ваша фраза оценивается на как крайне негативная ({}% негативности).\nСистема уверена в этом на {}%'.format(round(p,4),round(a,4))
					else:
						self.main_label.text = 'Ваша фраза оценивается на как негативная ({}% негативности). \nСистема уверена в этом на {}%'.format(round(p,4),round(a,4))
				else:
					self.main_label.text = 'Ваша фраза оценивается на как нейтральная ({}% негативности). \nСистема уверена в этом на {}%'.format(round(p,4),round(a,4))
			else:
				self.main_label.text = 'Ваша фраза оценивается на как положительная ({}% негативности). \nСистема уверена в этом на {}%'.format(round(p,4),round(a,4))
		else:		
			self.main_label.text = 'Ваша фраза оценивается на как очень положительная ({}% негативности). \nСистема уверена в этом на {} %'.format(round(p,4),round(a,4))

if __name__ == "__main__":
	ToneApp().run()
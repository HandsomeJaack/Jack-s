from kivy.app import App
from  kivy.uix.button import Button 
from kivy.config import Config
from  kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

Window.clearcolor = (.37,.50,.69, 1)
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '920')

def on_enter(instance, value):
    print('User pressed enter in', instance)

class ToneApp(App):
	def build(self):

		f1 = BoxLayout(orientation='vertical', padding = [50], spacing = 25)
		f1.add_widget(TextInput(text = 'Введи сообщение для анализа', multiline = False))
		f1.bind(on_text_validate=on_enter)
		f1.add_widget(Button(text = "Отправить", 
					font_size = 30, 
					on_press = self.btn_press1,
					background_color = [.17,.12,.69,1],
					background_normal = ''));
		f1.add_widget(Button(text = "Получить", 
					font_size = 30, 
					on_press = self.btn_press2,
					background_color = [.17,.12,.69,1],
					background_normal = ''));
		return f1

	def btn_press1(self, instance):
		instance.text = "Отправлено!"

	def btn_press2(self, instance):
		instance.text = "Получено!"

if __name__ == "__main__":
	ToneApp().run()
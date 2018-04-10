from kivy.app import App
from  kivy.uix.button import Button 

class MyApp(App):
	def build(self):
		return Button(text = "This is my first button!",
				front_size = 30,
				on_press =self.btn_press,
				backgrond_color = [1,0,0,1],
				backgrond_normal = '')

	def btn_press(self,instance):
		instance.text = 'I am done!'

if __name__ == "__main__":
	MyApp().run()
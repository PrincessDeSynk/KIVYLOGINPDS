from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from database import Database



class WindowManager(ScreenManager):
	pass


class MainWindow(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)
	def invalid_popup(self):
		win = FloatLayout()
		win.add_widget(Label(text ="Invalid Username/Password",size_hint =(0.6,0.2),pos_hint = {"x":0.2,"y":0.65}))
		bt =Button(text = "Exit",size_hint =(0.8,0.2),pos_hint = {"x":0.1,"y":0.05})
		win.add_widget(bt)		
		popupwindow = Popup(title = "Success",content =win , size_hint =(None,None),size =(400,400), auto_dismiss =False)
		popupwindow.open()
		bt.bind(on_press = popupwindow.dismiss)


	def verification(self):
		D = Database()
		D.create("entries")
		L=D.check(self.username.text,self.password.text)
		if L[0]==0:
			self.invalid_popup()
		else:
			self.username.text=''
			self.password.text=''	
		return L[0]

		
class LoginWindow(Screen):
	pass



class SigninWindow(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)
	email =ObjectProperty(None)
	def create_account(self):
		if self.username.text != '' and self.password.text!= '' and self.email.text!= '':
			f = Database()
			f.create("entries")
			f.datainput(self.username.text,self.password.text,self.email.text)
			self.username.text = ""
			self.password.text = ""
			self.email.text =""
			state =1
		else:
			state =0	
		signin_pop(state)



def signin_pop(created):
	if created == 1:
		win = FloatLayout()
		win.add_widget(Label(text ="Account Created !",size_hint =(0.6,0.2),pos_hint = {"x":0.2,"top":1}))
		bt =Button(text = "Exit",size_hint =(0.8,0.2),pos_hint = {"x":0.1,"y":0.05})
		win.add_widget(bt)		
		popupwindow = Popup(title = "Success",content =win , size_hint =(None,None),size =(400,400), auto_dismiss =False)
		popupwindow.open()
		bt.bind(on_press = popupwindow.dismiss)
	else:
		win = FloatLayout()
		win.add_widget(Label(text ="Please fill all entries !",size_hint =(0.6,0.2),pos_hint = {"x":0.2,"top":1}))
		bt =Button(text = "Exit",size_hint =(0.8,0.2),pos_hint = {"x":0.1,"y":0.05})
		win.add_widget(bt)		
		popupwindow = Popup(title = "Failure",content =win , size_hint =(None,None),size =(400,400), auto_dismiss =False)
		popupwindow.open()
		bt.bind(on_press = popupwindow.dismiss)			
		



kv = Builder.load_file("log.kv")

class LoginApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	LoginApp().run()
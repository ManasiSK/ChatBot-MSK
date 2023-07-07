import pyttsx3
import speech_recognition as sprecon
import webbrowser
import datetime
import os
import time


def spToTxt():
	recognizer= sprecon.Recognizer() 	  				#creating an object
	with sprecon.Microphone() as source:   				#class to use microphone
		print("Listening...!!!")		  				#print msg on screen
		recognizer.adjust_for_ambient_noise(source)     #removing noise from source
		audio = recognizer.listen(source)				#listening of instr from source
		try:
			print("Recognizing....")
			data = recognizer.recognize_google(audio)	#using google recognizer
			print(data)
			return data
		except sprecon.UnknownValueError:					#when voice is not audible properly / there's no one speaking
			print("!!..Voice not Audible..!!")


def txtToSp(x):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')     			#to determine which voice is to be chosen
	engine.setProperty('voice',voices[1].id) 			#'0' for male voice , '1' for female
	rate = engine.getProperty('rate')		 			#speed for voice
	engine.setProperty('rate',120)
	engine.say(x)
	engine.runAndWait()


if __name__ == '__main__':

	if "hello" in spToTxt().lower():

			while True: 
					data1 = spToTxt().lower()

					if "your name" in data1:
						name = "my name is alice"
						txtToSp(name)

					elif "old are you" in data1:
						age = "i am 25 years old"
						txtToSp(age)

					elif "time" in data1:
						time = datetime.datetime.now().strftime("%I%M%p")   #only time required- 'I' for hrs,'M' for min,'p' for am/pm
						txtToSp(time)

					elif "google" in data1:
						webbrowser.open("chrome://newtab/")

					elif "youtube" in data1:
						webbrowser.open("https://www.youtube.com/")

					elif "mail" in data1:
						webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

					elif "linkedin" in data1:
						webbrowser.open("https://www.linkedin.com/in/manasi-kulkarni-15860b224/")

					elif "instagram" in data1:
						webbrowser.open("https://www.instagram.com/")

					elif "play song" in data1:
						address = "E:\FE\Photos\Songs"
						listSongs = os.listdir(address)
						print(listSongs)
						os.startfile(os.path.join(address,listSongs[96]))

					elif "exit" in data1:
						txtToSp("thank you")
						break

					time.sleep(5)


	else:
		print("thank you")

		

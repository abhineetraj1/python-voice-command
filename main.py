import speech_recognition as sr
import pyttsx3
import datetime
import os
import platform

def m():
	gh = sr.Recognizer()
	with sr.Microphone() as source:
		e = gh.record(source, duration=5)
		print("listening...")
		try:
			print("Processing...")
			c=gh.recognize_google(e)
			gu(c)
		except:
			sleep(1)
	if (platform.system() == "Windows"):
		os.system("cls")
	else:
		os.system("clear")


def gu(te):
	y=[]
	for i in ["date","time"]:
		if (i in te):
			if (i == "date"):
				y.append(date_today())
			elif (i == "time"):
				y.append(time_now())
			else:
				y=y
	r=te
	p = open("data.ar","r").read().split("\n")
	for i in p:
		if (i.split(":")[0] in r):
			cr = i.split(":")[1]
			if (len(cr) == 0):
				y.append("Sorry I am not able to understand. Try again with other voice command")
			else:
				y.append(cr)
	for i in y:
		if (len(i) > 1):
			pyttsx3.speak(i)


def date_today():
	t = str(datetime.datetime.now()).split()[0].split("-")
	mn = ["January","febuary","march","april","may","june","july","august","september","october","november","december"]
	return "today is "+mn[int(t[1])-1] +" "+t[2] +" "+ t[0]

def time_now():
	t = str(datetime.datetime.now()).split()[1].split(".")[0].split(":")
	p = ""
	if (int(t[0]) < 12):
		p = str(t[0]) + " " + t[1] +" A M "
	else:
		p = str(int(t[0])-12) + " " + t[1] + " P M "
	return " Time is "+p

while True:
	m()
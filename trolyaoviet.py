import speech_recognition
import playsound
import webbrowser
from gtts import gTTS
import subprocess,json,time
import requests
import os	
may_nghe = speech_recognition.Recognizer()
b ="sever"
r = requests.get('https://api.npoint.io/365dfdd4fe77a000f2d2')
r = json.loads(r.text)
try:
	key = r[b]
	if key == True:
		print("Connected to sever is successfully")
		time.sleep(1)
		print("sever is open")
		time.sleep(1)
		print("Loading...!")
		time.sleep(1)
		print("Sever sẽ đóng vào 12h đêm đến 7h sáng mỗi ngày để bảo trì")
		while True:
			print("""
_________    __           .__   __________
\_   ___ \ _/  |_ _______ |  |  \____    /
/    \  \/ \   __\\_  __ \|  |    /     / 
\     \____ |  |   |  | \/|  |__ /     /_ 
 \_______/ |__|   |__|   |____//_________\
                                       

""")
			with speech_recognition.Microphone() as mic:
				print("Sen: tớ đang nghe nè")
				audio = may_nghe.record(mic, duration=7)
				may_nghe.adjust_for_ambient_noise(mic) 
				print("Sen:tớ đang suy nghĩ nha ...")
			try:
				you = may_nghe.recognize_google(audio,language="vi-VI")
			except:
				you == ""
				print("Bạn: " + you)
			if you == "":
				nao_may = "tôi không nghe thấy bạn vui lòng thử lại nha"
			elif "chào" in you:
				nao_may = "Xin chào cậu chủ, chúc cậu chủ một ngày tốt đẹp nha"
			if " YouTube" in you.lower():
				nao_may = "Được thôi"	
				url = "https://www.youtube.com/"
				runprf = webbrowser.open_new_tab(url)
			if "Mở Facebook" in you.lower():
				nao_may = "Dễ mà"	
				url = "https://www.facebook.com/"
				runprf = webbrowser.open_new_tab(url)
			if "Mở bản tin" in you.lower():
				nao_may = "Dễ mà"	
				url = "https://thanhnien.vn/"
				runprf=webbrowser.open_new_tab(url)
			if "Mở Google dịch" in you.lower():
				nao_may = "Dễ ợt"	
				url = "https://translate.google.com/?hl=vi#view=home&op=translate&sl=en&tl=vi"
				runprf = webbrowser.open_new_tab(url)
			elif "bạn có thể đọc suy nghĩ hiện tại của tôi không" in you:
				nao_may="có chứ"
			if "vậy suy nghĩ của tôi là gì vậy" in you:
				nao_may="nhóc con"
			elif "Tạm biệt" in you:
				nao_may= "Tạm biệt cậu chủ nha "	
				print("Sen: " + nao_may)
				output = gTTS(nao_may,lang="vi", slow=False)
				output.save("output.mp3")
				playsound.playsound('output.mp3', True)
				break
			print("Bạn : "+you)
			print("Sen: " + nao_may)
			output = gTTS(nao_may,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3', True)
	elif key == False:
		print("""Máy chủ đã đóng để bảo trì vui lòng quay lại sau nếu tool lỗi xin liên hệ
SĐT:0372108501 
FB:https://www.facebook.com/PCTPC57/""")
		time.sleep(10)
except:
	print("""Máy chủ đã đóng để bảo trì vui lòng quay lại sau nếu tool lỗi xin liên hệ
SĐT:0372108501 
FB:https://www.facebook.com/PCTPC57/""")
	time.sleep(10)


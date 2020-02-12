#音声とイラストと意味

from PIL import Image
import cv2
import sys
import pyocr
import pyocr.builders
import pyocr
from mutagen.mp3 import MP3 as mp3
import pygame
import time
from PIL import Image
import azure.cognitiveservices.speech as speechsdk
import re
import cv2
import random
import time
import msvcrt
import numpy as np
from operator import itemgetter
import tkinter as tk
from PIL import Image, ImageTk
from win32api import GetSystemMetrics

word_num = 60
score = [0] * (word_num+1)
word = {}
new_word = {}
new_score = {}
test_score = [0] * 10

#word[] = [単語0、音声1、イラスト2、テキスト画像3、意味4、認識単語5、説明6、カタカナ7]

#音声とイラストと意味 

word[0] = (["Liability",r'practice_sound\\liability.mp3', r'practice_image\\liability.png', r'practice_text\\liability_text.png', r'practice_imi\\liability_imi.png',"Liability.", r'practice_description\\liability_des.png' , r'practice_katakana\\liability_kata.png'])
word[1] = (["Contraband",r'practice_sound\\contraband.mp3', r'practice_image\\contraband.png', r'practice_text\\contraband_text.png', r'practice_imi\\contraband_imi.png',"Contraband.", r'practice_description\\contraband_des.png', r'practice_katakana\\contraband_kata.png'])
word[2] = (["Stem",r'practice_sound\\stem.mp3', r'practice_image\\stem.png', r'practice_text\\stem_text.png' ,'practice_imi\\stem_imi.png',"Stem.", r'practice_description\\stem_des.png', r'practice_katakana\\stem_kata.png'])
word[3] = (["Indiscretion",r'practice_sound\\indiscretion.mp3', r'practice_image\\indiscretion.png', r'practice_text\\indiscretion_text.png','practice_imi\\indiscretion_imi.png',"Indiscretion.", r'practice_description\\indiscretion_des.png', r'practice_katakana\\indiscretion_kata.png'])
word[4] = (["Gorge",r'practice_sound\\gorge.mp3', r'practice_image\\gorge.png', r'practice_text\\gorge_text.png','practice_imi\\gorge_imi.png',"Gorge.", r'practice_description\\gorge_des.png', r'practice_katakana\\gorge_kata.png'])
word[5] = (["Rampage",r'practice_sound\\rampage.mp3', r'practice_image\\rampage.png', r'practice_text\\rampage_text.png' ,'practice_imi\\rampage_imi.png',"Rampage.", r'practice_description\\rampage_des.png', r'practice_katakana\\rampage_kata.png'])
word[6] = (["Libel",r'practice_sound\\libel.mp3', r'practice_image\\libel.png', r'practice_text\\libel_text.png' ,'practice_imi\\libel_imi.png',"Libel.", r'practice_description\\libel_des.png', r'practice_katakana\\libel_kata.png'])
word[7] = (["Prodigy",r'practice_sound\\prodigy.mp3', r'practice_image\\prodigy.png', r'practice_text\\prodigy_text.png' ,'practice_imi\\prodigy_imi.png',"Prodigy.", r'practice_description\\prodigy_des.png', r'practice_katakana\\prodigy_kata.png'])
word[8] = (["Incentive",r'practice_sound\\incentive.mp3', r'practice_image\\incentive.png', r'practice_text\\incentive_text.png' ,'practice_imi\\incentive_imi.png', "Incentive.", r'practice_description\\incentive_des.png', r'practice_katakana\\incentive_kata.png'])
word[9] = (["Reversal",r'practice_sound\\reversal.mp3', r'practice_image\\reversal.png', r'practice_text\\reversal_text.png' ,'practice_imi\\reversal_imi.png', "Reversal.", r'practice_description\\reversal_des.png', r'practice_katakana\\reversal_kata.png'])

#音声とイラストと意味とカタカナ(word[i][1], word[i][2], word[i][5], word[i][8]) 


word[10] = (["Speculation",r'practice_sound\\speculation.mp3', r'practice_image\\speculation.png', r'practice_text\\speculation_text.png', r'practice_imi\\speculation_imi.png',"Speculation.", r'practice_description\\speculation_des.png' , r'practice_katakana\\speculation_kata.png'])
word[11] = (["Benchmark",r'practice_sound\\benchmark.mp3', r'practice_image\\benchmark.png', r'practice_text\\benchmark_text.png', r'practice_imi\\benchmark_imi.png',"Benchmark.",  r'practice_description\\benchmark_des.png', r'practice_katakana\\benchmark_kata.png'])
word[12] = (["Recipient",r'practice_sound\\recipient.mp3', r'practice_image\\recipient.png', r'practice_text\\recipient_text.png' ,'practice_imi\\recipient_imi.png',"Recipient.", r'practice_description\\recipient_des.png', r'practice_katakana\\recipient_kata.png'])
word[13] = (["Integration",r'practice_sound\\integration.mp3', r'practice_image\\integration.png', r'practice_text\\integration_text.png','practice_imi\\integration_imi.png',"Integration.", r'practice_description\\integration_des.png', r'practice_katakana\\integration_kata.png'])
word[14] = (["Retribution",r'practice_sound\\retribution.mp3', r'practice_image\\retribution.png', r'practice_text\\retribution_text.png','practice_imi\\retribution_imi.png',"Retribution.", r'practice_description\\retribution_des.png', r'practice_katakana\\retribution_kata.png'])
word[15] = (["Affinity",r'practice_sound\\affinity.mp3', r'practice_image\\affinity.png', r'practice_text\\affinity_text.png' ,'practice_imi\\affinity_imi.png',"Affinity.",r'practice_description\\affinity_des.png', r'practice_katakana\\affinity_kata.png'])
word[16] = (["Preservation",r'practice_sound\\preservation.mp3', r'practice_image\\preservation.png', r'practice_text\\preservation_text.png' ,'practice_imi\\preservation_imi.png',"Preservation.",  r'practice_description\\preservation_des.png', r'practice_katakana\\preservation_kata.png'])
word[17] = (["Hindrance",r'practice_sound\\Hindrance.mp3', r'practice_image\\hindrance.png', r'practice_text\\hindrance_text.png' ,'practice_imi\\hindrance_imi.png',"Hindrance.", r'practice_description\\hindrance_des.png', r'practice_katakana\\hindrance_kata.png'])
word[18] = (["Breakthrough",r'practice_sound\\breakthrough.mp3', r'practice_image\\breakthrough.png', r'practice_text\\breakthrough_text.png' ,'practice_imi\\breakthrough_imi.png', "Breakthrough.", r'practice_description\\breakthrough_des.png', r'practice_katakana\\breakthrough_kata.png'])
word[19] = (["Adherent",r'practice_sound\\adherent.mp3', r'practice_image\\adherent.png', r'practice_text\\adherent_text.png' ,'practice_imi\\adherent_imi.png', "Adherent.", r'practice_description\\adherent_des.png', r'practice_katakana\\adherent_kata.png'])


#音声とイラストと意味とフォニックスとカタカナ (word[i][1], word[i][2], word[i][5], word[i][8], word[i][9])

word[20] = (["Dissertation",r'practice_sound\\dissertation.mp3', r'practice_image\\dissertation.png', r'practice_text\\dissertation_text.png','practice_imi\\dissertation_imi.png',"Dissertation.", r'practice_description\\dissertation_des.png' , r'practice_katakana\\dissertation_kata.png'])
word[21] = (["Dispute",r'practice_sound\\dispute.mp3', r'practice_image\\dispute.png', r'practice_text\\dispute_text.png', r'practice_imi\\dispute_imi.png',"Dispute.", r'practice_description\\dispute_des.png', r'practice_katakana\\dispute_kata.png'])
word[22] = (["Dissension",r'practice_sound\\dissension.mp3', r'practice_image\\dissension.png', r'practice_text\\dissension_text.png' ,'practice_imi\\dissension_imi.png',"Dissension.", r'practice_description\\dissension_des.png', r'practice_katakana\\dissension_kata.png'])
word[23] = (["Jeopardy",r'practice_sound\\jeopardy.mp3', r'practice_image\\jeopardy.png', r'practice_text\\jeopardy_text.png','practice_imi\\jeopardy_imi.png',"Jeopardy.", r'practice_description\\jeopardy_des.png', r'practice_katakana\\jeopardy_kata.png'])
word[24] = (["Provision",r'practice_sound\\provision.mp3', r'practice_image\\provision.png', r'practice_text\\provision_text.png','practice_imi\\provision_imi.png',"Provision.", r'practice_description\\provision_des.png', r'practice_katakana\\provision_kata.png'])
word[25] = (["Duration",r'practice_sound\\duration.mp3', r'practice_image\\duration.png', r'practice_text\\duration_text.png' ,'practice_imi\\duration_imi.png',"Duration.", r'practice_description\\duration_des.png', r'practice_katakana\\duration_kata.png'])
word[26] = (["Conglomerate",r'practice_sound\\conglomerate.mp3', r'practice_image\\conglomerate.png', r'practice_text\\conglomerate_text.png' ,'practice_imi\\conglomerate_imi.png',"Conglomerate.", r'practice_description\\conglomerate_des.png', r'practice_katakana\\conglomerate_kata.png'])
word[27] = (["Enforcement",r'practice_sound\\enforcement.mp3', r'practice_image\\enforcement.png', r'practice_text\\enforcement_text.png' ,'practice_imi\\enforcement_imi.png',"Enforcement.", r'practice_description\\enforcement_des.png', r'practice_katakana\\enforcement_kata.png'])
word[28] = (["Disguise",r'practice_sound\\disguise.mp3', r'practice_image\\disguise.png', r'practice_text\\disguise_text.png' ,'practice_imi\\disguise_imi.png', "Disguise.",  r'practice_description\\disguise_des.png', r'practice_katakana\\disguise_kata.png'])
word[29] = (["Transgression",r'practice_sound\\transgression.mp3', r'practice_image\\transgression.png', r'practice_text\\transgression_text.png', r'practice_imi\\transgression_imi.png',"Transgression.", r'practice_description\\transgression_des.png', r'practice_katakana\\transgression_kata.png'])

#音声とイラストと意味と説明文とカタカナ (word[i][1], word[i][2], word[i][5], word[i][7], word[i][8]) 

word[30] = (["Mimicry",r'practice_sound\\mimicry.mp3', r'practice_image\\mimicry.png', r'practice_text\\mimicry_text.png', r'practice_imi\\mimicry_imi.png',"Mimicry.",r'practice_description\\mimicry_des.png', r'practice_katakana\\mimicry_kata.png'])
word[31] = (["Annotation",r'practice_sound\\annotation.mp3', r'practice_image\\annotation.png', r'practice_text\\annotation_text.png' , r'practice_imi\\annotation_imi.png',"Annotation.", r'practice_description\\annotation_des.png', r'practice_katakana\\annotation_kata.png' ])
word[32] = (["Gravity",r'practice_sound\\gravity.mp3', r'practice_image\\gravity.png', r'practice_text\\gravity_text.png', r'practice_imi\\gravity_imi.png',"Gravity.", r'practice_description\\gravity_des.png', r'practice_katakana\\gravity_kata.png'])
word[33] = (["Privilege",r'practice_sound\\privilege.mp3', r'practice_image\\privilege.png', r'practice_text\\privilege_text.png' , r'practice_imi\\privilege_imi.png',"Privilege.", r'practice_description\\privilege_des.png', r'practice_katakana\\privilege_kata.png'])
word[34] = (["Creed",r'practice_sound\\creed.mp3', r'practice_image\\creed.png', r'practice_text\\creed_text.png' , r'practice_imi\\creed_imi.png',"Creed.",  r'practice_description\\creed_des.png', r'practice_katakana\\creed_kata.png'])
word[35] = (["Backlog",r'practice_sound\\backlog.mp3', r'practice_image\\backlog.png', r'practice_text\\backlog_text.png' , r'practice_imi\\backlog_imi.png',"Backlog.", r'practice_description\\backlog_des.png', r'practice_katakana\\backlog_kata.png'])
word[36] = (["Remedy",r'practice_sound\\remedy.mp3', r'practice_image\\remedy.png', r'practice_text\\remedy_text.png' , r'practice_imi\\remedy_imi.png', "Remedy.", r'practice_description\\remedy_des.png', r'practice_katakana\\remedy_kata.png'])
word[37] = (["Misgiving",r'practice_sound\\misgiving.mp3', r'practice_image\\misgiving.png', r'practice_text\\misgiving_text.png' , r'practice_imi\\misgiving_imi.png', "Misgiving.", r'practice_description\\misgiving_des.png', r'practice_katakana\\misgiving_kata.png'])
word[38] = (["Momentum",r'practice_sound\\momentum.mp3', r'practice_image\\momentum.png', r'practice_text\\momentum_text.png', r'practice_imi\\momentum_imi.png',"Momentum.", r'practice_description\\momentum_des.png', r'practice_katakana\\momentum_kata.png'])
word[39] = (["Pageant",r'practice_sound\\pageant.mp3', r'practice_image\\pageant.png', r'practice_text\\pageant_text.png', r'practice_imi\\pageant_imi.png',"Pageant.", r'practice_description\\pageant_des.png', r'practice_katakana\\pageant_kata.png'])


#音声と意味と説明文とカタカナ(word[i][1], word[i][5]
word[40] = (["Aptitude",r'practice_sound\\aptitude.mp3', r'practice_image\\aptitude.png', r'practice_text\\aptitude_text.png', r'practice_imi\\aptitude_imi.png',"Aptitude.", r'practice_description\\aptitude_des.png', r'practice_katakana\\aptitude_kata.png'])
word[41] = (["Premium",r'practice_sound\\premium.mp3', r'practice_image\\premium.png', r'practice_text\\premium_text.png', r'practice_imi\\premium_imi.png',"Premium.", r'practice_description\\premium_des.png', r'practice_katakana\\premium_kata.png'])
word[42] = (["Elimination",r'practice_sound\\elimination.mp3', r'practice_image\\elimination.png', r'practice_text\\elimination_text.png' , r'practice_imi\\elimination_imi.png',"Elimination.", r'practice_description\\elimination_des.png', r'practice_katakana\\elimination_kata.png'])
word[43] = (["Platitude",r'practice_sound\\platitude.mp3', r'practice_image\\platitude.png', r'practice_text\\platitude_text.png' , r'practice_imi\\platitude_imi.png', "Platitude.", r'practice_description\\platitude_des.png', r'practice_katakana\\platitude_kata.png'])
word[44] = (["Longevity",r'practice_sound\\longevity.mp3', r'practice_image\\longevity.png', r'practice_text\\longevity_text.png' , r'practice_imi\\longevity_imi.png', "Longevity.", r'practice_description\\longevity_des.png', r'practice_katakana\\longevity_kata.png'])
word[45] = (["Perception",r'practice_sound\\perception.mp3', r'practice_image\\perception.png', r'practice_text\\perception_text.png' , r'practice_imi\\perception_imi.png',"Perception.", r'practice_description\\perception_des.png', r'practice_katakana\\perception_kata.png'])
word[46] = (["Repeal",r'practice_sound\\repeal.mp3', r'practice_image\\repeal.png', r'practice_text\\repeal_text.png', r'practice_imi\\repeal_imi.png',"Repeal.", r'practice_description\\repeal_des.png', r'practice_katakana\\repeal_kata.png'])
word[47] = (["Proponent",r'practice_sound\\proponent.mp3', r'practice_image\\proponent.png', r'practice_text\\proponent_text.png', r'practice_imi\\proponent_imi.png',"Proponent.", r'practice_description\\proponent_des.png', r'practice_katakana\\proponent_kata.png'])
word[48] = (["Abundance",r'practice_sound\\abundance.mp3', r'practice_image\\abundance.png', r'practice_text\\abundance_text.png' , r'practice_imi\\abundance_imi.png',"Abundance.", r'practice_description\\abundance_des.png', r'practice_katakana\\abundance_kata.png'])
word[49] = (["Deportation",r'practice_sound\\deportation.mp3', r'practice_image\\deportation.png', r'practice_text\\deportation_text.png' , r'practice_imi\\deportation_imi.png',"Deportation.", r'practice_description\\deportation_des.png', r'practice_katakana\\deportation_kata.png'])




word[50] = (["Commotion",r'practice_sound\\commotion.mp3', r'practice_image\\commotion.png', r'practice_text\\commotion_text.png' , r'practice_imi\\commotion_imi.png',"Commotion.", r'practice_description\\commotion_des.png', r'practice_katakana\\commotion_kata.png'])
word[51] = (["Proximity",r'practice_sound\\proximity.mp3', r'practice_image\\proximity.png', r'practice_text\\proximity_text.png' , r'practice_imi\\proximity_imi.png', "Proximity.", r'practice_description\\proximity_des.png', r'practice_katakana\\proximity_kata.png'])
word[52] = (["Jinx",r'practice_sound\\jinx.mp3', r'practice_image\\jinx.png', r'practice_text\\jinx_text.png', r'practice_imi\\jinx_imi.png',"Jinx.", r'practice_description\\jinx_des.png', r'practice_katakana\\jinx_kata.png'])
word[53] = (["Ultimatum",r'practice_sound\\ultimatum.mp3', r'practice_image\\ultimatum.png', r'practice_text\\ultimatum_text.png', r'practice_imi\\ultimatum_imi.png',"Ultimatum.",  r'practice_description\\ultimatum_des.png', r'practice_katakana\\ultimatum_kata.png'])
word[54] = (["Extinction",r'practice_sound\\extinction.mp3', r'practice_image\\extinction.png', r'practice_text\\extinction_text.png' , r'practice_imi\\extinction_imi.png',"Extinction.", r'practice_description\\extinction_des.png', r'practice_katakana\\extinction_kata.png'])
word[55] = (["Fidelity",r'practice_sound\\fidelity.mp3', r'practice_image\\fidelity.png', r'practice_text\\fidelity_text.png' , r'practice_imi\\fidelity_imi.png',"Fidelity.",r'practice_description\\fidelity_des.png', r'practice_katakana\\fidelity_kata.png'])
word[56] = (["Diversity",r'practice_sound\\diversity.mp3', r'practice_image\\diversity.png', r'practice_text\\diversity_text.png' , r'practice_imi\\diversity_imi.png',"Diversity.", r'practice_description\\diversity_des.png', r'practice_katakana\\diversity_kata.png'])
word[57] = (["Pretext",r'practice_sound\\pretext.mp3', r'practice_image\\pretext.png', r'practice_text\\pretext_text.png' , r'practice_imi\\pretext_imi.png',"Pretext.", r'practice_description\\pretext_des.png', r'practice_katakana\\pretext_kata.png'])
word[58] = (["Agility",r'practice_sound\\agility.mp3', r'practice_image\\agility.png', r'practice_text\\agility_text.png' , r'practice_imi\\agility_imi.png', "Agility.", r'practice_description\\agility_des.png', r'practice_katakana\\agility_kata.png'])
word[59] = (["Misnomer",r'practice_sound\\misnomer.mp3', r'practice_image\\misnomer.png', r'practice_text\\misnomer_text.png' , r'practice_imi\\misnomer_imi.png', "Misnomer.",r'practice_description\\misnomer_des.png', r'practice_katakana\\misnomer_kata.png'])






#スクリーンサイズ取得
sc_w = GetSystemMetrics(0)
sc_h = GetSystemMetrics(1)

#words = np.array(word)


#ran = random.randint(0,word_num)

def disp_img(img,banana):

	print(img[0]) 

	if banana == 1:	# disp_image_kata_dscr 
		#イラスト画像の表示 
		#LinerImg = cv2.resize(cv2.imread(img[2]),(700, 700))
		LinerImg = cv2.imread(img[2])
		cv2.imshow('LinerImg', LinerImg)
		cv2.moveWindow('LinerImg', 0, 0)
		
		#意味画像の表示       
		#LinerImg2 = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg2 = cv2.imread(img[4])    
		cv2.imshow('LinerImg2',LinerImg2)     
		cv2.moveWindow('LinerImg2',0,480)
		
		LinerImg3 = cv2.imread(img[6])    
		cv2.imshow('LinerImg3',LinerImg3)     
		cv2.moveWindow('LinerImg3',0,680)
		
		LinerImg4 = cv2.imread(img[7])    
		cv2.imshow('LinerImg4',LinerImg4)     
		cv2.moveWindow('LinerImg4',0,880)
		
	elif banana == 2:	#disp_image_kata(img):
		#イラスト画像の表示 
		#LinerImg = cv2.resize(cv2.imread(img[2]),(700, 700))
		LinerImg5 = cv2.imread(img[2])
		cv2.imshow('LinerImg5', LinerImg5)
		cv2.moveWindow('LinerImg5', 0, 0)

		#意味画像の表示       
		#LinerImg2 = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg6 = cv2.imread(img[4])    
		cv2.imshow('LinerImg6',LinerImg6)     
		cv2.moveWindow('LinerImg6',0,480)
		
		
		LinerImg7 = cv2.imread(img[7])    
		cv2.imshow('LinerImg7',LinerImg7)     
		cv2.moveWindow('LinerImg7',0,680)
		
	elif banana == 3:	# disp_image_dcsr(img):
		#イラスト画像の表示 
		#LinerImg = cv2.resize(cv2.imread(img[2]),(700, 700))
		LinerImg8 = cv2.imread(img[2])
		cv2.imshow('LinerImg8', LinerImg8)
		cv2.moveWindow('LinerImg8', 0, 0)

		#意味画像の表示       
		#LinerImg2 = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg9 = cv2.imread(img[4])    
		cv2.imshow('LinerImg9',LinerImg9)     
		cv2.moveWindow('LinerImg9',0,480)
		
		LinerImg10 = cv2.imread(img[6])    
		cv2.imshow('LinerImg10',LinerImg10)     
		cv2.moveWindow('LinerImg10',0,680)

	elif banana == 4:	#disp_kata_dcsr(img):
		#意味画像の表示       
		#LinerImg2 = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg11 = cv2.imread(img[4])    
		cv2.imshow('LinerImg11',LinerImg11)     
		cv2.moveWindow('LinerImg11',0,0)
		
		
		LinerImg12 = cv2.imread(img[6])    
		cv2.imshow('LinerImg12',LinerImg12)     
		cv2.moveWindow('LinerImg12',0,200)
		
		LinerImg13 = cv2.imread(img[7])    
		cv2.imshow('LinerImg13',LinerImg13)     
		cv2.moveWindow('LinerImg13',0,400)
		
	elif banana == 5:	#disp_kata(img):
		#意味画像の表示       
		#LinerImg13 = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg14 = cv2.imread(img[4])    
		cv2.imshow('LinerImg14',LinerImg14)     
		cv2.moveWindow('LinerImg14',0,0)

		
		LinerImg15 = cv2.imread(img[7])    
		cv2.imshow('LinerImg15',LinerImg15)     
		cv2.moveWindow('LinerImg15',0,200)

	elif banana == 6:	#disp_dcsr(img):
	
		#意味画像の表示       
		#LinerImg = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg16 = cv2.imread(img[4])    
		cv2.imshow('LinerImg16',LinerImg16)     
		cv2.moveWindow('LinerImg16',0,0)

		LinerImg17 = cv2.imread(img[6])    
		cv2.imshow('LinerImg17',LinerImg17)     
		cv2.moveWindow('LinerImg17',0,200)


	elif banana == 7:
		#イラスト画像の表示 
		#LinerImg = cv2.resize(cvw2.imread(img[2]),(700, 700))
		LinerImg18 = cv2.imread(img[2])
		cv2.imshow('LinerImg18', LinerImg18)
		cv2.moveWindow('LinerImg18', 0, 0)

		#LinerImg2 = cv2.resize(cv2.imread(img[4]), (512, 200))
		LinerImg19 = cv2.imread(img[4])    
		cv2.imshow('LinerImg19',LinerImg19)     
		cv2.moveWindow('LinerImg19',0,480)
	
	
	elif banana == 8:
		print("紙媒体学習")


	
		
	if banana == 9:
		TextImg = cv2.imread(img[3])
		cv2.imshow('TextImg', TextImg)
		cv2.moveWindow('TextImg', 0, 0)
		cv2.waitKey(0)
		
				
	if banana < 9:
		pygame.mixer.init()
		pygame.mixer.music.load(img[1])
		mp3_length = mp3(img[1]).info.length
		pygame.mixer.music.play(1) 
		time.sleep(mp3_length + 0.25)  
		pygame.mixer.music.stop()
		cv2.waitKey(0)
	
	

	#word[] = [単語0、音声1、イラスト2、テキスト画像3、意味4、認識単語5、説明6、カタカナ7]
	
	
#文字認識を行うコード

def word_ocr():
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("No OCR tool found")
		sys.exit(1)
	tool = tools[0]
	last_txt = ""
	langs = tool.get_available_languages()
	lang = langs[0]
	capture = cv2.VideoCapture(0)
	last_txt = ""
	while True:
		ret, frame = capture.read()
		
		orgHeight, orgWidth = frame.shape[:2]
		size = (500, 500)
		glay = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		image = cv2.resize(glay, size)
		
		cv2.moveWindow('Capture',-1920,480)
		edframe = frame
		t = time.time()

		#画像の中にある文字を"txt"の中に代入
		txt = tool.image_to_string(
			Image.fromarray(image),
			lang="eng",
			builder=pyocr.builders.TextBuilder(tesseract_layout=6)
		) 
		for i in range(word_num):
			if(txt == word[i][0]):
				return i
		cv2.imshow("Capture", image)
		if cv2.waitKey(33) >= 0:
			break



#音声認識コード

def sound_in():
	speech_key, service_region = "ここにサブスクリプションキー入力", "ここにエンドポイント入力"
	speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
	speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
	print("Say something...")
	result = speech_recognizer.recognize_once()

	if result.reason == speechsdk.ResultReason.RecognizedSpeech:
	    print("Recognized: {}".format(result.text))	    
	    
	elif result.reason == speechsdk.ResultReason.NoMatch:
	    print("No speech could be recognized: {}".format(result.no_match_details))
	    
	elif result.reason == speechsdk.ResultReason.Canceled:
	    cancellation_details = result.cancellation_details
	    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
	    
	    if cancellation_details.reason == speechsdk.CancellationReason.Error:
	        print("Error details: {}".format(cancellation_details.error_details))
	        
	#"te1"という変数に音声認識したテキストを格納
	return result.text





def jud_text(tex,numbe,new_numbe):

	if(tex == word[numbe][5]):   
		score[numbe] += 1
		print('あなたは{}回目に正解しました。'.format(score[numbe]))
		new_score[new_numbe] = score[numbe]
		return 0
	elif(tex != word[numbe][5]):
		score[numbe] += 1
		print("ちゃんと発音してね")
		while True:
			if msvcrt.kbhit():
				kb = msvcrt.getch()
				if kb.decode() == 'a':
					pygame.mixer.init()
					pygame.mixer.music.load(word[numbe][1])
					mp3_length = mp3(word[numbe][1]).info.length 
					pygame.mixer.music.play(1) 
					time.sleep(mp3_length + 0.25) 
					pygame.mixer.music.stop()
				elif kb.decode() == 'b':
					return 1
				elif kb.decode() == 'c':
					score[numbe] = 0
					new_score[new_numbe] = score[numbe]
					return 0



def fin_scr(thescore):

	for i in range(10):
		
		if(thescore[i] == 0):
			print(new_word[i][0]+'は音声認識できませんでした')
			
		else:
			print(new_word[i][0]+'は{}回目に音声認識できました'.format(thescore[i]))
			
	thescore[i] = 0

def jud_test_text(tex,numbe):
	if(tex == new_word[numbe][5]):   
		test_score[numbe] += 1
		print('あなたは{}回目に正解しました。'.format(test_score[numbe]))
		return 0
	elif(tex != new_word[numbe][5]):
		test_score[numbe] += 1
		print("ちゃんと発音してね")
		while True:
			if msvcrt.kbhit():
				kb = msvcrt.getch()
				if kb.decode() == 'a':
					pygame.mixer.init()
					pygame.mixer.music.load(new_word[numbe][1])
					mp3_length = mp3(new_word[numbe][1]).info.length 
					pygame.mixer.music.play(1) 
					time.sleep(mp3_length + 0.25) 
					pygame.mixer.music.stop()
				elif kb.decode() == 'b':
					return 1
				elif kb.decode() == 'c':
					test_score[numbe] = 0
					return 0


def main():
	l = [1,2,3,4,5,6,7,8]

	m = [1,2,3,4,5,6,7,8,9,10]
	#m = [1,2,3]

	nnumber = 0
	#rand_sort()
	x = random.sample(l,8)
	y = random.sample(m,10)

	#y = random.sample(m,3)
	print(x)
	print(y)
	#print(new_score)

	for k in range(0,8):	
		
		for i in range(0,10):
			print("練習問題{}問目".format(i+1))
			#ran = random.randint(0,word_num+1)
			#cv2.imshow('text',cv2.imread(new_word[i][3]))	
			number = word_ocr()
			print(number)
			#disp_img(word[number],x[k])
			disp_img(word[number],8)
			new_word[i] = word[number]
			nw = new_word[i]
			nw.append(word[number])
			jud_fin = 1
			while jud_fin == 1:
				sd_text = sound_in()
				jud_fin = jud_text(sd_text,number,nnumber)
			cv2.destroyAllWindows()
			nnumber += 1
		nnumber = 0
		print(new_score)
		print(new_score)
		#print(test_score)
		#print(new_word)
		fin_scr(new_score)
		
		start = input('Enterを押すとテストが開始します')
		
		for j in range(0, 10):
			
			print("テスト問題{}問目".format(j+1))
			number = y[j]
			disp_img(new_word[number-1],9)
			jud_fin = 1
			while jud_fin == 1:
				sd_text = sound_in()
				jud_fin = jud_test_text(sd_text,number-1)
			cv2.destroyAllWindows()
		fin_scr(test_score)
		
		wait = input('実験者の合図があったらEnterボタンを押してください')
		
		new_score.clear()
		new_word.clear()
		test_score.clear()
		print(new_score)

		#test_score = [0]*10
		
		print(test_score)
	print("終了です。お疲れさまでした。")
if __name__ == "__main__":
		main()

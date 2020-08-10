from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
DOWNLOAD_PATH = "D:/VSUSP"

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_dictionary":DOWNLOAD_PATH})
driver = webdriver.Chrome(executable_path=PATH,options=chromeOptions)
driver.get("https://vsusp.com")
driver.fullscreen_window()
class elemen:
	def __init__(self,id):
		try:
			self.elem = driver.find_element_by_id(id)
		except Exception as e:
			self.elem = driver.find_element_by_link_text(id)

	def sel(self,opt):
		
		self.elem = Select(self.elem)
		self.elem.select_by_visible_text(opt)
	
	def click(self):
		self.elem.click()

	def change(self,val):

		self.elem.send_keys(Keys.CONTROL + "a")
		self.elem.send_keys(Keys.DELETE)
		self.elem.send_keys(val)
		self.elem.send_keys(Keys.RETURN)

	def printelem(self):
		print(self.elem)

driver.implicitly_wait(2)

elemen('fby').change('17')
fclx=elemen('fclx')
fclx.change('8')
elemen('fbly').change('0')
fcux=elemen('fcux')
fcux.change('8.5')
elemen('fbuy').change('4.7')

elemen('control_arms_tab_li').click()
caul=elemen('caul')
caul.change('16')
call=elemen('call')
call.change('18')

elemen('knuckles_tab_li').click()
elemen('khux').change('3.15')
elemen('khuy').change('5')
elemen('khlx').change('1.024')
elemen('khly').change('1.142')

elemen('steering_tab_li').click()
elemen('sthotr_x').change('-1')
elemen('sthotr_y').change('0')

elemen('wheels_tab_li').click()
elemen('wo').change('-1.436')
elemen('tsc').sel('Explicit (diameter/width)')
elemen('tde').change('22')
elemen('twe').change('7')
elemen('wde').change('10')
elemen('tscmp').change('0')

elemen('Chart').click()
elemen('chxaf').sel('Left bump')
elemen('chxac').change('0')
elemen('chxaw').change('250')
elemen('chxns').change('21')

cl = driver.find_element_by_xpath("//option[contains(text() , 'Left camber')]")
cl.click()
clr = driver.find_element_by_xpath("//option[contains(text() , 'Roll center Y location')]")
clr.click()



# for i in range(0,40):
# 	elemen('control_arms_tab_li').click()
# 	caul.change(str(16+(i*5/100)))
# 	elemen('frame_tab_li').click()
# 	fcux.change(str(7.5-(i*5/100)))
# 	file_folder = 'CAUL(' + str(16+(i*5/100)) + ') & FCUX(' + str(7.5-(i*5/100)) +')'
# 	folder_path = os.path.join(DOWNLOAD_PATH,file_folder)
	
# 	for j in range(0,40):		
# 		elemen('control_arms_tab_li').click()
# 		call.change(str(18+(j*5/100)))
# 		elemen('frame_tab_li').click()
# 		fclx.change(str(8-(j*5/100)))
# 		file_path = 'CALL(' + str(18+(j*5/100)) + ') & FCLX(' + str(8-(j*5/100)) + ')'
# 		tw = driver.find_element_by_id('gr_tw').text
# 		fvsa = driver.find_element_by_id('gr_rfvsa').text
# 		if float(tw)<=51 and float(fvsa)>0:
# 			try:
# 				os.mkdir(folder_path)
# 			except:
# 				pass
# 			finally:
# 				try:
# 					os.mkdir(os.path.join(folder_path,file_path))
# 				except:
# 					pass
# 				finally:
# 					location=os.path.join(DOWNLOAD_PATH,file_folder,file_path)
# 					driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
# 					driver.save_screenshot(location+'/top.png')
# 					driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
# 					driver.save_screenshot(location+'/bottom.png')
# driver.quit()

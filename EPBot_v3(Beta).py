from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
import time
#Education Perfect Bot V3 (Beta)
loop = 1
data_answers = []
data_questions = []
#Defines the the data collection function
def ep_data(q,a,i):
    data_question = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/ui-view/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[{i}]/div[1]/div[2]').text
    data_answer = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/ui-view/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[{i}]/div[1]/div[1]').text
    q.append(data_question)
    a.append(data_answer)
#Function to Generate answer based on question    
def ep_task(q,a):
    task_question = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ui-view/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/span[2]').text
    try:
        task_answer_index = q.index(task_question)
        task_answer = (a[task_answer_index])
    except:
        task_answer_index = a.index(task_question)
        task_answer = (q[task_answer_index])
    return (task_answer)
#Funtion to save Credentials
def save_creds(username,password):
    file = open('log.txt', 'w')
    file.write(f'{username} {password}')
#Function to load Credentials
def load_creds():
    file = open ('log.txt','r')
    creds = (file.read().split(' '))
    return creds

print ('Education Perfect Bot (V3)')
link = input('Link to task: ')
amount = int(input('Question Amount (1)5, (2)10, (3)20, (4)50, (5)Infinity: '))
creds = load_creds()
try:
    print ('Password:',creds[1])
    print ('Username:',creds[0])
    load = input('Would you like to load credentials(Y/N): ')
except:
    print ('No credentials found')
    load = ('N')

if load == 'N':
    username = input('Username: ')
    password = input('Password: ')
    save = input('Would you like to save credentials(Y/N): ')
    if save == 'Y':
        save_creds(username,password)
if load == 'Y':
    username = (creds[0])
    password = (creds[1])
   
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
driver.get(link)
time.sleep(1.5)
pyautogui.write(username)
pyautogui.press('tab')
pyautogui.write(password)
pyautogui.press('enter')
time.sleep(1.5)
driver.find_element_by_xpath(f'//*[@id="number-of-questions-selector"]/li[{amount}]').click()
#Collects data
while True:
    try:
        ep_data(data_questions, data_answers, loop)
        loop += 1
    except:
        break
#Enters Task
driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)
time.sleep(0.5)
#Inputs Answers
while True:
    try:
        element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ui-view/div[1]/div[2]/div/div/div[2]/div[2]/game-lp-answer-input/div/div[2]/input');
        element.send_keys(ep_task(data_questions, data_answers))
        time.sleep(0.08)
        element.send_keys(Keys.ENTER)
    except:
        print('Task Complete')
        break
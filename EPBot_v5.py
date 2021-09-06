from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
import time
#Education Perfect Bot V5
#data refers to the data gathered from the questions and answers 
#Task refers to the actual questions and answers when the task stars

question_and_answer_number = 1
q = 1
data_answers = [] #Answers from the list task
data_questions = [] #Questions from the list task

#Defines the the data collection function
def ep_data(question,answer,i):
    data_question = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/ui-view/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[{i}]/div[1]/div[2]').text
    data_answer = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/ui-view/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[{i}]/div[1]/div[1]').text
    question.append(data_question)
    answer.append(data_answer)

#Function to Generate answer based on question    
def ep_task(question,answer):
    task_question = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ui-view/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/span[2]').text
    try:
        task_answer_index = question.index(task_question)
        task_answer = (answer[task_answer_index])
    except:
        task_answer_index = answer.index(task_question)
        task_answer = (question[task_answer_index])
    return (task_answer)

#Way to save your EP login to speed up run time

#Function to save Credentials and file directory
def save_creds(username,password,directory):
    file = open('log.txt', 'w')
    file.write(f'{username}%break%{password}%break%{directory}')

#Function to load Credentials
def load_creds():
    file = open ('log.txt','r')
    creds = (file.read().split('%break%'))
    return creds


#Where the actual program starts
print ('Education Perfect Bot (V5)')
link = input('Link to task: ')
amount = int(input('Question Amount (1)5, (2)10, (3)20, (4)50, (5)Infinity: '))
speed = float(input('Enter time between question in seconds (anything lower than 0.1 might break your code): '))

#Code to load credentials/prefernes
creds = load_creds()
try:
    print ('Password:',creds[1])
    print ('Username:',creds[0])
    print ('Driver Directory:',creds[2])
    load = input('Would you like to load credentials(Y/N): ')
except:
    print ('No credentials found')
    load = ('N')

if load == 'N' or load == 'n':
    username = input('Username: ')
    password = input('Password: ')
    directory = input('Driver Directory: ')
    save = input('Would you like to save preferences(Y/N): ')
    if save == 'Y':
        save_creds(username,password,directory)
if load == 'Y' or load == 'y':
    username = (creds[0])
    password = (creds[1])
    directory = (creds[2])
   
#Opens webpage
driver = webdriver.Firefox(executable_path=directory+'\geckodriver.exe')
driver.get(link)

#Login Process
while True:
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[1]/input').send_keys(username)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/form/button').click()
        break
    except:
        breakpoint

#Selects the amount of questions
while True:
    try:
        driver.find_element_by_xpath(f'//*[@id="number-of-questions-selector"]/li[{amount}]').click()
        break
    except:
        breakpoint
#Collects data
while True:
    try:
        ep_data(data_questions, data_answers, question_and_answer_number)
        question_and_answer_number += 1
    except:
        break

driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)
time.sleep(1)

#Inputs answers
while True:
    try:
        element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ui-view/div[1]/div[2]/div/div/div[2]/div[2]/game-lp-answer-input/div/div[2]/input');
        element.send_keys(ep_task(data_questions, data_answers))
        time.sleep(speed)
        element.send_keys(Keys.ENTER)
    except:
        print('Task Complete')
        break
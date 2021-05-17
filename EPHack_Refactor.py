from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
import time
#refactor
data_answers = []
data_questions = []
i = 1

#Inputs for the task
link = input('Link to task: ')
username = input('Enter Username: ')
password = input('Enter Password: ')
question_amount = int(input('Question Amount (1)5, (2)10, (3)20, (4)50, (5)Infinity: '))

#Path to chrome for selenium
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

#Logs into Education Perfect
driver.get(link)
time.sleep(3)
pyautogui.write('TUBM01@stpiusx.nsw.edu.au')#change to variable username
pyautogui.press('tab')
pyautogui.write('!Hnbty$56')#change to variable password
pyautogui.press('enter')
time.sleep(2)
#selects number of questions
driver.find_element_by_xpath(f'//*[@id="number-of-questions-selector"]/li[{question_amount}]').click()

#finds questions and answers
while True:
    try:
        data_question = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/ui-view/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[{i}]/div[1]/div[2]').text
        data_answer = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/ui-view/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[{i}]/div[1]/div[1]').text
        data_answers.append(data_answer)
        data_questions.append(data_question)
        i += 1
    except:
        break

print (data_answers)
print (data_questions)

driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)

time.sleep(2)

while True:
    task_question = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ui-view/div[1]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/span[2]').text
    try:
        task_answer_index = data_questions.index(task_question)
        task_answer = (data_answers[task_answer_index])
    except:
        task_answer_index = data_answers.index(task_question)
        task_answer = (data_questions[task_answer_index])

    print (task_answer)
    pyautogui.write(task_answer)
    pyautogui.press('enter')
    
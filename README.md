# education perfect bot

## automatically answers education perfect list tasks
### based off the education perfect bot by [KEN-2000l](https://github.com/KEN-2000l/EducationPerfected)

### [youtube tutorial](https://youtube.com/c/keypos)
*work in progress at the moment*

## documentation

the program is written in javascript and runs using node.js  
the [puppeteer](https://github.com/puppeteer/puppeteer) node library is used to control chromium and make actions in the browser

## installation guide

-   install node.js from https://nodejs.org/en/
-   install the Puppeteer library by opening terminal and running `npm i puppeteer`
-   download the `index.js` script (edit the username and password fields to auto login)
-   run the `index.js` script using Node.js with the command `npm start`

## expected behavior

when you run the script, it should open a new browser window running chromium
education perfect website will load as normal  
navigate through ep as normal as the epbot is loaded in the background  
trigger the functions using hotkeys provided below  
*close the programing by exiting the chromium window or using `ctrl + c` in the terminal*

## hotkeys

all functions are triggered via the hotkeys listed below

-   **refresh word list : `alt + r`**  
     scrapes the questions and answers to all questions  
     run before entering each task  
     make sure to refresh the word list before each new task

-   **auto answer : `alt + s`**  
    to be used while inside the task (after clicking start)  
    finds the answer for each question and automatically enters and submits it  
    *you can also pause the auto answer midway by pressing the hotkey again.*

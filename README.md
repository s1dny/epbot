

<h1 align="center">
  <img href="https://youtu.be/P-I77T8SokE"><img src="/src/epboticon.png" alt="ep bot logo" width="250"></img>
  </br>
  education perfect bot
</h1>
<h4 align="center">simple puppeteer script to automatically answer education perfect list tasks</h4>
<p align="center">
  <img src="https://img.shields.io/github/last-commit/keyp0s/epbot?logo=GitHub">
  <img src="https://img.shields.io/npm/v/puppeteer?label=puppeteer">
  <img src="https://img.shields.io/github/downloads/keyp0s/epbot/total?color=0logo=GitHub">
     
     
</p>

<p align="center">
  <a href="#getting-started">getting started</a> •
  <a href="#documentation">documentation</a> •
  <a href="#installation-guide">installation guide</a> •
  <a href="#expected-behavior">expected behavior</a> •
  <a href="#hotkeys">hotkeys</a>
</p>

## getting started
for a quick install guide checkout the [youtube tutorial](https://youtu.be/P-I77T8SokE)

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

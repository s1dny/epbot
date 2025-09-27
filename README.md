<h1 align="center">
  <img href="https://youtu.be/P-I77T8SokE"><img src="/src/epboticon.png" alt="ep bot logo" width="250"></img>
  </br>
  Education Perfect Bot
</h1>
<h4 align="center">Simple Puppeteer script to automatically answer education perfect list tasks</h4>
<p align="center">
  <img src="https://img.shields.io/github/last-commit/s1dny/epbot?logo=GitHub">
  <img src="https://img.shields.io/github/downloads/s1dny/epbot/total?color=0logo=GitHub">
</p>

## Getting started
For a quick install guide checkout the [YouTube tutorial](https://www.youtube.com/watch?v=P-I77T8SokE)

## Documentation

 - The program is written in JavaScript and runs using node.js
 - The [Puppeteer](https://github.com/puppeteer/puppeteer) node.js library is used to control chromium and make actions in the browser

## Installation guide

 - Install node.js from https://nodejs.org/en/
 - Install the Puppeteer library by opening terminal and running `npm i puppeteer`
 - Download the `index.js` script (edit the username and password fields to auto login)
 - Run the `index.js` script using Node.js with the command `npm start`

## Expected behavior

 - When you run the script, it should open a new browser window running chromium
 - Education perfect website will load as normal
 - Navigate through ep as normal as the epbot is loaded in the background
 - Trigger the functions using hotkeys provided below
 - *Close the programming by exiting the chromium window or using `ctrl + c` in the terminal*

## Hotkeys

All functions are triggered via the hotkeys listed below

 - **Refresh word list : `alt + r`**
   - Scrapes the questions and answers to all questions
   - Run before entering each task
   - Make sure to refresh the word list before each new task

 - **Auto answer : `alt + s`**  
   - To be used while inside the task (after clicking start)
   - Finds the answer for each question and automatically enters and submits it
   - *You can also pause the auto answer midway by pressing the hotkey again*

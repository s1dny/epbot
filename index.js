const puppeteer = require('puppeteer')
const dotenv = require('dotenv')

dotenv.config()

const ELEMENTS = {
    // login page elements
    usernameClass: '#login-username',
    passwordClass: '#login-password',
    loginButtonClass: '#login-submit-button',

    // task starter page elements
    baseListId: 'div.baseLanguage',
    targetListId: 'div.targetLanguage',
    startButtonClass: 'button#start-button-main',

    questionClass: '#question-text',
    answerBoxClass: 'input#answer-text',
}

const script = async () => {
    loginUrl = 'https://app.educationperfect.com/app/login'

    // specify chrome version
    const browserFetcher = puppeteer.createBrowserFetcher()
    const revisionInfo = await browserFetcher.download('991974')

    // launch browser
    puppeteer
        .launch({
            executablePath: revisionInfo.executablePath,
            headless: false,
            defaultViewport: null,
            handleSIGINT: false,
        })
        .then(async (browser) => {
            const page = (await browser.pages())[0]

            // open ep page and log in
            await page.goto(loginUrl)
            await page.waitForSelector(ELEMENTS.usernameClass)

            // fill in fields to login automaticly
            await page.type(ELEMENTS.usernameClass, process.env.EP_USERNAME)
            await page.type(ELEMENTS.passwordClass, process.env.EP_PASSWORD)
            await page.click(ELEMENTS.loginButtonClass)

            // auto-answer code starts here
            let TOGGLE = false
            let fullDict = {}
            let cutDict = {}

            function cleanString(string) {
                return String(string)
                    .replace(/\([^)]*\)/g, '')
                    .trim()
                    .split(';')[0]
                    .trim()
                    .split(',')[0]
                    .trim()
                    .split('|')[0]
                    .trim()
            }

            async function wordList(selector) {
                return await page.$$eval(selector, (els) => {
                    let words = []
                    els.forEach((i) => words.push(i.textContent))
                    return words
                })
            }

            async function refreshWordList() {
                const l1 = await wordList(ELEMENTS.baseListId)
                const l2 = await wordList(ELEMENTS.targetListId)
                for (let i = 0; i < l1.length; i++) {
                    fullDict[l2[i]] = cleanString(l1[i])
                    fullDict[l1[i]] = cleanString(l2[i])
                    cutDict[cleanString(l2[i])] = cleanString(l1[i])
                    cutDict[cleanString(l1[i])] = cleanString(l2[i])
                }
                console.log('word lists refreshed')
            }

            // finds matching answer
            function findAnswer(question) {
                let answer = fullDict[question]
                if (answer) return answer
                answer = fullDict[question.replace(',', ';')]
                if (answer) return answer
                answer = cutDict[cleanString(question)]
                if (answer) return answer
                console.log(`No answer found for ${question}`)
                return undefined
            }

            // main auto answer function
            async function answerLoop() {
                TOGGLE = true
                console.log('auto answer entered')

                while (TOGGLE) {
                    let question = await page.$eval(
                        ELEMENTS.questionClass,
                        (el) => el.textContent
                    )
                    let answer = findAnswer(question)

                    await page.click(ELEMENTS.answerBoxClass, { clickCount: 3 })
                    page.keyboard.sendCharacter(answer)
                    page.keyboard.press('Enter')
                }
                console.log('auto answer exited')
            }

            // auto answer toggling
            function toggle() {
                if (TOGGLE) {
                    TOGGLE = false
                    console.log('stopping auto answer')
                } else {
                    console.log('starting auto answer')
                    answerLoop().catch((e) => {
                        console.error(e)
                        TOGGLE = false
                    })
                }
            }

            await page.exposeFunction('refresh', refreshWordList)
            await page.exposeFunction('start', toggle)

            await page.evaluate(() => {
                document.addEventListener('keyup', async (event) => {
                    let key = event.key.toLowerCase()
                    if (event.altKey && key === 'r') {
                        await window.refresh()
                    } else if (event.altKey && key === 's') {
                        window.start()
                    }
                })
            })
            console.log('epbot loaded')
        })
}
script()

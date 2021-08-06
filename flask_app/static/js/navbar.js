var toType = document.querySelectorAll('.to-type')

var opening = document.querySelector('.opening')
var openingImg
setTimeout(async function(){
    // openingImg = new Promise((resolve, reject) => {
    //     opening.classList.add('fade-out')
    //     resolve("done")
    // })
    // await openingImg
    setTimeout(() => {
        // opening.style.display = 'none'
        typewriter()
    },500)
},500)

async function typewriter(){
    for (const element of toType) {
        phrase = element.textContent
        element.textContent = ""
        element.style.display = "inline"
        let i = 0
        var newLetter = new Promise((resolve, reject) => {
            var timer = setInterval(function(){
                if (i === phrase.length + 5){
                    clearInterval(timer)
                    element.style.display = 'none'
                    i=0
                    resolve("done")
                } else if (i < phrase.length) {
                    element.textContent += phrase[i]
                }
                i++
            }, 100)
        })
        await newLetter
    }
    typewriter()
}
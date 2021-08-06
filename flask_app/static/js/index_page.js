console.log(mainContent);
var mainATags = mainContent.querySelectorAll('.link')

async function index_page(){
    for (const tag of mainATags) {
        var promise = new Promise((resolve, reject) => {
            setTimeout(()=>{
                tag.style.position = 'relative'
                tag.classList.add('scroll-right')
                resolve('done')
            },100)
        })
        await promise
    }
    return
}
var wfLoads = document.querySelectorAll('.wf-load')
setTimeout(()=> {
    for (const wfLoad of wfLoads) {
        console.log(wfLoad);
        wfLoad.classList.remove('opacity-0')
        wfLoad.classList.add('fade-in')
    }
}, 1000)

var aTags = document.querySelectorAll('a')
var headerSkyBox = document.querySelector('.nav-head')
var mainContent = document.querySelector('.main-content')
var meta = document.querySelector('#page_info')

console.log(meta);

for (const tag of aTags) {
    tag.addEventListener('click', function(){
        console.log("click");
        var url = this.getAttribute('link')
        if (headerSkyBox){
            headerSkyBox.classList.add("scroll-up")
            document.querySelector('.contact-me-btn').textContent = 'Home'
            document.querySelector('.footer-mountain-1').classList.add('scroll-left')
            document.querySelector('.footer-mountain-2').classList.add('scroll-right')
            document.querySelector('.footer-mountain-3').classList.add('scroll-down')
            document.querySelector('.sky-img-lower').classList.add('fade-out')
        }
        if (meta.getAttribute('page_type') == 'index_page'){
            console.log("true");
            index_page()
        }
        mainContent.classList.add("fade-out")
        setTimeout(function(){
            window.location.href = url
        }, 750)
    })
}


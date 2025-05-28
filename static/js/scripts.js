
setTimeout(function () {
    var container = document.getElementById('messages-container')
    if (container) {
        container.style.transition = 'opacity 0.7s'
        container.style.opacity = '0'
        setTimeout(function () {
            container.style.display = 'none'
        }, 2000) //
    }
}, 2500)

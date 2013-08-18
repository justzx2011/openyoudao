var global = {
    fromVm:{
        searchDomain:'youdao.com'
    }
};
function rwt(a, newlink) {
    try {
        if (a === window) {
            a = window.event.srcElement;
            while (a) {
                if (a.href)
                    break;
                a = a.parentNode
            }
        }
        a.href = newlink;
        a.onmousedown = ""
    } catch (p) {
    }
    return true
}

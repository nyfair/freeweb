// ==UserScript==
// @name GeekBang Leech
// @namespace time.geekbang.org
// @match https://time.geekbang.org/course/detail/*
// @grant GM_setClipboard
// ==/UserScript==

var origOpen = XMLHttpRequest.prototype.open
XMLHttpRequest.prototype.open = function() {
  if (arguments[1].indexOf('m3u8') > -1) {
    m3u8 = arguments[1].replace('sd\/sd', 'hd/hd')
    window.setTimeout(function() {
      title = document.querySelector('h2').innerText.substring(6)
      GM_setClipboard('ffmpeg -i ' + m3u8 + ' -c copy "' + title + '.mp4"')
    }, 500)
  }
  origOpen.apply(this, arguments)
}

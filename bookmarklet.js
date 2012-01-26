javascript:(function(){
  var title = document.title;
  var url = location.href;
  open('http://127.0.0.1:8000/bookmarklet/add?title='+ encodeURIComponent(title) +'&url='+ encodeURIComponent(url),'yonda', 'width=512, height=384')
})();

javascript:(function(){var%20title=document.title;var%20url=location.href;open('http://127.0.0.1:8000/bookmarklet?title='+encodeURIComponent(title)+'&url='+encodeURIComponent(url),'yonda', 'width=512, height=384')})();

var nowurl=window.location.href;
if(nowurl.indexOf("www.mmonly.cc")>0){
	nowurl=nowurl.replace("www.mmonly.cc","m.mmonly.cc");
}else{
	nowurl=nowurl.replace("mmonly.cc","m.mmonly.cc");
}
if(/AppleWebKit.*Mobile/i.test(navigator.userAgent) || (/MIDP|SymbianOS|NOKIA|SAMSUNG|LG|NEC|TCL|Alcatel|BIRD|DBTEL|Dopod|PHILIPS|HAIER|LENOVO|MOT-|Nokia|SonyEricsson|SIE-|Amoi|ZTE/.test(navigator.userAgent))){
	if(window.location.href.indexOf("?agent=m")<0){
		try{
			if(/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)){
				window.location.href=nowurl;
			}else if(/iPad/i.test(navigator.userAgent)){
			}else{
				window.location.href=nowurl;
			}
		}catch(e){}
	}
}
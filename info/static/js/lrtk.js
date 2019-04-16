var jq = jQuery.noConflict();
//明星站焦点
jq(function () {
    jq.extend({
        'foucs': function (con) {
            var $container = jq('#fullbanner')
                , $imgs = $container.find('li.plan')
            , $leftBtn = $container.find('a.prev')
            , $rightBtn = $container.find('a.next')
            , config = {
                interval: con && con.interval || 60000, //一分钟切换
                animateTime: con && con.animateTime || 300,  //自动切换时间
                direction: con && (con.direction === 'right'),
                _imgLen: $imgs.length
            }
            , i = 0
            , getNextIndex = function (y) { return i + y >= config._imgLen ? i + y - config._imgLen : i + y; }
            , getPrevIndex = function (y) { return i - y < 0 ? config._imgLen + i - y : i - y; }
            , silde = function (d) {
                $imgs.eq((d ? getPrevIndex(2) : getNextIndex(2))).css('left', (d ? '-2088px' : '2088px'))
                $imgs.animate({
                    'left': (d ? '+' : '-') + '=1044px'
                }, config.animateTime);
                i = d ? getPrevIndex(1) : getNextIndex(1);
            }
            , s = setInterval(function () { silde(config.direction); }, config.interval);
            $imgs.eq(i).css('left', 0).end().eq(i + 1).css('left', '1044px').end().eq(i - 1).css('left', '-1044px');
            $container.find('.wrappic').add($leftBtn).add($rightBtn).hover(function () { clearInterval(s); }, function () { s = setInterval(function () { silde(config.direction); }, config.interval); });
            $leftBtn.click(function () {
                if (jq(':animated').length === 0) {
                    silde(false);
                }
            });
            $rightBtn.click(function () {
                if (jq(':animated').length === 0) {
                    silde(true);
                }
            });
        }
    });
}(jQuery));


//mouseover
jq(document).ready(function(){		
	jq('.imgcont').mouseover(function(){
		jq(this).stop().fadeTo(200,1);
		jq(".fdsm",this).stop().animate({bottom:'0px'},{queue:false,duration:200});//速度300 越高越慢
	})
	jq('.imgcont').mouseout(function(){
		jq(this).stop().fadeTo(200,1);
		jq(".fdsm",this).stop().animate({bottom:'-60px'},{queue:false,duration:200});//速度300 越高越慢
	})
	//通用
	jq('.ty-imgcont').mouseover(function(){
		jq(this).stop().fadeTo(200,1);
		jq(".ty-fdsm",this).stop().animate({bottom:'0px'},{queue:false,duration:200});//速度300 越高越慢
	})
	jq('.ty-imgcont').mouseout(function(){
		jq(this).stop().fadeTo(200,1);
		jq(".ty-fdsm",this).stop().animate({bottom:'-31px'},{queue:false,duration:200});//速度300 越高越慢
	})

});


//gotop
jq(document).ready(function(){
	jq('<a href="#" id="retop">返回顶部</a>').appendTo('body').fadeOut().click(function(){
		jq(document).scrollTop(0);
		jq(this).fadeOut();
		return false
	});
	var $retop = jq('#retop');
	function backTopLeft(){
		var btLeft = jq(window).width() / 2 + 535;
		if (btLeft <= 950){
			$retop.css({ 'left': 965 })
		}else{
			$retop.css({ 'left': btLeft }) 
		}
	}
	backTopLeft();
	jq(window).resize(backTopLeft);
	jq(window).scroll(function(){
		if (jq(document).scrollTop() === 0){
			$retop.fadeOut()
		}else{
			$retop.css({'display':'block'})
		}
		if (jq.browser.msie && jq.browser.version == 6.0 && jq(document).scrollTop() !== 0){
			$retop.css({ 'opacity': 1 })
		} 
	});
	
});


//排行榜
var accordion=function(){
	var tm=sp=1; //切换过渡时间
	function slider(n){this.nm=n; this.arr=[]}
	slider.prototype.init=function(t,c,k){
		var a,h,s,l,i; a=document.getElementById(t); this.sl=k?k:'';
		h=a.getElementsByTagName('dt'); s=a.getElementsByTagName('dd'); this.l=h.length;
		for(i=0;i<this.l;i++){var d=h[i]; this.arr[i]=d; d.onmouseover=new Function(this.nm+'.pro(this)'); if(c==i){d.className=this.sl}}
		l=s.length;
		for(i=0;i<l;i++){var d=s[i]; d.mh=d.offsetHeight; if(c!=i){d.style.height=0; d.style.display='none'}}
	}
	slider.prototype.pro=function(d){
		for(var i=0;i<this.l;i++){
			var h=this.arr[i], s=h.nextSibling; s=s.nodeType!=1?s.nextSibling:s; clearInterval(s.tm);
			if((h==d&&s.style.display=='none') || (h==d&&s.style.display=='')){s.style.display=''; su(s,1); h.className=this.sl}
			else if(s.style.display==''){su(s,-1); h.className=''}
		}
	}
	function su(c,f){c.tm=setInterval(function(){sl(c,f)},tm)}
	function sl(c,f){
		var h=c.offsetHeight, m=c.mh, d=f==1?m-h:h; c.style.height=h+(Math.ceil(d/sp)*f)+'px';
		//c.style.opacity=h/m; c.style.filter='alpha(opacity='+h*100/m+')'; //区块渐变过渡 暂时取消
		if(f==1&&h>=m){clearInterval(c.tm)}else if(f!=1&&h==1){c.style.display='none'; clearInterval(c.tm)}
	}
	return{slider:slider}
}();

//end

(function(a) {
    a.fn.waterfall = function(o, g, j) {
        var i = this;
        if (i.length <= 0) {
            return
        }
        if (typeof o !== "function") {
            j = g;
            g = o;
            o = a.noop
        }
        if (typeof g !== "string") {
            j = g;
            g = ""
        }
        var c = a.extend({},a.fn.waterfall.defaults, j);
        c.fn = o;
        var k,r = [];
        var q = !!g;
        var e = q ? a(g, i) : i , m = c.focus;
        if (q) {
            i.delegate(g, "mouseover mousemove", f);
            i.delegate(g, "mouseout", d)
        } else {
            i.bind("mouseover mousemove", f);
            i.bind("mouseleave", d)
        }
        n();
        function n() {
            for (var u = 0; u < e.length; u++) {
                var s = e.eq(u),
                v = s[0].scrollHeight,
                t = s.children().clone();
                s.append(t).data("cur", 0);
                if (c.async) {
                    p(u, u * c.gap + c.wait)
                }
            }
            h()
        }
        function h() {
            window.clearTimeout(k);
            k = window.setTimeout(function() {
                var s = e.index(e.filter("." + m));
                p((s + 1) % e.length);
                h()
            },
            c.autodelay)
        }
        function f() {
            a(this).attr("waiting", "1")
        }
        function d() {
            var t = a(this),
            s = e.index(t);
            a(this).removeAttr("waiting");
            if (c.mouseleavedo) {
                p(s)
            }
        }
        function l(s) {
            return
        }
        function b(v, y) {
            var v = v.not(":animated").not("[waiting],[sliding]");
            if (!v.length) {
                return
            }
            v.attr("sliding", "1");
            var x = v.children(),
            w = v.scrollTop(),
            u = v.data("cur"),
            s = x.length / 2;
            if (w < 10) {
                u = s - 1;
                w = x.eq(s).position().top;
                v.scrollTop(w)
            }
            var t = x.eq(u).position().top;
            v.animate({
                scrollTop: "+=" + t
            },
            c.anitime, 
            function() {
                a(this).data("cur", (s + (--u)) % s).removeAttr("sliding").removeAttr("waiting")
            });
            if (c.async) {
                v.delay(c.anidelay).queue(function() {
                    b(v);
                    a(this).dequeue()
                })
            }
        }
        function p(t, u) {
            var s = e.eq(t),
            u = u || 0;
            e.removeClass(m).eq(t).addClass(m);
            a({}).delay(u).queue(function() {
                if (s.children().length) {
                    if (c.down) {
                        b(s, true)
                    } else {
                        l(s, true)
                    }
                }
                a(this).dequeue()
            })
        }
        return i
    };
    a.fn.waterfall.defaults = {
        down: true,
        focus: "cur",
        index: 0,
        event: "click",
        mouseleavedo: false,//鼠标悬浮停止
        async: true,//开启随机滚动
        wait: 10000,
        gap: 10000,
        anidelay: 14000,
        anitime: 100,//滚动速度
        autodelay: 3000//间隔时间
    }
})(jQuery);

jq(function() {
    jq("#waterfall").waterfall("div.dym-dl", {index: 3})
});

jq(function(){
	jq(".tag_item").each(function(i, target){
		jq(target).mouseenter(function(e){
			//stop current animation.
			jq(target).stop();
			jq(target).find(".taglist").stop(false, true);
			jq(target).parent().addClass("curr");
			jq(".tag_item").not(jq(target)).addClass("not_curr");
			jq(target).animate({
				
				<!--鼠标滑过 图片的尺寸-->
				width: "200px",
				height: "144px",
				top: "-20px",
				left: "-24px"
			}, "normal");
		});
		jq(target).mouseleave(function(e){
			//stop current animation.
			jq(target).stop();
			jq(target).find(".taglist").stop(false, true);
			jq(target).parent().removeClass("curr");
			jq(".tag_item").not(target).removeClass("not_curr");
			jq(target).animate({
				width: "146px",
				height: "105px",
				top: "0",
				left: "0"
			}, "normal");
		});
	})
});



function browserRedirect() {  
	var sUserAgent = navigator.userAgent.toLowerCase();  
	var bIsIpad = sUserAgent.match(/ipad/i) == "ipad";  
	var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os";  
	var bIsMidp = sUserAgent.match(/midp/i) == "midp";  
	var bIsUc7 = sUserAgent.match(/rv:1.2.3.4/i) == "rv:1.2.3.4";  
	var bIsUc = sUserAgent.match(/ucweb/i) == "ucweb";  
	var bIsAndroid = sUserAgent.match(/android/i) == "android";  
	var bIsCE = sUserAgent.match(/windows ce/i) == "windows ce";  
	var bIsWM = sUserAgent.match(/windows mobile/i) == "windows mobile";  
	if ((bIsIpad || bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM) ){  
		document.write("<div style='width:100%; min-width:1044px; overflow:hidden; line-height:1.8em; font-size:2em; text-align:center; margin-top:10px;'>您使用了移动设备访问唯一图库！<br>强烈建议您访问唯一图库移动端网页 以达到最佳体验。 <br>移动端地址：<a href='http://m.mmonly.cc' style='font-size:3em;'>http://m.mmonly.cc</a></div>'") 
		//alert("您使用了移动设备访问搜优图片站！强烈建议您访问搜优图移动端网页 以达到最佳体验。 移动端地址：http://m.souutu.com");
			} 
		}
//browserRedirect();
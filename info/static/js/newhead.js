// JavaScript Document
//nav
$(document).ready(function(){

	$("#jq_topmenu li").hover(function(){
		$(this).addClass("hover").find("div.jq_hidebox").show();
	},function(){
		$(this).removeClass("hover").find("div.jq_hidebox").hide();
	});

});
//piclink
$(document).ready(function(){
	$("#nav li").hover(function(){
		$(this).find("ul").slideDown("slow");	
	},function(){
		$(this).find("ul").slideUp("fast");	
	});
});
function SouutuIMGupNext(bigimg){
	var lefturl		= $("#bigImg").attr('data-Lurl');
	var righturl	= $("#bigImg").attr('data-Rurl');
	var imgurl		= righturl;
	var width	= bigimg.width;
	var height	= bigimg.height;
	bigimg.onmousemove=function(){
		if(event.offsetX<width/2){
			bigimg.style.cursor	= 'url(http://www.mmonly.cc/skins/images/arr_left.cur),auto';
			imgurl= lefturl;
		}else{
			bigimg.style.cursor	= 'url(http://www.mmonly.cc/skins/images/arr_right.cur),auto';
			imgurl= righturl;
		}
	}
	bigimg.onclick=function(){
		top.location=imgurl;
	}
};
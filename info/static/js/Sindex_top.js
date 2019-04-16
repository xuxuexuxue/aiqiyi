// JavaScript Document
var currentindex=1;
function changeflash(i){	
	currentindex=i;
	for(j=1;j<=6;j++){
		if(j==i){
			jQuery("#flash"+j).fadeIn("normal");
			jQuery("#flash"+j).css("display","block");
			jQuery("#f"+j).removeClass();
			jQuery("#f"+j).addClass("dq");
			jQuery("#flashBg").css("background-color",jQuery("#flash"+j).attr("name"));
			jQuery("#imgalt"+j).text(jQuery("#flash"+j).attr("imgsm"));
		}else{
			jQuery("#flash"+j).css("display","none");
			jQuery("#f"+j).removeClass();
			jQuery("#f"+j).addClass("no");
		}
	}
}

function startAm(){
	timerID = setInterval("timer_tick()",3000);
}

function stopAm(){
	clearInterval(timerID);
}

function timer_tick(){
	currentindex=currentindex>=6?1:currentindex+1;
	changeflash(currentindex);
}
jQuery(document).ready(function(){

	jQuery(".flash_bar div").mouseover(function(){
		stopAm();
	}).mouseout(function(){
		startAm();
	});
	startAm();
});

jQuery(document).ready(function(){
	jQuery("#jq_topmenu li").hover(function(){
		jQuery(this).addClass("hover").find("div.jq_hidebox").show();
	},function(){
		jQuery(this).removeClass("hover").find("div.jq_hidebox").hide();
	});
});
//nav
jQuery(document).ready(function(){
	jQuery("#nav li").hover(function(){
		jQuery(this).find("ul").slideDown("slow");	
	},function(){
		jQuery(this).find("ul").slideUp("fast");	
	});
});
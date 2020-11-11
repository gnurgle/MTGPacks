var clicked = 0;
var flipped = 0;
var sub_total = 0;
var $items = $('.card_click');
var pack_total = 0;
var opened = 0;
var profitable = 0;
var prev_pack = 0;
var pack_name = "";

$('.card_click').one('click',function(){
  $(this).toggleClass('flipped');
  clicked = clicked + 1;
  	if (clicked + flipped >= 15)
		$('.overlay_button').css("visibility", "visible");
});

$('.card').one("mouseenter",function(){
    $(this).toggleClass('flipped');
  flipped = flipped + 1;
  	if (clicked + flipped >= 15)
		$('.overlay_button').css("visibility", "visible");

});

function reload() {
  	if (clicked + flipped >= 15)
		loadlink();
};

function flip(){
  $(this).toggleClass('flipped');
};

function storePack(vars){
pack_name = vars;
}


function loadlink(){
	$('.overlay_button').css("visibility", "hidden");

	animateCSS('.outbox','zoomOut').then(() => {
	$('.outbox').hide();
	$('#superout').load("/" + pack_name + " #superout > *");

			});
	//animateCSS('.outbox','zoomIn').then(() => {
	clicked = 0;
	flipped = 0;
	$(document).on("mouseenter", ".card", function(){
			var $this=$(this);
			if ($this.data('mouseentered')){
			return false;
			}
			$this.data('mouseentered',true); 
			$(this).toggleClass('flipped'); 
			clicked = clicked + 1; 
		  	if (clicked + flipped >= 15)
				$('.overlay_button').css("visibility", "visible");
		  });
	$(document).on('click', '.card_click', function(){
			var $this=$(this);
			if ($this.data('mouseentered')){
			return false;
			}
			$this.data('mouseentered',true);
  		$(this).toggleClass('flipped');
  		clicked = clicked + 1;
	  	if (clicked + flipped >= 15)
			$('.overlay_button').css("visibility", "visible");
	});


}

function addTotal(vars){
		sub_total = sub_total + vars
		$(".counter").countimator({
		value: sub_total
		});
	
}


function addPackPrice(vars){
		pack_total = pack_total + vars
		$(".pack_counter").countimator({
		value: pack_total
		});
}

function getProfit(){
		var profit = sub_total - pack_total
		prev_pack = profit
		$(".profit_counter").countimator({
		value: profit
		});
}

function getOpened(){
		opened = opened + 1
		$(".opened_counter").countimator({
		value: opened
		});
}

function getProfitable(pull,pack){
		if (arguments[0] > arguments[1]){
			profitable = profitable + 1
			}
		$(".profitable_counter").countimator({
		value: profitable
		});
}


function getNonProfit(){
		var nonprofit = opened-profitable
		$(".nonprofit_counter").countimator({
		value: nonprofit
		});
}

$(function (){
	$(".counter").countimator();
	$(".pack_counter").countimator();
	$(".profit_counter").countimator();
});

//Code from Animate to add animation then remove
const animateCSS = (element, animation, prefix = 'animate__') =>
  // We create a Promise and return it
  new Promise((resolve, reject) => {
    const animationName = `${prefix}${animation}`;
    const node = document.querySelector(element);

    node.classList.add(`${prefix}animated`, animationName);

    // When the animation ends, we clean the classes and resolve the Promise
    function handleAnimationEnd() {
      node.classList.remove(`${prefix}animated`, animationName);
      resolve('Animation ended');
    }

    node.addEventListener('animationend', handleAnimationEnd, {once: true});
  });

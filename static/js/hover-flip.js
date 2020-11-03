var clicked = 0;
var flipped = 0;
var sub_total = 0;
var $items = $('.card_click');
var pack_total = 0;
var pack_name = "";

$('.card_click').one('click',function(){
  $(this).toggleClass('flipped');
  clicked = clicked + 1;
});

$('.card').one("mouseenter",function(){
    $(this).toggleClass('flipped');
  flipped = flipped + 1;
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

    $('#superout').load("/" + pack_name + " #superout > *");

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
		  });
	$(document).on('click', '.card_click', function(){
			var $this=$(this);
			if ($this.data('mouseentered')){
			return false;
			}
			$this.data('mouseentered',true);
  		$(this).toggleClass('flipped');
  		clicked = clicked + 1;
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
		var profit = sub_total- pack_total
		$(".profit_counter").countimator({
		value: profit
		});
}

$(function (){
	$(".counter").countimator();
	$(".pack_counter").countimator();
	$(".profit_counter").countimator();
});

$(".coverflow").flipster({
style:'carousel',
spacing: -0.5,
nav:true,
buttons:true,
loop:true,
onItemSwitch: (currentItem, previousItem) => {
	console.log(currentItem.id)
	logoSwap(currentItem.id)
	}

});


var myFlipster = $(".coverflow:".flipster)

function logoSwap(id){
	var img_rp = "static/img/"+id+"_logo.png"
	console.log(img_rp)
	document.getElementsByClassName("set_logo")[0].src = img_rp;
};

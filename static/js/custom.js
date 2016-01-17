// Jquery with no conflict
jQuery(document).ready(function($) {   
	
	    
	//##########################################
	// Bg stretcher
	//##########################################

	var theWindow        = $(window);
	
		var originalBg = "img/bg/blue.jpg";
	
	$.backstretch(
		originalBg,
		{fade: 750,
		duration: 4000});




	//##########################################
	// FIX FOOTER AT BOTTOM
	//##########################################	
	function fixFooterBottom(){
		var h = $('#scroll-holder').height()*2;
		$('#footer-container-fixed').css({
			marginTop: function(index, value){ return h }
		});
	}
	
    
    
    //##########################################
	// Tool tips
	//##########################################
	
    $('.poshytip').poshytip({
    	className: 'tip-twitter',
		showTimeout: 1,
		alignTo: 'target',
		alignX: 'center',
		offsetY: 5,
		allowTipHover: false
    });
    
    $('.form-poshytip').poshytip({
		className: 'tip-yellowsimple',
		showOn: 'focus',
		alignTo: 'target',
		alignX: 'right',
		alignY: 'center',
		offsetX: 5
	});
	
    //##########################################
	// Rollover
	//##########################################

	$("#sidebar li a").hover(function() { 
		// on rollover	
		$(this).stop().animate({ 
			marginLeft: "8" 
		}, "fast");
	} , function() { 
		// on out
		$(this).stop().animate({
			marginLeft: "0" 
		}, "fast");
	});
		                                        
	//##########################################
	// Scrolling bar
	//##########################################
	
	function starScrolling(){
		$("div#makeMeScrollable").smoothDivScroll({ 
			autoScrollingMode: "onstart" , 
			autoScrollingDirection: "endlessLoopRight", 
			autoScrollingStep: 1, 
			autoScrollingInterval: 10,	
			startAtElementId: "startAtMe",
			visibleHotSpotBackgrounds: "always",
			setupComplete: centerScroll,
			windowResized: centerScroll
		});
	};

	// centers the scroll on resize
	
	function centerScroll(){
		var h = $(window).height()/2 - $('#scroll-holder').height()/2;
		$('#scroll-holder').css({
			top: function(index, value){ return h }
		});
	}
	
	
	function hideScroller(settings){
		$("#scroll-holder").hide();
		$("#makeMeScrollable").smoothDivScroll("hide");
		$("#gallery-holder").hide();
		$("#image-buttons").show();
		$('#nav').hide();
		setDescription(settings);
	}
	
	function showScroller(){
		$("#scroll-holder").show();
		$("#makeMeScrollable").smoothDivScroll("show");
		$("#image-buttons").hide();
		$('#nav').show();
		$('#image-description').hide();
		fixFooterBottom();
		$.backstretch(
			originalBg,
			{fade: 750,
			duration: 4000});
	}
	
	function setDescription(settings){
		img_title = settings.attr('title');
		img_desc = settings.children('img').attr('alt');
		setImageDescription(img_title, img_desc);	
	}
	
	function changeBg(settings){
		$('#bg').hide('');
		// put loader image
		$('#no-bg-click').addClass('loading-img');
		// load image on Bg and call resizeBg
		$.backstretch(
			settings.attr('href'),
			{fade: 750,
			duration: 4000});
	}
	
	
	
	// Click image, Open image on background
	$("div#makeMeScrollable a").click(function(){
		hideScroller($(this));
		changeBg($(this));
		return false;
	});
	
	
	// Close button
	$('#image-buttons #close-image').click(function(){
		$("div#gallery-holder").fadeIn();
		showScroller();
	});
	
	// Open description
	$('#image-buttons #info-button').click(function(){
		$('#image-description').fadeToggle();
	})
	
	
	//##########################################
	// Footer toggle
	//##########################################
	
	var footerContainer = jQuery('#footer-container');
	var footerTrigger = jQuery('#footer-open a');
	
	var footerContainerHeight = footerContainer.height() + 3;

	footerContainer.css({
		marginBottom : -footerContainerHeight,
		display : 'block'
	});
	
	footerTrigger.toggle( function() {
	
		footerContainerHeight = footerContainer.height() + 3;
		
		footerContainer.animate({
			marginBottom : 0
		}, 700, 'easeOutExpo');
		footerTrigger.addClass('footer-close');
	}, function() {
		footerContainer.animate({
			marginBottom : -footerContainerHeight
		}, 700, 'easeOutExpo');
		footerTrigger.removeClass('footer-close');
	});

		
	//##########################################
	// Resize event
	//##########################################
	
	theWindow.resize(function() {
	    fixFooterBottom();
	}).trigger("resize");
	
	//##########################################
	// Pretty photo
	//##########################################
	
	$("a[rel^='prettyPhoto']").prettyPhoto();
	
	
	//##########################################
	// Nav menu
	//##########################################
	
	$("ul.sf-menu").superfish({ 
        animation: {height:'show'},   // slide-down effect without fade-in 
        delay:     800 ,              // 1.2 second delay on mouseout 
        autoArrows:  false,
        speed:         'normal'
    });


	//##########################################
	// QUICKSAND FILTER
	//##########################################	
	
	// get the initial (full) list
	
	var $filterList = $('ul#portfolio-list');
		
	// Unique id 
	for(var i=0; i<$('ul#portfolio-list li').length; i++){
		$('ul#portfolio-list li:eq(' + i + ')').attr('id','unique_item' + i);
	}
	
	// clone list
	var $data = $filterList.clone();
	
	
	// Click
	$('#portfolio-filter a').click(function(e) {
		if($(this).attr('rel') == 'all') {
			// get a group of all items
			var $filteredData = $data.find('li');
		} else {
			// get a group of items of a particular class
			var $filteredData = $data.find('li.' + $(this).attr('rel'));
		}
		
		// call Quicksand
		$('ul#portfolio-list').quicksand($filteredData, {
			duration: 500,
			attribute: function(v) {
				// this is the unique id attribute we created above
				return $(v).attr('id');
			}
		}, function() {
	        // restart functions
	        galleryRestart();
		});
		// remove # link
		e.preventDefault();
	});
	
    
    // set the description from the image at the description holder
    function setImageDescription(title, desc){
    	$('#image-description .title').text(title);
    	$('#image-description .desc').text(desc);
    	return false;
    }
    
	galleryRestart();
	
	function galleryRestart(){
	    // open image
	    $("#portfolio-list a").click(function(){
	    	// only if not prettyPhoto
	    	if($(this).attr('rel') != "prettyPhoto" ){
		    	// set description
				setDescription($(this));
				hideScroller($(this));
				changeBg($(this));
				return false;
			}
		});
		
		// tooltip
		 $('.gallery-thumbs img').poshytip({
	    	className: 'tip-twitter',
			showTimeout: 1,
			alignTo: 'target',
			alignX: 'center',
			offsetY: 5,
			allowTipHover: false
	    });
	    
	    // prettyPhoto restart
	    $("a[rel^='prettyPhoto']").prettyPhoto();
	}
	
	
	
	//##########################################
	// On load page
	//##########################################

	theWindow.load(function(){
		// Hide footer at first
		footerContainerHeight = footerContainer.height() + 3;
		footerContainer.animate({
			marginBottom : -footerContainerHeight
		}, 1, 'easeOutExpo');// Center and resize after all page is loaded
		fixFooterBottom();
	});
	
	fixFooterBottom();
	starScrolling();
	




});

// search clearance	
function defaultInput(target){
	if((target).value == 'Search...'){(target).value=''}
}

function clearInput(target){
	if((target).value == ''){(target).value='Search...'}
}

// Skin changer (for demo only)

function changeSkin(skin){
	document.getElementById('css-skins').href = 'skins/'+skin+'.css';
	
	if(skin == "dark"){
		logo = 'img/logo-dark.png';
	}else{
		logo = 'img/logo.png';
	}
	document.getElementById('logo').src = logo;
	
}

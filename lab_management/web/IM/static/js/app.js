// JavaScript Document

var main = function() {
  /* Push the body and the nav over by 285px over */
  $('.icon-menu').click(function() {
    $('.menu').animate({
      left: "0px"
    }, 200);

    $('body').animate({
      left: "285px"
    }, 200);
  });

  /* Then push them back */
  $('#close-menu').click(function() {
    $('.menu').animate({
      left: "-285px"
    }, 200);

    $('body').animate({
      left: "0px"
    }, 200);
  });
  
  $('#messages-menu').hide();
  $('#messages-icon').click(function(){
	 $('#main-menu').hide();
	 $('#messages-menu').show();
  });
  
  $('#close-messages-menu').click(function(){
	 $('#messages-menu').hide();
	 $('#main-menu').show();
  });
  
  
  /* Button-click to flip card */
  $('.flip-btn').click(function(){
	 $('.flip-container').toggleClass('flip'); 
  });
  
  
  var cards = new Array();
  cards.push('#Inventories');
  cards.push('#Users');
  cards.push('#MyItems');
  cards.push('#MyMessages');
  
  /* Hide the other cards */
  for(var i=1; i < cards.length; i++){
	  $(cards[i]).hide();
  }

  /* Button-click to switch card */
  var current_index = 0;
  $('.switch-btn').click(function(){
	 if ((current_index+1) == cards.length) {
		$(cards[current_index]).hide();
		$(cards[0]).show('slide', {direction: 'right'}, 1000);
		current_index = 0;
	 }else{
		$(cards[current_index]).hide('slide', {direction: 'left'}, 100);
		$(cards[current_index+1]).show('slide', {direction: 'right'}, 1000); 
		current_index += 1
	 }
  });
  
  /* Choose in menu to show the according card*/
  $('#main-menu p').click(function(){
	 $(cards[current_index]).hide();
	 var clicked_item = $(this).html();
	 clicked_item = clicked_item.replace(" ",'');
	 for (var i=0; i<cards.length; i++){
		 if (cards[i] == '#'+ clicked_item){
			 current_index = i;
		 }
	 }
	 $(cards[current_index]).show();
  });
  
  /* check items */
  $('.check-item').click(function(){
	  /*check-head change according to check-item*/
	  if ($('.check-item:checked').length == $('.check-item').length) {
	        $('#check-head').prop('checked', true);
	  }
	  else {
	        $('#check-head').prop('checked', false);
	  }
	  /*operation show and hide according to checked item*/
	  if ($('.check-item:checked').length) {
		  $('.operation').css('visibility', 'visible');
		  
	  }else{
	      $('.operation').css('visibility', 'hidden');
	  }
  });
  
  /* check-head: select/unselect all*/
  $('#check-head').change(function(){
		 $('.check-item').prop('checked', $(this).prop('checked'));
		 if (this.checked == true){
 			 $('.operation').css('visibility', 'visible')
 		  }else{
 			 $('.operation').css('visibility', 'hidden');
 		  }
  });
  
  /*apply operation on checked items*/
  $('#operation-delete').click(function(){
	 checked_items = new Array();
	 if($('.check-item:checked').length){
		 $('.check-item:checked').each(function(){
			  var currentRow = this.parentNode.parentNode;
			  var column = currentRow.getElementsByTagName("td")[1];
			  var rowID = column.textContent;
			  
			  checked_items.push(rowID);
		 });
	 }
		 $.ajax({
			url: "http://127.0.0.1:5000/delete-inventory",
			type: "POST",
			data: {rows:checked_items},

			async: true,
		 }).done(function(data){
			 alert(data.result);
			 location.reload();
		 });
		
  });
  
  $('#operation-borrow').click(function(){
	 checked_items = new Array();
	 if($('.check-item:checked').length){
		 $('.check-item:checked').each(function(){
			  var currentRow = this.parentNode.parentNode;
			  var column = currentRow.getElementsByTagName("td")[1];
			  var rowID = column.textContent;
			  
			  checked_items.push(rowID);
		 });
	 }
	 
	 username = $('.user-name').val();
	 
	 $.ajax({
		url: "http://127.0.0.1:5000/borrow",
		type: "POST",
		data: {rows:checked_items, username: username},

		async: true,
	 }).done(function(data){alert(data.result);});
  });
  
  
  $('#search-inventory').keydown(function(event){
	  if (event.which == 13){
		  search_string = $('#search-inventory').val();
		  $.ajax({
			 url: "http://127.0.0.1:5000/search-user",
			 type: "POST",
			 data: {search_string: search_string},
			 async: true,
		  }).done(function(data){alert(data.result);});
	  }
  });
  
  var tag = $("#tag"),
  name = $("#name"),
  PN = $("#PN"),
  SN = $("#SN"),
  ship = $("#shipping"),
  cap = $("#capital"),
  dis = $("#disposition"),
  status = $("#status"),
  owner = $("#owner"),
  error = $("#dialog-form .error-msg")
  allFields = $([]).add(tag).add(name).add(PN).add(SN).add(ship).add(cap).add(dis).add(status).add(owner);
  
  $('#dialog-form').dialog({
	  autoOpen: false,
	  resizable: false,
	  height: 500,
	  width: 250,
	  modal: true,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
        effect: "blind",
        duration: 500
      },
      buttons: {
    	  "Add an inventory": function() {
    		  error.hide();
              var bValid = true;
//              allFields.removeClass( "ui-state-error" );
//     
//              bValid = bValid && checkLength( tag, "username", 3, 16 );
//              bValid = bValid && checkLength( name, "email", 6, 80 );
//             
//              bValid = bValid && checkRegexp( name, /^[a-z]([0-9a-z_])+$/i, "必须由 a-z、0-9、下划线组成，且必须以字母开头。" );
//              // From jquery.validate.js (by joern), contributed by Scott Gonzalez: http://projects.scottsplayground.com/email_address_validation/
//              //bValid = bValid && checkRegexp( email, /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i, "eg. ui@jquery.com" );
//              //bValid = bValid && checkRegexp( password, /^([0-9a-zA-Z])+$/, "密码字段只允许： a-z 0-9" );
//     
              if ( bValid ) {
	        	  $.ajax({
	     			 url: "http://127.0.0.1:5000/add-inventory",
	     			 type: "POST",
	     			 data: {tag: tag.val(),
	     				 	name: name.val(),
	     				 	PN: PN.val(),
	     				 	SN: SN.val(),
	     				 	ship: ship.val(),
	     				 	cap: cap.val(),
	     				 	dis: dis.val(),
	     				 	status: status.val(),
	     				 	owner: owner.val(),
	     			 },
	     			 async: true,
	     		  }).done(function(data){
	     			  var inv = data.result
	     			  if (inv) {
	     				 $( ".inventory-table" ).append( "<tr>" +
		     	                  "<td><input type='checkbox' class='check-item'/></td>" +
		     	                  "<td style='display:none;' class='inventory-id'>" + inv[0] + "</td>" +
		     	                  "<td align='center'>" + inv[1] + "</td>" +
		     	                  "<td align='center'>" + inv[2] + "</td>" +
		     	                  "<td align='center'>" + inv[3] + "</td>" +
		     	                  "<td align='center'>" + inv[4] + "</td>" +
		     	                  "<td align='center'>" + inv[5] + "</td>" +
		     	                  "<td align='center'>" + inv[6] + "</td>" +
		     	                  "<td align='center'>" + inv[7] + "</td>" +
		     	                  "<td align='center'>" + inv[8] + "</td>" +
		     	                  "<td align='center'>" + inv[9] + "</td>" +
		     	              	  "</tr>" );
	     				 $( '#dialog-form' ).dialog( "close" );
	     			  }
	     			  else {
	     				  error.show();
	     			  }
	     		  });
                
              }
            },
            Cancel: function() {
              $( this ).dialog( "close" );
            }
          },
      close: function() {
        allFields.val( "" ).removeClass( "ui-state-error" );
      }
   });
      
  
  $('.new-btn').click(function(){
	 $('#dialog-form').dialog("open"); 
	 error.hide();
  });

  
  $('#export-excel').click(function(){
	  $.ajax({
			 url: "http://127.0.0.1:5000/export-excel",
			 type: "GET",
			 async: false,
		  });
  });
  
};


$(document).ready(main);
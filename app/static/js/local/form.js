/* global $ */
/* global moment */
// DateTimePicker
$(document).ready(function(){
  $('.selectpicker').selectpicker();
});

$('#datetimepicker0').datetimepicker({
    useCurrent: false,
    format: 'MM/DD/YY',
    minDate: moment().add(14,'days')
});

// Prevents Enter Key from being pressed
$('#userForm').on('keyup keypress', function(e) {
  var keyCode = e.keyCode || e.which;
  if (keyCode === 13) { 
    e.preventDefault();
    return false;
  }
});

$(function () {
  $('[data-toggle="popover"]').popover()
})

function removeSelectPickerRequired(){
  //This is necessary because of Internet explorer
  document.getElementById("requestor[]").required = false;
}


// checks to make sure form is valid before the modal is shown. 
function validate() {
  var required = document.getElementById("userForm").querySelectorAll("[required]");
  var stop = 0;
  for ( var i = 0, element; element = required[i++];){
    console.log(element.value);
    if (element.value == ""){
      stop = stop + 1;
    }
  }
  var email = document.getElementById('email').value;
  if (email.indexOf('@') == -1){
    stop = stop + 1;
  }
  if (email.indexOf('.') == -1){
    stop = stop + 1;
  }
  if (stop === 0){
     removeSelectPickerRequired();
     $('#reviewRequest').modal('show');
     fillModal();
  }
  else{
     document.getElementById('submit').click();
  }
}

// gets selected items from dropdown menu and fills the corresponding field in the modal. 
function getDropdown(formId, reviewId) {
   var x =document.getElementById(formId);
   var data_list= [];
   for (var i = 0; i < x.options.length; i ++) {
    if(x.options[i].selected){
      data_list.push(x.options[i].text);
    }
  }
  // deletes all previous items
  var myNode = document.getElementById(reviewId);
  while (myNode.firstChild) {
    myNode.removeChild(myNode.firstChild);
  }
  document.getElementById(reviewId).innerHTML = "";
  for (var item in data_list) {
    var listItem = "<ul class= list-unstyled >" + "<li>" + data_list[item] + "</li>" + "</ul>";
    document.getElementById(reviewId).innerHTML += listItem;
  }
  
}

//get text form text area and fills the corresponding field in the modal. 
function getText(formId, reviewId) {
  var textInput = document.getElementById(formId).value;
  document.getElementById(reviewId).innerHTML = "";
  document.getElementById(reviewId).innerHTML = textInput;
}

// gets selected values from checkboxes and fills the corresponding field in the modal.
function getChecked(formId, reviewId) {
  var checkboxes = document.getElementsByName(formId);
  var data_list = []; 
  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      var x =$('label[for='+checkboxes[i].value+']');
      //console.log(x.text())
      data_list.push(x.text());
      //console.log(data_list)
    }
  }
  console.log(data_list)
  // deletes all previous items
  var myNode = document.getElementById(reviewId);
  while (myNode.firstChild) {
    myNode.removeChild(myNode.firstChild);
  }
  document.getElementById(reviewId).innerHTMl = "";
  for (var item in data_list) {
    console.log(data_list[item])
    var listItem = "<ul class= list-unstyled >" + "<li>" + data_list[item] + "</li>" + "</ul>";
    document.getElementById(reviewId).innerHTML += listItem;
  }
  data_list = [];
}

//fills the modal with data from the form. 
function fillModal() {
  getText("phone", "phoneNumber");
  getText("department", "departmentName");
  getText("datetimepicker0", "dateNeeded");
  getText("email", "emailReview");
  getDropdown("requestor[]", "requestors");
  getText("purpose", "purposeReview");
  getText("output", "outputNeeded"); 
  getDropdown("format_type[]", "formatType");
  getText("selection", "selectionCriteria");
  getText("signature", "signer");
  getChecked("extra_groups[]", "additionalGroups"); 
  getChecked("excluded_groups[]", "excludedGroups");
  // checks to see if yes is checked
  if (document.getElementById("radio0").checked) {
      document.getElementById("bannerReview").innerHTML = "Yes";
  }
  else {
        document.getElementById("bannerReview").innerHTML = "No";
  }
  getText("additional-comments", "comments")
}


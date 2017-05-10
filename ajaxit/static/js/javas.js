function isEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}
function edit(emp_id1){

$.ajaxSetup({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
});
 $.ajax({
 type:"POST",
 async:true,
 url: "/ajaxit/editemployee/",
 data:
 {
 employee_id:emp_id1
 },
 error: function(xhr){
            alert("An error occured: " + xhr.status + " " + xhr.statusText);
 },
 success:function(result){
    empobj=JSON.parse(result)
    var person = prompt("New name",empobj.emp_name);
    var person_email = prompt("New Email",empobj.emp_email);
    var person_dob = prompt("New Date",empobj.emp_dob);
    var person_pass = prompt("New Password",empobj.emp_pass);

    var person_id=empobj.emp_id;
//    alert('successsssssssssssssss');
//    alert(person_id);
if(person!="" && person_email!="" && person_dob!="" && person_pass!="" &&person!=null && person_email!=null && person_dob!=null && person_pass!=null){
$.ajaxSetup({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
});
 $.ajax({
 type:"POST",
 async:true,
 url: "/ajaxit/editemployeefull/",
 data:
 {
 employee_name:person,employee_id:person_id,employee_email:person_email,employee_dob:person_dob,employee_pass:person_pass
 },
 error: function(xhr){
            alert("An error occured: " + xhr.status + " " + xhr.statusText);
 },
 success:function(resultet){

 document.getElementById('emplist').innerHTML=resultet



 }
});







}
else{
alert('Invalid information inserted')
}



}
});


}
function del(emp_idd){
 $.ajaxSetup({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
});
 $.ajax({
 type:"POST",
 async:true,
 url: "/ajaxit/delemployee/",
 data:
 {
 employee_id:emp_idd
 },
 error: function(xhr){
            alert("An error occured: " + xhr.status + " " + xhr.statusText);
 },
 success:function(result){
 document.getElementById('emplist').innerHTML=result
 }
});





}
$(document).ready(function()
{
$('#emp_add').click(

    function()
    {
        var emp_name=$('#id_emp_name').val();
        var emp_email=$('#id_emp_email').val();
        var emp_dob=$('#id_emp_dob').val();
        var emp_pass=$('#id_emp_pass').val();
        if(emp_name.length>25){
        alert('Name should be less than 25 characters')
        emp_name="";
        $('#id_emp_name').val("");
        }
        if(!isEmail(emp_email)){
        alert('Please provide a valid email address')
        $('#id_emp_email').val("");


        }
        if(emp_name==""|emp_email==""|emp_dob==""|emp_pass==""){
        alert('Empty fields not allowed');

        }
        else{


        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
});
 $.ajax({
 type:"POST",
 async:true,
 url: "/ajaxit/addemployee/",
 data:
 {
 employee_name:emp_name,employee_email:emp_email,employee_dob:emp_dob,employee_pass:emp_pass
 },
 error: function(xhr){
            alert("An error occured: " + xhr.status + " " + xhr.statusText);
 },
 success:function(result){
 document.getElementById('emplist').innerHTML=result
 }
});
}



});
});
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var pass = document.forms['vform']['password'];
var passconf = document.forms['vform']['comfirmpassword'];

function chk() {
if (pass.value != passconf.value) {
alert('Passwords dont match');
return false;
}
}
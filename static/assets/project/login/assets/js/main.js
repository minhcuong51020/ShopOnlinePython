const submit_button = document.getElementById("signup");
const errorMessage = document.getElementById("error-message");
submit_button.onclick = (e)=>{
	let pass = document.getElementById("pass");
	let rePass = document.getElementById("re_pass");
	let name = document.getElementById("name");
	let agree = document.getElementById("agree-term");
	if(name.value.length < 3){
		errorMessage.innerHTML="Tên người dùng phải có ít nhất 3 chữ cái";
		e.preventDefault()
		return
	}
	if(pass.value!=rePass.value){
		errorMessage.innerHTML="Password không trùng nhau"
		e.preventDefault()
		return
	}
	if(pass.value.length < 4){
		errorMessage.innerHTML="Mật khẩu phải chứa ít nhất 4 kí tự";
		e.preventDefault()
		return
	}
	if(agree.checked == false){
		errorMessage.innerHTML="Đọc điều khoản và tick vào ô xác nhận";
		e.preventDefault()
		return
	}
}
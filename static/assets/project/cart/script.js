let bookItemElement = document.querySelector("#content .book-item");
console.log(bookItemElement);
if(bookItemElement==null){
	document.querySelector("#content .cart-container").classList.add("display-none");
	document.querySelector("#content .empty-cart").classList.add("display");
}
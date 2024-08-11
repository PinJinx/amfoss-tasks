var cart = [];
const prd = document.querySelector('.product-Hlist');
var total = 0
window.addEventListener("load", Main);

function Main(){
    var cartData = sessionStorage.getItem("Cart");
    if (cartData) {
        cart = JSON.parse(cartData);
        console.log(cart);
    } else {
		console.log("Error in loading Cart");	
    }

	for (var i in cart) {
        var div = document.createElement("div");
        var price = document.createElement("div");
		var title = document.createElement("div");
		var txtdiv = document.createElement("div");
        var img = document.createElement("img");

        img.src = cart[i].image;
        img.classList.add("prd_item");
        div.classList.add("prdH");
        price.classList.add("price");
		title.classList.add("title");
		txtdiv.classList.add("prdHtext")
		total += parseInt(cart[i].price)
        var k = prd.appendChild(div);
        k.appendChild(img);
		tdiv = k.appendChild(txtdiv)

        var tl = tdiv.appendChild(title);
        tl.innerHTML = cart[i].title;

        var pr = tdiv.appendChild(price);
        pr.innerHTML = "$" + cart[i].price;

    }

	var element = document.getElementById("shopping_id");
	element.innerHTML = "Shopping id: "+(parseInt(Math.random() * 1000000000)).toString()

	var element = document.getElementById("tax");
	element.innerHTML = "Tax :$"+(total*0.08).toString()
	var element = document.getElementById("total");
	element.innerHTML = "Total Price :$"+(total+total*0.08).toString()
}
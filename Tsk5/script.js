const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');
const prd = document.querySelector('.product-list');
var cart = [];
var filtered_products = [];
var products = [];
var detail_product = [];



function handleInput(command) {
    var l = command.split(" ");
	if(l.length===2){
		if (l[0] === "search") {
			ListProducts(l[1]);
		} 
		else if (l[0] === "add") {
			if(filtered_products.length > 0){add(parseInt(l[1]));}
			else{terminalOutput.textContent += "No items to add!";}
		} 
		else if (l[0] === "remove") {
			if(filtered_products.length > 0){remove(parseInt(l[1]));}
			else{terminalOutput.textContent += "No items to remove!";}
		}
		else if(l[0] == "sort"){
			if(l[1].toLowerCase() == "price" ||l[1].toLowerCase() == "prices"){
				SortResults("p")
			}
			else if(l[1].toLowerCase() == "name" ||l[1].toLowerCase() == "names"){
				SortResults("n")
			}
		}
		else if(l[0] == "details" || l[0] == "detail"){
			details(parseInt(l[1]))
		}
	}
	else if(l.length === 1){
        switch (l[0]) {
            case 'help':
                viewCommand();
                break;
            case 'list':
                ListProducts();
                break;
            case 'cart':
                viewcart();
                break;
            case 'clear':
                ClearScreen();
                break;
			case 'buy':
				if(cart.length != 0){
					window.location.href = 'BuyPage.html';
				}
				else{
					terminalOutput.textContent += "No items in cart to buy!";
				}
				break
            default:
                terminalOutput.textContent += `Invalid command: ${command}\n`;
                break;
        }
    }
	else{
		var k = ""
		if(l[0] === "search"){
			for (i in l){
				if(i != 0 && i != 1){
					k+= " "+l[i]
				}
				else if(i == 1){
					k+= l[i]
				}
			}
			console.log(k);
			ListProducts(k);
		}
		else{
			terminalOutput.textContent += `Invalid command: ${command}\n`;
		}

	}
    terminalInput.value = '';
}


function SaveCartLocally(){
	var cartData = JSON.stringify(cart);
	sessionStorage.setItem("Cart",cartData );
}




window.addEventListener("load", Main);


terminalInput.addEventListener('keydown', (e) => {
    if (e.key === "Enter") {
        handleInput(e.target.value);
    }
});

function ClearScreen() {
    terminalOutput.innerHTML = "";
}

function viewCommand() {
	terminalOutput.innerHTML = ""
    terminalOutput.innerHTML += "Available Commands:\n";
    terminalOutput.innerHTML += "list: List all products\n";
	terminalOutput.innerHTML += "details [product_number]: Details of a products\n";
    terminalOutput.innerHTML += "add [product_number]: Add a product to cart\n";
    terminalOutput.innerHTML += "remove [product_number]: Remove a product to cart\n";
    terminalOutput.innerHTML += "cart: View your cart\n";
    terminalOutput.innerHTML += "buy: Buy all products in cart\n";
    terminalOutput.innerHTML += "search [query]: Search products by name\n";
    terminalOutput.innerHTML += "sort [price,name]: Sort products by price or name\n";
    terminalOutput.innerHTML += "clear: Clear the screen";
}

function details(i){
	if (detail_product.length !== 0 && detail_product.length - 1 >= i - 1 && i - 1 >= 0) {
		terminalOutput.innerHTML ="Name:\n"+ detail_product[i-1].title+"\nDescription:\n"+detail_product[i-1].description
    }
}


function add(i) {

	terminalOutput.innerHTML += "Item Added to Cart!\n";
    if (filtered_products.length !== 0 && filtered_products.length - 1 >= i - 1 && i - 1 >= 0) {
        cart.push(filtered_products[i - 1]);
    }
	SaveCartLocally()
}

function remove(i) {
    var l = [];
    if (filtered_products.length !== 0 && cart.length - 1 >= i - 1 && i - 1 >= 0) {
        for (var j in cart) {
            if (cart[j] !== cart[i - 1]) {
                l.push(cart[j]);
            }
        }
        cart = l;
    }
	SaveCartLocally()
}

function viewcart() {
    var k = 1;
	var element = document.getElementById("Main_heading");
	element.innerHTML = "My Cart"
    terminalOutput.innerHTML = "Cart Contents:\n";
    for (var i in cart) {
        terminalOutput.innerHTML += k + ") " + cart[i].title + " -- " + cart[i].price + "\n";
        k += 1;
    }
	//display cart
    var element = document.getElementById("parent");
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    }
    for (var i in cart) {
        var div = document.createElement("div");
        var price = document.createElement("div");
        var box = document.createElement("div");
        var bxtxt = document.createElement("div");
        var img = document.createElement("img");
        img.src = cart[i].image;
        img.classList.add("prd_item");
        div.classList.add("prd");
        price.classList.add("price");
        bxtxt.classList.add("box-text");
        box.classList.add("hover-box");
        var k = prd.appendChild(div);
        k.appendChild(img);
        var bx = k.appendChild(box);
        var bx_txt = bx.appendChild(bxtxt);
        var pr = k.appendChild(price);
        pr.innerHTML = "$" + cart[i].price;
        var title = cart[i].title.length > 20 ? cart[i].title.slice(0, 20) : cart[i].title;
        bx_txt.innerHTML = title;
    }
	detail_product = cart
}

function SortResults(type){
	if(type == "p"){
		products.sort(function(a, b) {
			return parseFloat(a.price) - parseFloat(b.price);
		});
		console.log(products.sort())
	}
	else{
		products.sort((a, b) => (a.title < b.title? -1 : a.title > b.title? 1 : 0))
		console.log(products.sort())
	}
	var element = document.getElementById("parent");
	while (element.firstChild) {
		element.removeChild(element.firstChild);
	}
	var element = document.getElementById("Main_heading");
	element.innerHTML = "Sorted Result"
	terminalOutput.innerHTML ="Sorted Result\n"
	no = 1
	for (var i in products) {
		filtered_products.push(products[i])
		terminalOutput.innerHTML += no + ") " + products[i].title + " -- " + products[i].price + "\n";
		no += 1;
		var div = document.createElement("div");
		var price = document.createElement("div");
		var box = document.createElement("div");
		var bxtxt = document.createElement("div");
		var img = document.createElement("img");
		img.src = products[i].image;
		img.classList.add("prd_item");
		div.classList.add("prd");
		price.classList.add("price");
		bxtxt.classList.add("box-text");
		box.classList.add("hover-box");
		var k = prd.appendChild(div);
		k.appendChild(img);
		var bx = k.appendChild(box);
		var bx_txt = bx.appendChild(bxtxt);
		var pr = k.appendChild(price);
		pr.innerHTML = "$" + products[i].price;
		var title = products[i].title.length > 20 ? products[i].title.slice(0, 20) : products[i].title;
			bx_txt.innerHTML = title;
		
	}
	detail_product = products
}


function ListProducts(filter = "") {
	var element = document.getElementById("Main_heading");
	element.innerHTML = "All Products"
	filtered_products =[]
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(json => {
            products = json;
            if (products.length > 0) {
                terminalOutput.innerHTML = "";
                terminalOutput.innerHTML += "All Products:\n";
            } else {
                terminalOutput.innerHTML = "";
                terminalOutput.innerHTML += "Failed to fetch products, please try again";
            }
            for (var i in products) {
				
                if (filter !== "") {
					var element = document.getElementById("Main_heading");
					element.innerHTML = "Search Results"
					//Search Title
					if (products[i].title.toLowerCase().includes(filter.toLowerCase())) {
						filtered_products.push(products[i]);
					}
						//Search in category
					else if (products[i].category.toLowerCase().includes(filter.toLowerCase())) {
						filtered_products.push(products[i]);
					}
                } 
				else {
                    filtered_products.push(products[i]);
                }
            }

			//display element
            var element = document.getElementById("parent");
            while (element.firstChild) {
                element.removeChild(element.firstChild);
            }

			var no = 1;
            for (var i in filtered_products) {
                terminalOutput.innerHTML += no + ") " + filtered_products[i].title + " -- " + filtered_products[i].price + "\n";
                no += 1;
                var div = document.createElement("div");
                var price = document.createElement("div");
                var box = document.createElement("div");
                var bxtxt = document.createElement("div");
                var img = document.createElement("img");
                img.src = filtered_products[i].image;
                img.classList.add("prd_item");
                div.classList.add("prd");
                price.classList.add("price");
                bxtxt.classList.add("box-text");
                box.classList.add("hover-box");
                var k = prd.appendChild(div);
                k.appendChild(img);
                var bx = k.appendChild(box);
                var bx_txt = bx.appendChild(bxtxt);
                var pr = k.appendChild(price);
                pr.innerHTML = "$" + filtered_products[i].price;
                var title = filtered_products[i].title.length > 20 ? filtered_products[i].title.slice(0, 20) : filtered_products[i].title;
                bx_txt.innerHTML = title;
            }
        });
	detail_product = filtered_products
}




function Main() {
	var element = document.getElementById("Main_heading");
	element.innerHTML = "All Products"
	sessionStorage.clear()

    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(json => {
            products = json;
            for (var i in products) {
                var div = document.createElement("div");
                var price = document.createElement("div");
                var box = document.createElement("div");
                var bxtxt = document.createElement("div");
                var img = document.createElement("img");
                img.src = products[i].image;
                img.classList.add("prd_item");
                div.classList.add("prd");
                price.classList.add("price");
                bxtxt.classList.add("box-text");
                box.classList.add("hover-box");
                var k = prd.appendChild(div);
                k.appendChild(img);
                var bx = k.appendChild(box);
                var bx_txt = bx.appendChild(bxtxt);
                var pr = k.appendChild(price);
                pr.innerHTML = "$" + products[i].price;
                var title = products[i].title.length > 20 ? products[i].title.slice(0, 20) : products[i].title;
                bx_txt.innerHTML = title;
            }
        });
}

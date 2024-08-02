/* 
    Vanilla JavaScript to get items from the API and load them 
    into the "front end" as cards.  
*/
let host = window.location.host;
let protocol = window.location.protocol; 
let dataEndpoint = protocol + '//' + host + "/api/items"

let cardContainer = document.getElementById("items-for-sale")
const cardTemplate = document.getElementById("item-card");

async function getItems() {
    fetch(dataEndpoint).then(resp => {
        if (resp.status === 200) {
            resp.json().then(data => {
                data.forEach(item => {
                    const cardClone = cardTemplate.content.cloneNode(true);
                    // Adding data to the card Clone
                    cardClone.querySelector(".card-header-title").textContent = item.item_name;
                    cardClone.querySelector(".content").textContent = item.description;
                    cardClone.querySelector(".price").textContent = item.price;
                    cardContainer.appendChild(cardClone);
                })
                console.log(data);
            })
        }
    })
}
getItems()
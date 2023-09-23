var updateBtns = document.getElementsByClassName('update-btn')
for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var radioButtons = document.querySelectorAll('input[type="radio"][name="optionsRadios"]');
        var size = null;

        radioButtons.forEach(function (radio) {
            if (radio.checked) {
                size = radio.value;
            }
        });
        console.log(productId);
        console.log('action: ', action);
        console.log('user: ', user)
        console.log('size: ', size)
        if (user === "AnonymousUser") {
            console.log("User not login");
        } else {
            updateUserOrder(productId, action,size);
        }
    })
}

function updateUserOrder(productId, action, size){
    console.log("User login ok");
    console.log("id: ", productId);
    console.log("action 2: ", action);
    var url = '/update_item/';
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action, 'size': size})
    }).then((reponse) =>{
       return reponse.json();
       
    }).then((data) =>{
        console.log('data: ', data)
        location.reload();
    })
}

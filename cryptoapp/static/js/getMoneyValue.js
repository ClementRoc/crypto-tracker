window.onload = () => {
    const moneySelect = document.getElementById('name')
    const moneyPrice = document.getElementById('price')
    const moneyQuantity = document.getElementById('quantity')
    moneySelect.addEventListener('change', function(e) {
        if (this.selectedIndex !== 0) {
            moneyPrice.value = this.children[this.selectedIndex].dataset.price
        } else if (this.selectedIndex === 0) {
            moneyPrice.value = "Prix d'achat"
        }
    })
        moneyQuantity.addEventListener('change', function(e) {
            if (this.selectedIndex !== 0 && moneyPrice.value !== 0) {
                moneyPrice.value = moneyQuantity.value * moneyPrice.value
            }
        })
}
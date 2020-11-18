var $ = function (id) {
    return document.getElementById(id);
}

function calculateCoins() {
    var userInput = $("cents").value;
    var quarters = Math.floor(userInput / 25);
    var remainder = userInput % 25;
    var dimes = Math.floor(remainder / 10);
    remainder = remainder % 10;
    var nickles = Math.floor(remainder / 5);
    remainder = remainder % 5;
    var pennies = remainder;

    $("quarters").value = quarters;
    $("dimes").value = dimes;
    $("nickels").value = nickles;
    $("pennies").value = pennies;

}


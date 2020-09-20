function calculateArea(myArea) {
    var area = 3.14 * (myArea * myArea);
    return area.toFixed(1);
}

var myRadius = parseFloat(prompt("Enter the radius in centimeters: "));
alert("The circle with a " + myRadius + " centimeter radius has an area of " + calculateArea(myRadius) + " square centimeters.");
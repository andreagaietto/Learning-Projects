var age = parseFloat(prompt("Please enter your age: "));

if (age < 21) {
    window.location = "http://www.disney.com";
} else {
    window.location = "http://www.espn.com";
}
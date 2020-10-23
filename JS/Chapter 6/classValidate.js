function result() {
    var TestVar = document.getElementById("data").value;
    var testRegEx = /[A-Z]{3}\.\d{3}#\d{4}_[a-z]{2}-\d{4}$/;

    if (testRegEx.test(TestVar)) {
        document.getElementById("feedback").innerHTML = "Correct Format";
    } else {
        document.getElementById("feedback").innerHTML = "Incorrect Format";
    }
}
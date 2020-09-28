var timeDay;
var toDisplay;
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

var date = new Date();
var currentDate = date.getDate();
var currentHour = date.getHours();
var currentMinute = date.getMinutes();
var currentDay = days[date.getDay()];
var currentMonth = months[date.getMonth()];

if (currentHour < 12) {
    timeDay = "AM";
} else if (currentHour >= 12) {
    timeDay = "PM"
    if (currentHour > 12) {
        currentHour -= 12;
    }
}
if (currentHour == 0) {
    currentHour = 12;
} 
if (currentMinute < 10) {
    currentMinute = "0" + currentMinute;
}

toDisplay = ("It is currently: " + currentHour + ":" + currentMinute + " " + timeDay + " on " + currentDay + ", " + currentMonth + " " + currentDate + ".");
document.write(toDisplay.bold().italics());


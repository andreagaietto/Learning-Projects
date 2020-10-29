var hours = 0;
var minutes = 0;
var seconds = 0;
var secondsString;
var minutesString;
var hoursString;
var timer;
var isRunning = false;



function incrementTime() {
    if (seconds <= 59) {
        seconds += 1;
    } 
    if (seconds == 60) {
        seconds = 0;
        minutes += 1;
    } 
    if (minutes == 60) {
        minutes = 0;
        hours += 1;
    }
    displayTime();
}

function startTimer() {
    if (!isRunning) {
        timer = setInterval(incrementTime, 1000);
        isRunning = true;
    } 
}

function pauseTimer() {
    clearInterval(timer);
    isRunning = false;
}

function resetTimer() {
    clearInterval(timer);
    isRunning = false;
    hours = 0;
    minutes = 0;
    seconds = 0;
    displayTime();
}

function displayTime() {
    if (seconds < 10) {
        secondsString = "0" + seconds;    
    } else {
        secondsString = seconds;
    } 
    if (minutes < 10) {
        minutesString = "0" + minutes;
    } else {
        minutesString = minutes;
    }
    if (hours < 10) {
        hoursString = "0" + hours;
    } else {
        hoursString = hours;
    }
    document.getElementById("timer").innerHTML = hoursString + ":" + minutesString + ":" + secondsString;
}
function getBrowserName() {
    var browserCheck = navigator.userAgent;
    

    if (browserCheck.indexOf("Trident") >= 0) {
        return "Internet Explorer";
    } else if (browserCheck.indexOf("Firefox") >= 0) {
        return "Firefox";
    } else if (browserCheck.indexOf("Chrome") >= 0) {
        return "Chrome";
    } else if (browserCheck.indexOf("Safari") >= 0) {
        return "Safari";
    } else if (browserCheck.indexOf("Opera") >= 0) {
        return "Opera";
    } else {
        return "Unknown";
    }
}

function getVersion() {
    var ua = navigator.userAgent;
    var browser = getBrowserName();
    if (browser != "Internet Explorer") {
        var findIndex = ua.indexOf(browser) + browser.length + 1;
        var browserVersion = parseFloat(ua.substring(findIndex, findIndex + 3));
    } else {
        var findIndex = ua.indexOf("rv:");
        var browserVersion = parseFloat(ua.substring(findIndex + 3, findIndex + 5));
    }

    return browserVersion;
}

var browserName = getBrowserName();
var browserVersion = getVersion();
var height = screen.availHeight;
var width = screen.availWidth;

document.write("You are using version " + browserVersion + " of the " + browserName + " browser to view this page in a browser whose inner window that is " + width + " pixels wide and " + height + " pixels tall.")
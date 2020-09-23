var nowDate = new Date();
var currentMonth = nowDate.getMonth();
nowDate.setMonth(currentMonth + 12);
document.write(nowDate)
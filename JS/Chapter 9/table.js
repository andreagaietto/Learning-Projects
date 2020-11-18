var tableInfo = [["Car", "Top Speed", "Price"], ["Chevrolet", "120mph", "$10,000"], ["Pontiac", "140mph", "$20,000"]];
var createTable = document.createElement("table");
document.body.appendChild(createTable);
createTable.style.color = "red"; //style object being used to style text red
createTable.style.fontWeight = "bold";//style object being used to add bold font weight
createTable.setAttribute("border", "1"); //setAttribute used to create 1 px border
createTable.setAttribute("bgColor", "gray");//setAttribute() method being used to create gray background
for (outerLoop = 0; outerLoop < 3; outerLoop++) {
    var makeRow = document.createElement("tr");
    document.getElementsByTagName("tr").setAttribute
    createTable.appendChild(makeRow);
    for (innerLoop = 0; innerLoop < 3; innerLoop++) {
        var makeCell = document.createElement("td");
        newText = document.createTextNode(tableInfo[outerLoop][innerLoop]);
        makeCell.appendChild(newText);
        makeRow.appendChild(makeCell);
    }
}

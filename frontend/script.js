let url = "http://localhost:8081/attendances";
let headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  mode: 'no-cors'
};

window.onload = async () => {
  const res = await fetch(url);
  const data = await res.json();

  let table = document.getElementById('attendances');

  data.forEach(row => {
    let newRow = table.insertRow();

    let newCell = newRow.insertCell();
    let nameTextNode = document.createTextNode(row['name']);
    newCell.appendChild(nameTextNode);

    let datetime = row['date'];
    let date = datetime.split('T')[0]
    let time = datetime.split('T')[1].split('.')[0]
    
    newCell = newRow.insertCell();
    let dateTextNode = document.createTextNode(date);
    newCell.appendChild(dateTextNode);

    newCell = newRow.insertCell();
    let timeTextNode = document.createTextNode(time);
    newCell.appendChild(timeTextNode);
  });
}

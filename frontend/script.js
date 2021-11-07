let url = "http://localhost:8081/attendance";
let headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  mode: 'no-cors'
};

window.onload = async () => {
  const res = await fetch(url);
  const data = await res.json();

  const attendanceList = data['object'];

  let tableBody = document.getElementById('attendances').getElementsByTagName('tbody')[0];

  attendanceList.forEach(row => {
    let newRow = tableBody.insertRow();

    let name = capitalizeName(row['name'].toLowerCase());
    let datetime = row['datetime'];
    let date = datetime.split('T')[0];
    let time = datetime.split('T')[1].split('.')[0];

    let newCell = newRow.insertCell();
    let nameTextNode = document.createTextNode(name);
    newCell.appendChild(nameTextNode);

    newCell = newRow.insertCell();
    let dateTextNode = document.createTextNode(date);
    newCell.appendChild(dateTextNode);

    newCell = newRow.insertCell();
    let timeTextNode = document.createTextNode(time);
    newCell.appendChild(timeTextNode);
  });

  $('#attendances').DataTable();
};

function capitalizeName(name) {
  const nameArr = name.split(' ');

  for (var i = 0; i < nameArr.length; i++) {
    nameArr[i] = nameArr[i].charAt(0).toUpperCase() + nameArr[i].slice(1);
  }

  const capitalizedName = nameArr.join(' ');

  return capitalizedName;
};

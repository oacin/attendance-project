let url = "http://localhost:8081/attendances";
let headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  mode: 'no-cors'
};

let attendanceList = [];

function load() {
  fetch(url)
  .then(res => res.json())
  .then(res => attendanceList = res);
};

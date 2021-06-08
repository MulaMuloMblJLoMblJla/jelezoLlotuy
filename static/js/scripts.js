function ajaxSend(url, params) {
  fetch(`${url}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: params
  })
      .then(response => response.json())
      .then(json => render(json))
      .catch(error => console.log(error))
}

const form = document.getElementById('reviewForm');

form.addEventListener('submit', function (e) {
  e.preventDefault();
  let url = this.action;
  let params = new URLSearchParams(new FormData(this)).toString();
  ajaxSend(url, params);
});


function render(data) {
  let template = Handlebars.compile(html);
  console.log(data)
  let output = template(data);
  const div = document.getElementById('request');
  div.innerHTML = output;
}


let html = '\
<li class="sub-title">\
        Request status\
      </li>\
{{#each reviews}}\
    <li class="sub-li">\
        {{name}}\
    </li>\
{{/each}}'
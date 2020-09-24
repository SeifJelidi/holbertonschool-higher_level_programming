$.get('https://swapi-api.hbtn.io/api/people/5/?format=json',
  function (d, textStatus) {
    $('DIV#character').text(d.name);
  });

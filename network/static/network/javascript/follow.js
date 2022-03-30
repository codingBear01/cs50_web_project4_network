follow_btn = document.querySelector('#follow_btn');

follow_btn.addEventListener('click', (e) => {
  user = follow_btn.getAttribute('data-user').trim();
  action = follow_btn.innerText.trim();

  console.log(action);
  console.log(user);

  form = new FormData();
  form.append('user', user);
  form.append('action', action);

  fetch('/follow', {
    method: 'POST',
    body: form,
  })
    .then((res) => res.json())
    .then((res) => console.log(res));
});

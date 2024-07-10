// script.js

const form = document.getElementById('form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const food = document.getElementById('food').value;

  fetch('/api/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, food }),
  })
   .then((response) => response.json())
   .then((data) => {
      resultDiv.textContent = `Thank you, ${data.name}! Your order for ${data.food} has been received. We will send a confirmation email to ${data.email}.`;
    })
   .catch((error) => {
      console.error(error);
    });
});
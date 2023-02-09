const text = document.getElementById('text');
let count = 0;
// Funciona
text.addEventListener('click', function () {
  count++;
  this.innerHTML = String(count);
});
// NÃO funciona
text.addEventListener('click', () => {
  count++;
  this.innerHTML = String(count);
});

const start = () => {
  const submitButton = document.getElementById('button');

  submitButton.addEventListener('click', e => {
    e.preventDefault();

    const EMAIL_REGEX =
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    const validaEmail = email => EMAIL_REGEX.test(email);

    const message = document.getElementById('mensagem');
    const email = document.getElementById('email');
    const name = document.getElementById('nome');

    if (!message.value) {
      message.classList.remove('is-valid');
      message.classList.add('is-invalid');
    } else {
      message.classList.add('is-valid');
      message.classList.remove('is-invalid');
    }

    if (!validaEmail(email.value)) {
      email.classList.remove('is-valid');
      email.classList.add('is-invalid');
    } else {
      email.classList.add('is-valid');
      email.classList.remove('is-invalid');
    }

    if (!name.value) {
      name.classList.remove('is-valid');
      name.classList.add('is-invalid');
    } else {
      name.classList.add('is-valid');
      name.classList.remove('is-invalid');
    }
  });
};

start();

function validateEmail(email) {
  let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}

function validatePassword(password) {
  var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;
  return re.test(password);
}

function checkPassword(password) {
  let res = "Your password must have:\n";
  let valid = true;
  
  if (/^[^\d+\n]+$/.test(password)) {
    res += "-digit\n";
    valid = false;
  }

  if (password.toUpperCase() == password) {
    res += "-lower letters\n";
    valid = false;
  }

  if (password.toLowerCase() == password) {
    res += "-upper letters\n";
    valid = false;
  }

  if (password.length < 8) {
    res += "-len from 8\n";
    valid = false;
  }
  
  if (valid) { 
    return "False";
  }
  
  return res;
}

window.addEventListener("load", function() {
  let form = document.querySelector('.autoriz-form'),
    inputEmail = document.querySelector('.js-input-email'),
    inputPassword = document.querySelector('.js-input-password');

  //добавил слушателя на окно, потому что код js выполняется быстрее, чем создается форма, если не добавить, форма пустая окажется и он ее не найдет

  form.onsubmit = function() {
    formInputs = document.querySelectorAll('.js-input');
    let emailVal = inputEmail.value,
      passwordVal = inputPassword.value,
      emptyInputs = Array.from(formInputs).filter(input => input.value === '');

    formInputs.forEach(function(input) {
      if (input.value === '') {
        input.classList.add('error');

      } else {
        input.classList.remove('error');
      }
    });

    if (emptyInputs.length !== 0) {
      console.log('inputs not filled');
      return false;
    }
    
    if ((!validateEmail(emailVal)) || (!validatePassword(passwordVal))) {
      if (!validateEmail(emailVal)) {
        console.log('email not valid');
        inputEmail.classList.add('error');
      } else {
        inputEmail.classList.remove('error');
      }
      
      if (!validatePassword(passwordVal)) {
        console.log(!validatePassword(passwordVal));
        console.log("Ваш пароль недостаточно сложный");
        console.log(checkPassword(passwordVal));
        inputPassword.classList.add('error');
      } else {
        inputPassword.classList.remove('error');
      }
      return false;
    }
  }
});

window.addEventListener("load", function() {
  let form = document.querySelector('.form-feedback'),
    inputFeedback = document.querySelector('.js-input-feedback');

  //добавил слушателя на окно, потому что код js выполняется быстрее, чем создается форма, если не добавить, форма пустая окажется и он ее не найдет

  form.onsubmit = function() {
    formInputs = document.querySelectorAll('.js-input');
    let feedbackVal = inputFeedback.value;
      emptyInputs = Array.from(formInputs).filter(input => input.value === '');

    console.log(feedbackVal);
      
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

    API_link = "https://api.telegram.org/bot6257874849:AAEyYu-eWxtSToscCpFiDvlLm9aHHUxmJGI";
    admin_id = "519665581";
    let xhr = new XMLHttpRequest();
    xhr.open('GET', API_link + "/sendMessage?chat_id=" + admin_id + "&text=" + feedbackVal);
    xhr.send();
  }
});
    

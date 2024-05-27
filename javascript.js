const questions = document.querySelectorAll('question-answer');

questions.forEach(function(question) {
  const bth = question.querySelectorAll('question-btn');
  console.log(btn);
  btn.addEventListener("click", function() {
    questons.forEach(function(item) {
      if (item !== question) {
        item.classList.remove("show-text");
        
        
      
      question.classList.toggle("show-text");

}

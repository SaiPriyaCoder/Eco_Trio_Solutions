document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll('.faq-question');
    const answers = document.querySelectorAll('.faq-answer');

    questions.forEach(q => {
      q.addEventListener('click', () => {
        const index = q.getAttribute('data-answer');

        // Remove active class from all
        questions.forEach(q => q.classList.remove('active'));
        answers.forEach(a => a.classList.remove('active'));

        // Add to current
        q.classList.add('active');
        document.getElementById('answer-' + index).classList.add('active');
      });
    });
  });

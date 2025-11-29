document.addEventListener("DOMContentLoaded", () => {
  const questions = document.querySelectorAll(".question");
  const nextBtn = document.getElementById("nextBtn");
  const prevBtn = document.getElementById("prevBtn");
  const indexSpan = document.getElementById("currentIndex");

  let current = 0;

  questions[current].style.display = "block";
  updateUI();

  function updateUI() {
      indexSpan.textContent = current + 1;
      prevBtn.disabled = current === 0;
      nextBtn.textContent =
          current === questions.length - 1 ? "Submit Test" : "Next";
  }

  nextBtn.onclick = () => {
      const checked = questions[current].querySelector(
          "input[type='radio']:checked"
      );

      if (!checked) {
          alert("Please select an answer before continuing.");
          return;
      }

      if (current === questions.length - 1) {
          calculateScore();
          return;
      }

      questions[current].style.display = "none";
      current++;
      questions[current].style.display = "block";
      updateUI();
  };

  prevBtn.onclick = () => {
      questions[current].style.display = "none";
      current--;
      questions[current].style.display = "block";
      updateUI();
  };

  function calculateScore() {
      let score = 0;

      for (let i = 1; i <= questions.length; i++) {
          const selected = document.querySelector(
              `input[name="q${i}"]:checked`
          );
          const correct = document.querySelector(
              `input[name="correct${i}"]`
          ).value;

          if (selected && selected.value === correct) score++;
      }

      document.getElementById("scoreField").value = score;
      document.getElementById("testForm").submit();
  }
});

document.addEventListener("DOMContentLoaded", function() {
  const roleField = document.getElementById("id_role");
  const examinerField = document.getElementById("div_id_examiner_id");

  if (!roleField) return console.error("Role field not found");
  if (!examinerField) return console.error("Examiner field not found");

  function toggleExaminerID() {
      if (roleField.value.toLowerCase() === "examiner") {
          examinerField.style.display = "block";
      } else {
          examinerField.style.display = "none";
      }
  }

  toggleExaminerID();
  roleField.addEventListener("change", toggleExaminerID);
});

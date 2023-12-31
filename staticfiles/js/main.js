/*jshint esversion: 6 */
checkboxes = document.querySelectorAll('input[type="checkbox"]');
checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", (e) => {
    const [id, dayOfWeek] = checkbox.id.split('-');
    const csrfToken = getCookie("csrftoken");
    fetch(`/tick`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({
        id: id,
        dayOfWeek: dayOfWeek,
      }),
    })
      .then((res) => {
        if (!res.ok) {
          throw Error(res.status);
        }
      })
      .catch((err) => console.error(err));
  });
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}


document.getElementById("clear").onclick = function () {
  const csrfToken = getCookie("csrftoken");
  fetch(`/clear`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
  })
    .then((res) => {
      if (!res.ok) {
        throw Error(res.status);
      }
    })
    .catch((err) => console.error(err));
};

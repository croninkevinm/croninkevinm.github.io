function updateCopyrightDate(id) {
  const year = new Date().getFullYear();
  document.getElementById(id).textContent = year;
  console.log(`Updated copyright year to ${year}`);
}

updateCopyrightDate('copyrightyear');

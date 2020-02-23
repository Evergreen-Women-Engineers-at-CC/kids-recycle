funcion drag(ev) {
  ev.preventDefault();
  ev.dataTransfer.setData("text", ev.target.id);
  ev.target.appendChild(document.getElementById(data));
}

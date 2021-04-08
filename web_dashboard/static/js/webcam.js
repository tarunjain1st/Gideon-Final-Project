  var checkBox = document.getElementById("cam-check");
  var img = document.createElement("img");
  var src = document.getElementById("cam");
  var msg = document.getElementById("msg");

  if (checkBox.checked == false) {
    src.style.display = "none";
    msg.style.display = "block";
  }

  function togle() {
    if (checkBox.checked == true) {
      src.style.display = "block";
      msg.style.display = "none";
    } else {
      src.style.display = "none";
      msg.style.display = "block";
    }
  }

  img.src = "/webcam";
  img.width = 350;
  img.height = 280;
  src.appendChild(img);

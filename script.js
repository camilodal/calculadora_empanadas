function calcularDeuda() {
    var cantidadEmpanadas = document.getElementById("cantidadEmpanadas").value;
    var resultado = cantidadEmpanadas * 888 + 428;
    document.getElementById("resultado").innerText = "Le debes $" + resultado + " a Santi";
  }
  
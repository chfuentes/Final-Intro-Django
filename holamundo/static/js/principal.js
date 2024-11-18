function mensaje(texto) {
    Swal.fire({
        position: "center",
        icon: "success",
        title: texto,
        showConfirmButton: false,
        timer: 1500
      });
}
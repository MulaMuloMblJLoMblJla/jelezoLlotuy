function f() {
  const elements = document.getElementsByClassName("title1-div1")
  for (let i = 0; i < elements.length; i++) {
    let el = elements[i]
    el.addEventListener('mousemove', function (e) {
      console.log(this)
      this.style.backgroundColor = "#3a7280"
    })
    el.addEventListener('mouseleave', function (e) {
      this.style.backgroundColor = "#5fbfd4"
    })
  }
}

f()
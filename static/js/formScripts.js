function addArticleOpen() {
  // const articleContentIds = ["content1", "content2", "content3"]
  const articleTitles = document.getElementsByClassName('article')
  const articleText = document.getElementsByClassName('article-text')
  for (let i = 0; i < articleText.length; i++) {
    articleTitles[i].addEventListener('click', function () {
      console.log(articleText[i].style.display)
      if (articleText[i].style.display === 'none' || articleText[i].style.display === '') {
        articleText[i].style.display = 'block'
      } else {
        articleText[i].style.display = 'none'
        articleTitles[i].style.backgroundColor = '#cad0d7'
      }
    })
  }
}

addArticleOpen()
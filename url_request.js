const https = require('https');

const url = (title, pageNum = 1) => 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + title + "&page=" + pageNum

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get((url), res => {
      res.on('data', function(body) {
        let data = JSON.parse(body);
        resolve(data);
      })
    })
  })
}

function convertToString (arr) {
    return console.log(arr.sort().join('\n'))
}

function getMovieTitles(title) {
  return fetchUrl(url(title, 1))
  .then((data) => {
    titleArray = []
    data.data.forEach((movie) => {
      titleArray.push(movie.Title)
    })
    totalPage = data.total_pages;
    let promises = []

    for (let page = 2; page <= totalPage; page++) {
      promises.push(fetchUrl(url(title, page)))
    }
    return {promises: promises,
      titleArray: titleArray}

  })
  .then((data) => {
    titleArray =  data.titleArray
    Promise.all(data.promises)
    .then((datas) => {
      datas.forEach((data) => {
        data.data.forEach((movie) => {
          titleArray.push(movie.Title)
        })
      })
      return titleArray
    }).then((titleArray) => {
      return convertToString(titleArray)
    })
  })
}


getMovieTitles('spiderman')




$(document).ready(function () {
    $.ajax({
      url: "https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=158cdc736b1e483cae554052bc307b8b",
      success: function (results) {
        console.log(results);
      },
    });
  });

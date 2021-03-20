$("#yliko").change(function () {
var url = $("#post-form").attr("data-cities-url");  // get the url of the `load_cities` view
var ylikoId = $(this).val();
  // get the selected country ID from the HTML input

// console.log($(this).val());
console.log(ylikoId);
console.log("Changes!");



$.ajax({                       // initialize an AJAX request
  url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
  data: {
    'ergo': ylikoId       // add the country id to the GET parameters
  },
  traditional: true,
  success: function (data) {   // `data` is the return of the `load_cities` view function
    $("#trial").html(data);  // replace the contents of the city input with the data that came from the server
  }
});

});

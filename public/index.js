"use strict";

$(document).ready(function() {

  var ingredient
  var cookingList = []
  var str
  var ingredientsList

  $.get('/ingredients', function(data) {
    ingredientsList = data.ingredients;
    $('#single-ingredient').autocomplete({
      source: ingredientsList
    });
  })

  $('#add-button').click(function() {
    ingredient = $('#single-ingredient').val()
    $('#single-ingredient').val('')
    cookingList.push(ingredient)
    $('#cooking-list').append(`<li>${ingredient}</li>`)
  })

  $('#cook-button').click(function() {
    $.post('/', { id: 1, cuisine: "", ingredients: cookingList }, function() {
      $.get('/prediction', function(data) {
        $('#prediction-div').append(`<p id="prediction">${data.prediction}</p>`)
      })
    })
  })

})

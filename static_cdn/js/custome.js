$(document).ready(function()
{$('select').formSelect();
$('input[type=checkbox]').each(function() {
        if(this.nextSibling.nodeName != 'label') {
          $(this).after('<label for="'+this.id+'"></label>')
        }
      })
});
$(document).ready(function() {
  $('input[type=checkbox]').each(function() {
    if(this.nextSibling.nodeName != 'label') {
      $(this).after('<label for="'+this.id+'"></label>')
    }
  })
})

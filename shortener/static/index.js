$(document).on('submit','#post-form',function(e){
    e.preventDefault();
    if($('#link').val().trim() == ''){
      toastr.error("Enter Url!")
      return;
    }
    $.ajax({
      type:'POST',
      url:'/create',
      data:{
        link:$('#link').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data){
        $('h2').html("localhost:8000/"+data)
      }
    });
  });
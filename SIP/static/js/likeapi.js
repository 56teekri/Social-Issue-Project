$(document).ready(function(){

    function getCookie(name) {
        var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g,
          '\\$1') + "=([^;]*)"));
        return matches ? decodeURIComponent(matches[1]) : undefined;
      }
      const csrftoken = getCookie("csrftoken")
      function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      }
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        },
        // xhrFields: { withCredentials:true }
        // crossdomain: true,
      });

    
    //click event for like functionality
    $(".like-icon").click(function (e){
        const el=$(e.currentTarget)
        //console.log(elm)
        //console.log($(el).html())
        //console.log(el.data("id"))
        $.post(
            {
            url:"likeAPI",
            mydata:{
                "issue_id":el.data("id")
            },
            success:function(data,textStatus,jqXHR){
                if(textStatus=="success"){
                    const count=$(el).find(".like_count")
                    let incCounter=parseInt(count.text())
                    incCounter=incCounter+1
                    count.text(incCounter)
                }
            },
            error:function(err){
                let error=JSON.parse(err.responseText)
                if(error.hasOwnProperty("message")){
                    console.log(err)
                    const count=$(el).find(".like_count")
                    count.text(error["message"])
                }
            },
        });
    });
});
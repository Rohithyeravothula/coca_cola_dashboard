console.log("hello");

function sendSms() {
    customerName = $("[name=name]").val();
    phoneNumber = $("[name=number]").val();
    data = {"name": customerName,
            "number": phoneNumber};
    $.ajax({
          type: "POST",
          url: "/coca/sendsms",
          // headers: {'X-CSRFToken': $("[name=csrfmiddlewaretoken]").val()},
          data: data,
        });
}

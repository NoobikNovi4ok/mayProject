//(function ($) {
//  "use strict";
//  $(".input100").each(function () {
//    $(this).on("blur", function () {
//      if ($(this).val().trim() !== "") {
//        $(this).addClass("has-val");
//      } else {
//        $(this).removeClass("has-val");
//      }
//    });
//  });
//  let showPass = 0;
//  $(".btn-show-pass").on("click", function () {
//    if (showPass == 0) {
//      $(this).next("input").attr("type", "text");
//      $(this).find("i").removeClass("fa fa-eye-slash");
//      $(this).find("i").addClass("fa fa-eye");
//      showPass = 1;
//    } else {
//      $(this).next("input").attr("type", "password");
//      $(this).find("i").removeClass("fa fa-eye");
//      $(this).find("i").addClass("fa fa-eye-slash");
//
//      showPass = 0;
//    }
//  });
//})(jQuery);
$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "Type the correct answer, please.");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 8
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "Your name, please?",
                    minlength: "your name must consist of at least 2 characters"
                },
                subject: {
                    required: "Please write what the content is about.",
                    minlength: "your subject must consist of at least 4 characters"
                },
                number: {
                    required: "come on, you have a number, don't you?",
                    minlength: "Your mumber must contain at least 8 characters"
                },
                email: {
                    required: "Your email is needed to get response."
                },
                message: {
                    required: "Please fill in your message.",
                    minlength: "It is too short to be sent."
                }
            },
        })
    })
        
 })(jQuery)
})
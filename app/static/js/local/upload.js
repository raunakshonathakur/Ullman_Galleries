
$(window).on('load',function(){
    $('#uploadModal').modal('show');
})

function closeModal(){
    $('#uploadModal').modal('hide');
}

DropZone
Dropzone.options.drop = {
    paramname: 'file', //The name that will be used to transfer the file
    acceptedFiles: ".doc,docx,.pdf,.txt,.zip",
    dictDefaultMessage: "Upload additional files here.",
    addRemoveLinks: true,
    clickable: true,
    init: function(){
        var submitButton = document.querySelector('#submit')
        drop = this;
        
        submitButton.addEventListener('click',function(){
            drop.processQueue();
        });
    }
}


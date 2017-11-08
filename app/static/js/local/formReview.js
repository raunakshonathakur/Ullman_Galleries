function redirectNote(SNID, FID){
    console.log('in js')
    var url = "/deleteNote/" + SNID + "/" + FID;
    window.location.replace(url)
}

function editNote(SNID, FID){
    var x = document.getElementById('changedNote') //get element 
    notes = x.value; // get value
    var note = { new_note : notes }; //create dictionary 
    var the_url = "/editNote/" + SNID; //create url
    $.ajax({
        type: "POST",
        data: JSON.stringify(note),
        url: the_url,
        contentType: 'application/json'
    }).done(function (data)
    {
        window.location.replace('/form/summary/' + FID)   
    })
}
$(function () {
  $('[data-toggle="popover"]').popover()
})

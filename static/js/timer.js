function timer(){
    $('#timer-outer').css('display','block');
    $('#timer').css('width','100%');
    var i = 100;
    var counterBack = setInterval(function () {
    i--;
    if (i > 0) {
        $('#timer').css('width', i + '%');
    } else {
        clearInterval(counterBack);
    }
    }, 50);
    /* setTimeout(function(){
        $('#timer').css('width','75%');
    }, 500);
    setTimeout(function(){
        $('#timer').css('width','50%');
    }, 1000);
    setTimeout(function(){
        $('#timer').css('width','25%');
    }, 1500);
    setTimeout(function(){
        $('#timer').css('width','0%');
    }, 2000); */
}
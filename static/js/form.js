$(document).ready(function(){
    $('#custom14button').click(function(){
            $('#ques15').fadeIn(800);
            $('#ques1').fadeOut();
    });
    /* var i;
    for(i=1; i<15; i++){
        $("#ques"+String(i)+"but").click(function(){
            //if( $('input[name=ques' + String(i) +']:checked').val() == undefined ){
            //    alert('It is necessary to answer every question.');
            //}
            //else{
                $("#ques"+String(i+1)).fadeIn(800);
                $("#ques"+String(i)).fadeOut();
            //}
        });
    } */
    $('#ques1but').click(function(){
        if( $('input[name="ques1"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            //$('#ques1').animate({
            //    opacity:0,
            //    marginLeft: '-100vw'
            //},'slow', 'linear', function(){
            //    $(this).remove();
            //});
            $('#noentrytext').css('display', 'none');
            $('#pbar').css('width','calc( (2/30)*100% )');
            $('#ques2').fadeIn(800);
            $('#ques1').fadeOut();
        }
    });
    $('#ques2but').click(function(){
        if( $('input[name="ques2"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (3/30)*100% )');
            $('#ques3').fadeIn(800);
            $('#ques2').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques3but').click(function(){
        if( $('input[name="ques3"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (4/30)*100% )');
            $('#ques4').fadeIn(800);
            $('#ques3').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques4but').click(function(){
        if( $('input[name="ques4"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (5/30)*100% )');
            $('#ques5').fadeIn(800);
            $('#ques4').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques5but').click(function(){
        if( $('input[name="ques5"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (6/30)*100% )');
            $('#ques6').fadeIn(800);
            $('#ques5').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques6but').click(function(){
        if( $('input[name="ques6"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (7/30)*100% )');
            $('#ques7').fadeIn(800);
            $('#ques6').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques7but').click(function(){
        if( $('input[name="ques7"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (8/30)*100% )');
            $('#ques8').fadeIn(800);
            $('#ques7').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques8but').click(function(){
        if( $('input[name="ques8"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (9/30)*100% )');
            $('#ques9').fadeIn(800);
            $('#ques8').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques9but').click(function(){
        if( $('input[name="ques9"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (10/30)*100% )');
            $('#ques10').fadeIn(800);
            $('#ques9').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    }); 
    $('#ques10but').click(function(){
        if( $('input[name="ques10"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (11/30)*100% )');
            $('#ques11').fadeIn(800);
            $('#ques10').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques11but').click(function(){
        if( $('input[name="ques11"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (12/30)*100% )');
            $('#ques12').fadeIn(800);
            $('#ques11').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques12but').click(function(){
        if( $('input[name="ques12"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (13/30)*100% )');
            $('#ques13').fadeIn(800);
            $('#ques12').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques13but').click(function(){
        if( $('input[name="ques13"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (14/30)*100% )');
            $('#ques14').fadeIn(800);
            $('#ques13').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques14but').click(function(){
        if( $('input[name="ques14"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#pbar').css('width','calc( (15/30)*100% )');
            $('#ques15').fadeIn(800);
            $('#ques14').fadeOut();
            $('#noentrytext').css('display', 'none');
        }
    });
    $('#ques15but').click(function(){
        if( $('input[name="ques15"]:checked').val() == undefined ){
            $('#noentrytext').css('display', 'block');
        }
        else{
            $('#noentrytext').css('display', 'none');
            $('#ques15').fadeOut();
            $('#ques16').fadeIn(800);
            $('#pbar').css('width','calc( (16/30)*100% )');
            timer();
            setTimeout(function(){
                $('#pbar').css('width','calc( (17/30)*100% )');
                $('#ques17').fadeIn(800);
                $('#ques16').fadeOut();
                timer();
            }, 5000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (18/30)*100% )');
                $('#ques18').fadeIn(800);
                $('#ques17').fadeOut();
                timer();
            }, 10000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (19/30)*100% )');
                $('#ques19').fadeIn(800);
                $('#ques18').fadeOut();
                timer();
            }, 15000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (20/30)*100% )');
                $('#ques20').fadeIn(800);
                $('#ques19').fadeOut();
                timer();
            }, 20000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (21/30)*100% )');
                $('#ques21').fadeIn(800);
                $('#ques20').fadeOut();
                timer();
            }, 25000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (22/30)*100% )');
                $('#ques22').fadeIn(800);
                $('#ques21').fadeOut();
                timer();
            }, 30000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (23/30)*100% )');
                $('#ques23').fadeIn(800);
                $('#ques22').fadeOut();
                timer();
            }, 35000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (24/30)*100% )');
                $('#ques24').fadeIn(800);
                $('#ques23').fadeOut();
                timer();
            }, 40000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (25/30)*100% )');
                $('#ques25').fadeIn(800);
                $('#ques24').fadeOut();
                timer();
            }, 45000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (26/30)*100% )');
                $('#ques26').fadeIn(800);
                $('#ques25').fadeOut();
                timer();
            }, 50000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (27/30)*100% )');
                $('#ques27').fadeIn(800);
                $('#ques26').fadeOut();
                timer();
            }, 55000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (28/30)*100% )');
                $('#ques28').fadeIn(800);
                $('#ques27').fadeOut();
                timer();
            }, 60000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (29/30)*100% )');
                $('#ques29').fadeIn(800);
                $('#ques28').fadeOut();
                timer();
            }, 65000);
            setTimeout(function(){
                $('#pbar').css('width','calc( (30/30)*100% )');
                $('#ques30').fadeIn(800);
                $('#ques29').fadeOut();
                timer();
            }, 70000);
        }
        /* if( $('input[name="ques15"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques16').fadeIn(800);
            $('#ques15').fadeOut();
        } */
    });
    
    /* $('#ques16but').click(function(){
        if( $('input[name="ques16"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques17').fadeIn(800);
            $('#ques16').fadeOut();
        }
    });
    $('#ques17but').click(function(){
        if( $('input[name="ques17"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques18').fadeIn(800);
            $('#ques17').fadeOut();
        }
    });
    $('#ques18but').click(function(){
        if( $('input[name="ques18"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques19').fadeIn(800);
            $('#ques18').fadeOut();
        }
    });
    $('#ques19but').click(function(){
        if( $('input[name="ques19"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques20').fadeIn(800);
            $('#ques19').fadeOut();
        }
    });
    $('#ques20but').click(function(){
        if( $('input[name="ques17"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques21').fadeIn(800);
            $('#ques20').fadeOut();
        }
    });
    $('#ques21but').click(function(){
        if( $('input[name="ques21"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques22').fadeIn(800);
            $('#ques21').fadeOut();
        }
    });    
    $('#ques22but').click(function(){
        if( $('input[name="ques22"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques23').fadeIn(800);
            $('#ques22').fadeOut();
        }
    });  
    $('#ques23but').click(function(){
        if( $('input[name="ques23"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
        }
        else{
            $('#ques24').fadeIn(800);
            $('#ques23').fadeOut();
        }
    });   */
    $('#ques2butprev').click(function(){
        $('#ques1').fadeIn(800);
        $('#ques2').fadeOut();
        $('#pbar').css('width','calc( (1/30)*100% )');
    });
    $('#ques3butprev').click(function(){
        $('#ques2').fadeIn(800);
        $('#ques3').fadeOut();
        $('#pbar').css('width','calc( (2/30)*100% )');
    });
    $('#ques4butprev').click(function(){
        $('#ques3').fadeIn(800);
        $('#ques4').fadeOut();
        $('#pbar').css('width','calc( (3/30)*100% )');
    });
    $('#ques5butprev').click(function(){
        $('#ques4').fadeIn(800);
        $('#ques5').fadeOut();
        $('#pbar').css('width','calc( (4/30)*100% )');
    });
    $('#ques6butprev').click(function(){
        $('#ques5').fadeIn(800);
        $('#ques6').fadeOut();
        $('#pbar').css('width','calc( (5/30)*100% )');
    });
    $('#ques7butprev').click(function(){
        $('#ques6').fadeIn(800);
        $('#ques7').fadeOut();
        $('#pbar').css('width','calc( (6/30)*100% )');
    });
    $('#ques8butprev').click(function(){
        $('#ques7').fadeIn(800);
        $('#ques8').fadeOut();
        $('#pbar').css('width','calc( (7/30)*100% )');
    });
    $('#ques9butprev').click(function(){
        $('#ques8').fadeIn(800);
        $('#ques9').fadeOut();
        $('#pbar').css('width','calc( (8/30)*100% )');
    });
    $('#ques10butprev').click(function(){
        $('#ques9').fadeIn(800);
        $('#ques10').fadeOut();
        $('#pbar').css('width','calc( (9/30)*100% )');
    });
    $('#ques11butprev').click(function(){
        $('#ques10').fadeIn(800);
        $('#ques11').fadeOut();
        $('#pbar').css('width','calc( (10/30)*100% )');
    });
    $('#ques12butprev').click(function(){
        $('#ques11').fadeIn(800);
        $('#ques12').fadeOut();
        $('#pbar').css('width','calc( (11/30)*100% )');
    });
    $('#ques13butprev').click(function(){
        $('#ques12').fadeIn(800);
        $('#ques13').fadeOut();
        $('#pbar').css('width','calc( (12/30)*100% )');
    });
    $('#ques14butprev').click(function(){
        $('#ques13').fadeIn(800);
        $('#ques14').fadeOut();
        $('#pbar').css('width','calc( (13/30)*100% )');
    });
    $('#ques15butprev').click(function(){
        $('#ques14').fadeIn(800);
        $('#ques15').fadeOut();
        $('#pbar').css('width','calc( (14/30)*100% )');
    });
    $('form').submit(function(){
        if( $('input[name="ques30"]:checked').val() == undefined ){
            alert('It is necessary to answer every question.');
            event.preventDefault();
        }
        else{
            return;
        }
    });
});
function draw_picture(){
    var str = window.location.href; //取得整个地址栏    
    var num = str.indexOf("?");//问号之前的位置
    var equal = str.indexOf("=");

    var loaction=str.substr(0,num);//问号之前的URL
    str = str.substr(equal+ 1);//问号之后的URL
    console.log(str);
    $.ajax({
        //url: 'http://10.226.25.50/stone/guard/get_info?type=test_0406',
        url: 'http://10.226.25.50/stone/guard/get_info?type='+str,
        type: "GET",
        async: true,
        dataType: 'jsonp',
        jsonp: "callbackparam",
        jsonpCallback: "mycallback",
        success: function(result) {
            console.log(result);
            $('#container_CTR').highcharts(result['chart']);
        },
        error: function() {
            $('#img_loading')[0].style.visibility='hidden';
            alert('fail');
        }
    });
}
</script>
<script type="text/javascript">
$(document).ready(function() {
    draw_picture();
});

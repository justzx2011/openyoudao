$(document).ready(function() {
    var pageObj=document.getElementById("turnPage");
    var begPage = pageObj.getAttribute("begPage"); //开始页码
    var displayPage = pageObj.getAttribute("displayPage"); //显示页码数
    var pageSize = pageObj.getAttribute("pageSize"); //每面显示记录数
    var totalPagesUrl=pageObj.getAttribute("totalPagesUrl"); //获取总页数的url
    var pageDataUrl=pageObj.getAttribute("pageDataUrl"); //获取相关页的数据数的url
    var pagesNum=0;//总页数

    //取得分页数据
    //pageSize:每页记录条数
    //currentPage:当前是第几页
    function getPaginateData(pSize, curPage) {
        var paras = "{pageSize:" + pSize + ",currentPage:" + curPage + "}";
        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: pageDataUrl+"?pageSize="+"&currentPage="+curPage,
            //data: paras,
            dataType: ' json',
            beforeSend: function() {
                $("#content>table>tbody").html("");
                $("#load_gif").attr('style', 'display:block');
            },
            success: function(json) {
                //alert("123");
                //alert(json);
                //var result=eval('(' + json + ')');
                //alert(result);
                showPaginateData(json);
                addHoverCss();
            },
            complete: function() {
                $("#load_gif").attr('style', 'display:none');
            },
            error: function(xhr) {
                alert('页出错\n\r' + xhr.responseText);
            }
        });
    }
    //取得总页数
    function getTotalPage(pSize) {
        var paras = "{pageSize:" + pSize + "}";
        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: totalPagesUrl,
            data: paras,
            dataType: 'json',
            beforeSend: function() {
                $("#load_gif").attr('style', 'display:block');
            },
            success: function(json) {
                var data = eval('(' + json.totalPages + ')');
                pagesNum=data;
                setPaginate();
            },
            complete: function() {
               $("#load_gif").attr('style', 'display:none');
            },
            error: function(xhr) {
                alert('页出错\n\r' + xhr.responseText);
            }
        });
    }
    //分页页码显示 setPaginate()
    function setPaginate() {
        $("#turnPage").paginate({
            count: pagesNum,//总页数
            start: begPage,//开始页
            display: displayPage,//显示页
            border					: true,
            border_color			: '#fff',
            text_color  			: '#fff',
            background_color    	: 'black',
            border_hover_color		: '#ccc',
            text_hover_color  		: '#000',
            background_hover_color	: '#fff',
            images		: false,
            mouse		: 'press',
            onChange: function(currentPage) {
                //取得分页数据
                  getPaginateData(pageSize, currentPage);
            }
        });
    }
    function addHoverCss() {
        jQuery("body tr").hover(function () {
            jQuery(this).addClass("hover");
        }, function () {
            jQuery(this).removeClass("hover");
        });
    }

    getTotalPage(pageSize);
    getPaginateData(pageSize, begPage);
});


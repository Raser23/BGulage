/**
 * Created by Сергей Нещадим on 24.04.2017.
 */
pageContent = null;
sideBar = null;
function onLoad()
{

    pageContent = $('#content');
    sideBar = $('#side_bar');

    scrWidth = $(document).width();
    contentWidth = 1200;
    pageContent.width( contentWidth );

    sideBar.width(contentWidth/6);

    pageContent.css('margin-left',(scrWidth -contentWidth)/2 +'px');

}
window.onload = onLoad;
$(window).resize(onLoad)

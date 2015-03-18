$(function(){
    var task_add = $(".task_add")
    var task_finish = $(".task_finish")
    var task_delete = $(".task_delete")
    task_add.on("click", function(){
        location.href = "/task/add_task";
    });

    $(".submit_task_add").on("click", function(){
            $.ajax({
                cache: true,
                type: "POST",
                url:"/task/add_task",
                data:$(".form_task_add").serialize(),// 你的formid
                async: false,
                error: function(request) {
                    alert("任务创建失败");
                },
                success: function(data) {
                   location.href = "/home";
                }
            });
    });

    $(".delete_task").on("click", function(){
        var task_id = $(this).attr("id");
            $.ajax({
                cache: true,
                type: "POST",
                url:"/task/del_task",
                data:{ "task_id": task_id },
                async: false,
                error: function(request) {
                    alert("任务删除失败");
                },
                success: function(data) {
                    // alert(data)
                   // location.href = "/home";
                }
            });
    });
});
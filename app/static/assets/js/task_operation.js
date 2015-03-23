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
        var task_id = $(this).closest("tr").find('.task_id').attr('id');
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
                    alert(data)
                   // location.href = "/home";
                }
            });
    });

    $(".submit_task_edit").on("click", function(){
        var task_id = $(this).attr("id");
            $.ajax({
                cache: true,
                type: "POST",
                url:"/task/edit_task/"+task_id,
                data:$(".form_task_edit").serialize(),// 你的formid
                async: false,
                error: function(request) {
                    alert("任务创建失败");
                },
                success: function(data) {
                   location.href = "/home";
                }
            });
    });

    $(".finish_task").on("click", function(){
        var task_id = $(this).closest("tr").find('.task_id').attr('id');
            $.ajax({
                cache: true,
                type: "GET",
                url:"/task/finish_task/"+task_id,
                async: false,
                error: function(request) {
                    alert("任务状态更新失败");
                },
                success: function(data) {
                    alert(data)
                   // location.href = "/home";
                }
            });
    });

    $(".edit_task").on("click", function(){
        var task_id = $(this).closest("tr").find('.task_id').attr('id');
        window.location = "/task/edit_task/"+task_id;
        return 1
    });

});

$(document).ready(function(){
    var rules = $('textarea[name=rules]');
    var source_id = $('select[name=source_id]');
    var source_url = $('input[name=source_url]');
    var preview_btn = $('#preview-rule');
    var preview_pane = $('#preview-pane table');

    // event handlers
    preview_btn.click(preview);

    // preview button handler
    function preview(e) {
        e.preventDefault();
        rule_data = {'source_id': source_id.val(),
                     'source_url': source_url.val(),
                     'rules': rules.val()}

        $.post('/admin/rule/build', rule_data, function(data){
            display_preview(data);
        })
    }

    // display entries in preview pane
    function display_preview(data){
        $.each(data.entries, function(index, value){
            preview_pane.append('<tr><td><a href='+ value[0] + '>' + value[1] + '</a>')
        })
    }
});

$(document).ready(function(){
    var rules = $('textarea[name=rules]');
    var source_id = $('select[name=source_id]');
    var source_url = $('input[name=source_url]');
    var preview_btn = $('#preview-rule');

    // event handlers
    preview_btn.click(preview);

    // functions
    function preview(e) {
        e.preventDefault();
        rule_data = {'source_id': source_id.val(),
                     'source_url': source_url.val(),
                     'rules': rules.val()}

        console.log(rule_data);
        $.post('/admin/rule/build', rule_data, function(data){
            display_preview(data);
        })
    }

    function display_preview(data){
        console.log(data)
    }
});

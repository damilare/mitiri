$(document).ready(function(){
    var rule = $('textarea[name=rule]');
    var source = $('select[name=source]');
    var source_url = $('input[name=source_url]');
    var preview_btn = $('#preview-rule');

    // event handlers
    preview_btn.click(preview);

    // functions
    function preview(e) {
        e.preventDefault();
        rule_data = {'source': source.val(),
                     'source_url': source_url.val(),
                     'rule': rule.val()}

        $.post('/admin/rule/build', function(data){
            display_preview(data);
        })
    }

    function display_preview(data){
        console.log(data)
    }
});

$(document).ready(function(){
    var rules = $('textarea[name=rules]');
    var source_id = $('select[name=source_id]');
    var source_url = $('input[name=source_url]');
    var preview_btn = $('#preview-rule');
    var save_btn = $('#save-rule');
    var notice_pane = $('span.notice');
    var preview_pane = $('#preview-pane table');

    // event handlers
    preview_btn.click(rule_builder);
    save_btn.click(rule_builder);


    // preview button handler
    function rule_builder(e) {
        e.preventDefault();
        rule_data = {'source_id': source_id.val(),
                     'source_url': source_url.val(),
                     'rules': rules.val()}

      // switch to appropriate endpoint
      if (e.target.id == 'preview-rule'){
           rule_endpoint = '/admin/rule/preview'
       } else if (e.target.id == 'save-rule'){
           rule_endpoint = '/admin/rule/save' 
       }
      
       $.post(rule_endpoint, rule_data, function(data){
            display_flag = rule_endpoint.match('/preview$')
            if (display_flag){
               console.log('catches preview')
               display_preview(data);
            } else {
               console.log('catches data')
               display_notice(data);
            }
        })
    }

    // display entries in preview pane
    function display_preview(data){
        $.each(data.entries, function(index, value){
            preview_pane.append('<tr><td><a href='+ value[0] + '>' + value[1] + '</a>')
        })
    }

    // displa notice
    function display_notice(data){
      notice_pane.append(data.message)
    }
});

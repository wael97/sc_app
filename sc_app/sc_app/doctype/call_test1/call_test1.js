// Copyright (c) 2024, wael and contributors
// For license information, please see license.txt

frappe.ui.form.on('call_test1', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('call_test1', {
    refresh: function(frm) {
    
      frm.add_custom_button(__('Get User Email Address'), function(){
      
      frappe.call({
          method: "sc_app.sc_app.doctype.call_test1.api-test1.get_token", 
          callback: function(r) {
          console.log(r)
       
          }
      });

      
        frappe.msgprint(frm.doc.full_name);
    }, __("Utilities"));
    
  }
});


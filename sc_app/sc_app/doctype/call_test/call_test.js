// Copyright (c) 2024, wael and contributors
// For license information, please see license.txt

frappe.ui.form.on('Call Test', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Call Test', {
    refresh: function(frm) {
    
      frm.add_custom_button(__('Get User Email Address'), function(){
      
      frappe.call({
          method: "sc_app.sc_app.doctype.Call Test.api-test.delete_item", 
          callback: function(r) {
          console.log(r)
       
          }
      });

      
        frappe.msgprint(frm.doc.full_name);
    }, __("Utilities"));
    
  }
});


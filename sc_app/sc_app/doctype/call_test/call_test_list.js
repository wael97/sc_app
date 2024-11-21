frappe.listview_settings['Call Test'].refresh = function(listview) {
    // add button in menu
	listview.page.add_menu_item(__("Menu"));
   // add button in action
	listview.page.add_action_item(__("Actions"));
};
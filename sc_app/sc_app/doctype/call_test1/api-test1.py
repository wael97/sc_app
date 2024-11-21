import frappe
import requests

FOUND_DATA = 99
NOT_FOUND = 9


@frappe.whitelist(allow_guest=True)

def get_all_items(group):
    
     
    items = frappe.db.sql(f"""SELECT item_name,item_code,item_group FROM `tabItem` WHERE item_group = '{group}';""",as_dict = True)
    
    


    if (items):
         status_code = FOUND_DATA
         body = items
    else :
          status_code = NOT_FOUND
          body = "لا يوجد بيانات"
    response = dict ( status_code = status_code ,
                     body = body 
                          )
    return response

@frappe.whitelist()
def add_items(code,name,group,uom):
    add_items = frappe.get_doc ({"doctype": "Item",
         "item_code" : code,
         "item_name" : name,                        
         "item_group" : group,
         "stock_uom" : uom                        
                                })
    add_items.insert()
    frappe.db.commit()
    return add_items

def add_new_note(name,group):
    title = f"{name} has been addded"
    content = f"{name}is in {group}"
    add_note = frappe.get_doc({"doctype":"note",
               "title" : title,
               "content" : content
      }) 
    add_note.insert()

@frappe.whitelist(allow_guest=True)
def delete_item():
    delete_item = frappe.db.sql ("""DELETE FROM`tabItem` WHERE item_name = 'قلم رصاص'""")
    frappe.db.commit()
    return "تم المسح بنجاح"
     
    

@frappe.whitelist(allow_guest=True)
def update_item():
    frappe.db.sql(f"""UPDATE `tabItem` SET item_name = 'UPDATED item in api'
    WHERE item_name = 'Power Caps'""")
    frappe.db.commit()
    return "تم التحديث"

@frappe.whitelist(allow_guest=True)
def get_token():
    

     url = "https://id.preprod.eta.gov.eg/connect/token"

     payload = 'grant_type=client_credentials&client_id=03d7859f-76e7-4464-84ac-c281d92ce103&client_secret=f3f3be9a-7eea-467d-8f0d-1eff57e96ea8&scope=InvoicingAPI'
     headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
                  '': ''
                 }

      response = requests.request("POST", url, headers=headers, data=payload)

      print(response.text)

      return "تم التحديث"
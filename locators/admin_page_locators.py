class AdminPageLocators:
    view_users_button_id = "menu_admin_viewAdminModule"
    add_user_button_id = "btnAdd"
    userRole_dropdown_id = "systemUser_userType"
    userRole_option_name_admin = "Admin"
    employeeName_textbox_id = "systemUser_employeeName_empName"
    error_notFoundEmployee_validation_error = "span.validation-error"
    new_username_textbox_id = "systemUser_userName"
    userStatus_dropdown_id = "systemUser_status"
    userStatus_option_disabled = "systemUser[status]"
    new_user_password_textbox_id = "systemUser_password"
    confirm_password_textbox_id = "systemUser_confirmPassword"
    save_newUser_button_id = "btnSave"
    customer_list_table = "resultTable"
    username_search_field_name = "searchSystemUser[userName]"
    username_search_button = "searchBtn"
    found_new_username = "qwerty2018"
    new_user_success_label_xpath = "//div[@class='message success fadable']"
    new_created_user = "//a[text()='%s']"
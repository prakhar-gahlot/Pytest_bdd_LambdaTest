class LoginPageLocator:

    # login page
    login_page_title_xpath = '/html/body/app-root/login/mat-card/mat-card-header/div/mat-card-title'
    user_name_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/input[1]'
    password_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/input[2]'
    login_xpath = '/html/body/app-root/login/mat-card/mat-card-content/button'
    login_error_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/span'
    role_reviewer_xpath = './/*[text()="Reviewer"]'
    select_role_id = 'mat-select-0'


    # switch company page
    search_company_id = 'mat-input-0'
    first_company_id = 'mat-option-1'
    select_company_xpath = '/html/body/app-root/login/mat-card/mat-card-content/button'

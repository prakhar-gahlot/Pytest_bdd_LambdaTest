class LoginPageLocator:

    # login page
    login_page_title_xpath = '/html/body/app-root/login/mat-card/mat-card-header/div/mat-card-title'
    user_name_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/input[1]'
    password_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/input[2]'
    login_xpath = '/html/body/app-root/login/mat-card/mat-card-content/button'
    login_error_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/span'
    role_reviewer_xpath = '/html/body/div[1]/div[2]/div/div/div/div[1]/mat-option'
    selected_reviewer_role_xpath = '/html/body/app-root/login/mat-card/mat-card-content/role-company-form/form/mat-select/div/div[1]/span/span'
    role_trainee_xpath = '/html/body/div[1]/div[2]/div/div/div/div[2]/mat-option/span'
    select_role_xpath = '/html/body/app-root/login/mat-card/mat-card-content/role-company-form/form/mat-select/div/div[1]/span'
    role_list_first_xpath = '/html/body/div[2]/div[2]/div/div/div/mat-option'
    # switch company page
    search_company_xpath = '/html/body/app-root/login/mat-card/mat-card-content/role-company-form/form/div/input'
    first_company_xpath = '/html/body/div[1]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[1]/span'
    second_company_xpath = '/html/body/div[1]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[2]/span'
    third_company_xpath = '/html/body/div[1]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[3]/span'
    fourth_company_xpath = '/html/body/div[1]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[4]/span'
    select_company_xpath = '/html/body/app-root/login/mat-card/mat-card-content/button'

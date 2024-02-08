class LoginPageLocator:

    # login page
    login_page_title_xpath = '/html/body/app-root/login/mat-card/mat-card-header/div/mat-card-title'
    user_name_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/input[1]'
    password_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/input[2]'
    login_xpath = '/html/body/app-root/login/mat-card/mat-card-content/button'
    login_error_xpath = '/html/body/app-root/login/mat-card/mat-card-content/login-form/form/span'
    role_reviewer_xpath = '//*[@id="mat-option-0"]/span'
    selected_reviewer_role_xpath = '/html/body/app-root/login/mat-card/mat-card-content/role-company-form/form/mat-select/div/div[1]/span/span'
    role_trainee_xpath = '//*[@id="mat-option-1"]/span'
    select_role_xpath = '/html/body/app-root/login/mat-card/mat-card-content/role-company-form/form/mat-select/div/div[1]/span'
    role_list_first_xpath = '/html/body/div[2]/div[2]/div/div/div/mat-option'
    # switch company page
    search_company_xpath = '/html/body/app-root/login/mat-card/mat-card-content/role-company-form/form/div/input'
    first_company_xpath = '/html/body/div[2]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[1]'
    second_company_xpath = '/html/body/div[2]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[2]'
    third_company_xpath = '/html/body/div[2]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[3]'
    fourth_company_xpath = '/html/body/div[2]/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option[4]'
    select_company_xpath = '/html/body/app-root/login/mat-card/mat-card-content/button'

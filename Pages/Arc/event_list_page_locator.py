class EventListPage:

    # top bar
    title_xpath = '/html/body/app-root/top-bar/div/p'
    reviewing_company_xpath = '/html/body/app-root/top-bar/div/div/p[1]/strong'
    company_name_xpath = '/html/body/app-root/top-bar/div/div/p[1]/strong'
    switch_company_xpath = '/html/body/app-root/top-bar/div/div/p[2]'
    give_feedback_xpath = '/html/body/app-root/top-bar/reviewer-home/div/give-feedback-button/div/button/span[1]'

    # switch company dialog
    search_company_switch_company_xpath = '/html/body/div[2]/div[2]/div/mat-dialog-container/company-switch' \
                                          '/mat-card/mat-card-content/role-company-form/form/div/input'
    first_company_xpath = '/html/body/div[2]/div[3]/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option'
    select_company_xpath = '/html/body/div[2]/div[2]/div/mat-dialog-container' \
                           '/company-switch/mat-card/mat-card-content/button[1]'

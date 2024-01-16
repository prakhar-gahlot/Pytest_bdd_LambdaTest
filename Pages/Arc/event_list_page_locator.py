class EventListPageLocator:

    # top bar
    title_xpath = '/html/body/app-root/top-bar/div/p'
    reviewing_company_xpath = '/html/body/app-root/top-bar/div/div/p[1]/strong'
    company_name_xpath = '/html/body/app-root/top-bar/div/div/p[1]/strong'
    switch_company_xpath = '/html/body/app-root/top-bar/div/div/p[2]'
    give_feedback_xpath = '/html/body/app-root/top-bar/reviewer-home/div/give-feedback-button/div/button/span[1]'
    training_mode_xpath = '/html/body/app-root/top-bar/div/div[2]'

    # switch company dialog
    search_company_switch_company_xpath = '/html/body/div[2]/div[2]/div/mat-dialog-container/company-switch' \
                                          '/mat-card/mat-card-content/role-company-form/form/div/input'
    first_company_xpath = '/html/body/div[2]/div[3]/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option'
    select_company_xpath = '/html/body/div[2]/div[2]/div/mat-dialog-container' \
                           '/company-switch/mat-card/mat-card-content/button[1]'

    # filter and tabs
    review_id_filter_xpath = '/html/body/app-root/top-bar/reviewer-home/filter-event-list/div/form/input'
    filter_button_xpath = '/html/body/app-root/top-bar/reviewer-home/filter-event-list/div/form/button[1]'
    clear_button_xpath = '/html/body/app-root/top-bar/reviewer-home/filter-event-list/div/form/button[2]'
    new_tab_xpath = '/html/body/app-root/top-bar/reviewer-home/div/div/div[1]'
    return_tab_xpath = '/html/body/app-root/top-bar/reviewer-home/div/div/div[2]'
    search_range_and_results_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/div/p'

    # event list titles
    review_id_title_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list' \
                            '/mat-table/mat-header-row/mat-header-cell[1]'
    event_id_title_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list' \
                           '/mat-table/mat-header-row/mat-header-cell[2]'
    creation_date_title_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list' \
                                '/mat-table/mat-header-row/mat-header-cell[3]'
    vehicle_name_title_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list' \
                               '/mat-table/mat-header-row/mat-header-cell[4]'
    serial_num_title_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list' \
                             '/mat-table/mat-header-row/mat-header-cell[5]'

    # event list first row if only one event returned
    review_id_1st_only_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row/mat-cell[1]/a'
    event_id_1st_only_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row/mat-cell[2]'
    creation_date_1st_only_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row/mat-cell[3]'
    vehicle_name_1st_only_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row/mat-cell[4]'
    serial_num_1st_only_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row/mat-cell[5]'

    # event list rows if multiple events returned
    review_id_1st_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row[1]/mat-cell[1]/a'
    event_id_1st_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row[1]/mat-cell[2]'
    creation_date_1st_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row[1]/mat-cell[3]'
    vehicle_name_1st_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row[1]/mat-cell[4]'
    serial_num_1st_xpath = '/html/body/app-root/top-bar/reviewer-home/event-list/mat-table/mat-row[1]/mat-cell[5]'

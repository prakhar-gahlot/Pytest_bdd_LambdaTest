class WSLibraryPageLocator:

    # WS Library navigation
    library_navigator_xpath = '/html/body/app/shell/div/div/navigation/div[1]/div[4]'
    events_xpath = '/html/body/app/shell/div/div/navigation/div[1]/div[4]/div[2]/div[2]/div[1]'
    select_search_id = 'event-list-search-criteria'
    select_search_event_id_xpath = '//*[@id="event-list-search-criteria"]/div/div/ul/li[1]'
    select_search_event_driver_xpath = '//*[@id="event-list-search-criteria"]/div/div/ul/li[2]'
    select_search_criteria_id = 'searchInput'
    search_driver_result_id = 'ngb-typeahead-0-0'
    search_icon_xpath = '//*[@id="eventId-search-criteria"]/div/span'
    event_status_1st_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                             '/div/div/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[8]/span[2]'
    event_trigger_1st_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                              '/div/div/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[9]/span[2]'
    event_behaviors_1st_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                '/div/div/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[10]/span[2]'

    # events page

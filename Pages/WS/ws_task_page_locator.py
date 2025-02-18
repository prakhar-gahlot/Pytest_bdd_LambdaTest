class WSTaskPageLocator:

    # WS Task navigation
    task_xpath = '/html/body/app/shell/div/div/navigation/div[1]/div[2]'
    due_for_coaching_xpath = '/html/body/app/shell/div/div/navigation/div[1]/div[2]/div[2]/div[2]/div[1]'

    # due for coaching page
    search_driver_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list/task-card-list' \
                          '/div/div[1]/filter-bar/div/div[2]/div[2]/lytx-search/div/form/input'
    coach_button_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list/task-card-list' \
                         '/div/div[3]/coaching-task-card/div/div[2]/div[2]/button'
    task_count_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list/task-card-list' \
                       '/div/div[1]/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'

    # coaching session page
    play_event_xpath = '/html/body/app/shell/div/div/div/coaching-session/lx-page-container' \
                       '/div/div[3]/div/div/event-player/div/video-player/div[2]/div[2]/div[2]/i'
    behavior_1st_xpath = '//*[@id="event-viewer-details__behaviors-content"]/div/lytx-pill[1]'
    behavior_2nd_xpath = '//*[@id="event-viewer-details__behaviors-content"]/div/lytx-pill[2]'
    behaviors_xpath = '//*[@id="event-viewer-details__behaviors-content"]/div'

    event_id_id = 'event-viewer-details__event'
    event_status_id = 'event-viewer-details__aggregated-status'
    event_trigger_id = 'event-viewer-details__trigger'
    event_score_id = 'event-viewer-details__event-score'

    complete_session_id = 'coaching-session-complete-button'
    confirm_complete_id = 'modalShellPrimaryButton'
    first_action_plan_id = 'lytx-radio-button__content'

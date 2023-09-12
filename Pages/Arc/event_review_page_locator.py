class EventReviewPageLocator:

    # top bar
    top_bar_title_class_name = 'top-bar-title'
    top_bar_review_text_class_name = 'top-bar-reviewer'
    top_bar_switch_company_class_name = 'top-bar-switch-companies'

    # video
    video_tag_name = 'video'

    # top info
    back_to_home_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                         '/mat-toolbar/mat-toolbar-row/div[1]'
    review_id_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                            '/mat-toolbar/mat-toolbar-row/div[2]/div[1]/span'
    review_id_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                      '/mat-toolbar/mat-toolbar-row/div[2]/div[1]/p'
    trigger_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                          '/mat-toolbar/mat-toolbar-row/div[2]/div[2]/span'
    trigger_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                    '/mat-toolbar/mat-toolbar-row/div[2]/div[2]/p'
    record_date_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                              '/mat-toolbar/mat-toolbar-row/div[2]/div[3]/span'
    record_date_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                        '/mat-toolbar/mat-toolbar-row/div[2]/div[3]/p'
    vehicle_id_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                             '/mat-toolbar/mat-toolbar-row/div[2]/div[4]/span'
    vehicle_id_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                       '/mat-toolbar/mat-toolbar-row/div[2]/div[4]/p'
    vehicle_type_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                               '/mat-toolbar/mat-toolbar-row/div[2]/div[5]/span'
    vehicle_type_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                         '/mat-toolbar/mat-toolbar-row/div[2]/div[5]/p'
    seatbelt_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                           '/mat-toolbar/mat-toolbar-row/div[2]/div[6]/span'
    seatbelt_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                     '/mat-toolbar/mat-toolbar-row/div[2]/div[6]/p'
    audio_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                        '/mat-toolbar/mat-toolbar-row/div[2]/div[7]/span'
    audio_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar/mat-toolbar' \
                  '/mat-toolbar-row/div[2]/div[7]/p'
    FPS_title_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                      '/mat-toolbar/mat-toolbar-row/div[2]/div[8]/span'
    FPS_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                '/mat-toolbar/mat-toolbar-row/div[2]/div[8]/p'

    event_details_icon_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                               '/mat-toolbar/mat-toolbar-row/div[3]/button'
    event_details_text_xpath = '/html/body/app-root/top-bar/app-review/div/div[1]/video-player-top-bar' \
                               '/mat-toolbar/mat-toolbar-row/div[3]/span'

    # event play
    rear_view_text_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[1]/div/label[1]'
    front_view_text_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[1]/div/label[2]'

    event_play_time_id = 'time-value'

    play_and_pause_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player' \
                           '/div[4]/div[2]/button[2]/span[1]/mat-icon'
    rear_and_front_class_name = 'rear-front-btn'
    rear_class_name = 'rear-btn'
    front_class_name = 'front-btn'
    full_screen_class_name = 'expand-btn'
    stop_watch_class_name = 'stopwatch-button'
    backward_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[4]/div[2]/button[1]'
    forward_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[4]/div[2]/button[3]'
    backward_1_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[4]/div[2]/button[4]'
    forward_1_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[4]/div[2]/button[5]'

    # telemetry bar
    telemetry_graph_tab_name = 'canvas'
    scrubber_id = 'scrubber'
    current_time_id = 'currentTime'
    fwd_id = 'fwd-value'
    lat_id = 'lat-value'
    time_id = 'time-value'
    gps_speed_id = 'gps-speed-value'
    fwd_force_graph_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[3]/div[3]/ul/li[1]'
    lat_force_graph_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[3]/div[3]/ul/li[2]'
    gps_speed_force_graph_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[3]/div[3]/ul/li[3]'
    time_force_graph_xpath = '/html/body/app-root/top-bar/app-review/div/div[2]/video-player/div[3]/div[3]/ul/li[4]'

    # event review tabs
    outcome_trigger_tab_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar' \
                                '/mat-tab-group/mat-tab-header/div/div/div/div[1]'
    behavior_tab_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar' \
                         '/mat-tab-group/mat-tab-header/div/div/div/div[2]'
    comments_tab_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar' \
                         '/mat-tab-group/mat-tab-header/div/div/div/div[3]'

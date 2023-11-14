class BehaviorsTabLocator:

    # comments and more behaviors button
    comments_class = 'btn-comments-less'
    more_behaviors_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                           '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[3]/div[1]/button'
    previous_behaviors_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                               '/div/mat-tab-body[2]/div/behaviors-review/div[2]/div[1]/div[1]/button'
    custom_behaviors_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group/div' \
                             '/mat-tab-body[2]/div/behaviors-review/div[2]/div[1]/div[4]/behavior-group/div/div[1]'

    # Distractions

    # Awareness
    blank_stare_checkbox_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                                 '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[1]/div[2]' \
                                 '/behavior-group/div/div[2]/div[1]/mat-checkbox'
    blank_stare_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                        '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[1]/div[2]' \
                        '/behavior-group/div/div[2]/div[1]/mat-checkbox/label/span[2]'
    # Fundamentals

    # Following Distance

    # Traffic Violations
    red_light_checkbox_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                               '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[1]/div[5]' \
                               '/behavior-group/div/div[2]/div[3]/mat-checkbox'
    red_light_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                      '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[1]/div[5]' \
                      '/behavior-group/div/div[2]/div[3]/mat-checkbox/label/span[2]'

    # Driver Condition

    # Driver Conduct
    falling_asleep_checkbox_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                                    '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[1]/div[6]' \
                                    '/behavior-group/div/div[2]/div[2]/mat-checkbox'
    falling_asleep_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                           '/div/mat-tab-body[2]/div/behaviors-review/div[1]/div[1]/div[6]' \
                           '/behavior-group/div/div[2]/div[2]/mat-checkbox/label/span[2]'

    # Other Behaviors

    # Driver Un-belted

    # Custom Behaviors
    custom_behaviors_container_xpath = '/html/body/app-root/top-bar/app-review/div/review-bar/mat-tab-group' \
                                       '/div/mat-tab-body[2]/div/behaviors-review/div[2]/div[1]/div[4]' \
                                       '/behavior-group/div/div[2]'

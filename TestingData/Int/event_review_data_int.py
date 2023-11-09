class EventReviewDataInt:

    # general
    # company_id = 1129
    company_name_switch = '101 Towing'
    company_name = 'DriveCam DC4DC Test Co'
    reviewer_user_name = 'reviewerbychris'
    reviewer_password = 'Login123!'
    review_id_range_from = '4025987370'
    review_id_range_to = '5025980126'

    # driver
    driver_employee_id = 'auto_test_9527'
    driver_name = 'auto_test donot_edit'
    driver_id = '0000FFFF-0000-0B00-F44C-ED46B0D60000'

    # coach
    coach_user_name = 'auto_coach_9876'
    coach_password = 'Login123!'

    # f2f coaching event behaviors
    f2f_behavior_1st = 'Red Light'

    # create new event
    ER = 'QM40011227'
    ER_with_custom_behaviors = 'QM40011227'   # in group with some custom behaviors, Root/Cellular Unassigned
    # custom behaviors in Root/Cellular Unassigned
    custom_behaviors = ['Behavior', 'Other', 'Unsafe and Unnecessary', 'U-Turn', 'Pedestrian/Bicyclist',
                        'Trailer Detachment', 'Sleeper Berth Securement', 'Tandem Slide', 'Tree Strike']
    custom_behavior_comments = ["Comment",
                                "The event was triggered due to a force exceeding the video event recorder's threshold.",
                                "It is your organization's policy to select Unsafe and Not Necessary anytime the vehicle is traveling 15 miles per hour or greater when there is no passenger present in the vehicle.",
                                "The driver made a U-turn on the roadway.",
                                "The vehicle came close to a pedestrian or bicyclist.",
                                "There was an issue identified with the trailer in this event.",
                                "A passenger does not appear to be secured in the sleeper berth.",
                                "This event may have resulted in a tandem axle slide.",
                                "The vehicle made contact with a tree."]
    ER_without_custom_behaviors = 'SF00001440'    # in group without custom behaviors, Root/BruteForce
    ER_with_many_custom_behaviors = 'SF80000128'  # in group with more than 8 custom behaviors, Root/Christian Koguchi
    trigger = 'Handheld Device'
    vehicle = 'Colin Otto'
    vehicle_type = 'Unassigned'
    seatbelt = 'Shoulder Harness'
    audio = 'No'
    fps = '10'
    actor_id = '0000FFFF-0000-1B00-6CAA-ED46B0D60000'

    # event play data
    start_time = '-10.00'
    end_time = '+0.00'

    num_of_back_steps_1 = 3
    fwd_of_back_steps_1 = '-0.03'
    lat_of_back_steps_1 = '+0.04'
    time_of_back_steps_1 = '-0.30'
    speed_of_back_steps_1 = '+ 9.9 MPH'

    num_of_back_steps_2 = 5
    fwd_of_back_steps_2 = '-0.07'
    lat_of_back_steps_2 = '+0.04'
    time_of_back_steps_2 = '-0.80'
    speed_of_back_steps_2 = '+ 10.4 MPH'

    fwd_value_by_click = 'FWD: -0.12'
    lat_value_by_click = 'LAT: +0.05'
    time_value_by_click = 'TIME: -4.80'
    speed_value_by_click = 'GPS SPEED: + 16.4 MPH'

    fwd_value_by_drag = 'FWD: -0.08'
    lat_value_by_drag = 'LAT: +0.04'
    time_value_by_drag = 'TIME: -4.50'
    speed_value_by_drag = 'GPS SPEED: + 15.2 MPH'

    # event play data for 2nd event
    behavior_1st = 'cellphone'
    behavior_2nd = 'smoking'

    fwd_value_by_click_2nd = 'FWD: -0.04'
    lat_value_by_click_2nd = 'LAT: -0.04'
    time_value_by_click_2nd = 'TIME: -1.80'
    speed_value_by_click_2nd = 'GPS SPEED: + 21.1 MPH'

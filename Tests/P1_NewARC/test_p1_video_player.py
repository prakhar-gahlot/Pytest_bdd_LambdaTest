from datetime import datetime, timedelta
from time import sleep
from pytest_bdd import scenarios, given, when, then
from Pages.Arc.event_list_page import EventListPage
from Pages.Arc.event_review_page import EventReviewPage
from Pages.Arc.login_page import LoginPage
from Tests.common import ARC_URL, ENV, AutomationDataManager
from TestingData.Int.event_review_data_int import EventReviewDataInt as ERD_INT
from TestingData.Stg.event_review_data_stg import EventReviewDataStg as ERD_STG
from TestingData.Prod.event_review_data_prod import EventReviewDataProd as ERD_PROD

LOGIN_PAGE = 0
EVENT_LIST_PAGE = 0
EVENT_REVIEW_PAGE = 0
ERD = ''
EVENT_REVIEW_ID = 0
DATA_MGR = ''

scenarios('../../Features/P1_NewARC/p1_video_player.feature')


# LQ-11160
@given('"Reviewer" logs in ARC')
def logs_in_arc(browser):
    global LOGIN_PAGE, EVENT_LIST_PAGE, EVENT_REVIEW_PAGE, ERD, DATA_MGR

    DATA_MGR = AutomationDataManager()
    LOGIN_PAGE = LoginPage(browser)
    EVENT_LIST_PAGE = EventListPage(browser)
    EVENT_REVIEW_PAGE = EventReviewPage(browser)

    browser.get(ARC_URL)

    if ENV == 'int':
        ERD = ERD_INT
    elif ENV == 'stg':
        ERD = ERD_STG
    else:
        ERD = ERD_PROD

    LOGIN_PAGE.user_name().type(ERD.reviewer_user_name)
    LOGIN_PAGE.password().type(ERD.reviewer_password)
    LOGIN_PAGE.login().click()
    LOGIN_PAGE.search_company().wait_for_element_displayed()
    LOGIN_PAGE.search_company().type_and_auto_search(ERD.company_name)
    LOGIN_PAGE.first_company().click()
    LOGIN_PAGE.select_company().click()


@when('"Reviewer" filtered out some events in new ARC and the user clicks one event review ID and the user checks the event details above event video')
def filter_in_new_tab():
    global EVENT_REVIEW_ID, EVENT_ID
    EVENT_REVIEW_ID = DATA_MGR.create_new_event()

    EVENT_LIST_PAGE.review_id_filter().type(EVENT_REVIEW_ID)
    EVENT_LIST_PAGE.filter_button().click()
    EVENT_ID = EVENT_LIST_PAGE.event_id_1st_only().get_text()
    EVENT_LIST_PAGE.review_id_1st().click()


@then('Review ID is displayed correctly and Trigger is displayed correctly and Record Date is displayed based on local time zone and format is YYYY-MM-DD hh:mm AM/PM')
def verify_review_id_and_trigger_and_record_date():
    EVENT_REVIEW_PAGE.review_id().wait_for_expected_text(str(EVENT_REVIEW_ID))
    record_date = EVENT_REVIEW_PAGE.record_date().get_text()
    am_pm = record_date[-2:]
    record_date_time = datetime.strptime(record_date[:-3], '%m/%d/%Y %I:%M')

    assert EVENT_REVIEW_PAGE.review_id().get_text() == str(EVENT_REVIEW_ID)
    assert EVENT_REVIEW_PAGE.trigger().get_text() == ERD.trigger
    assert (am_pm == 'AM' or am_pm == 'PM') is True
    assert record_date_time < datetime.now()
    assert record_date_time > datetime.now() + timedelta(days=-1)

@then('Vehicle ID is displayed as vehicle name and Vehicle type is displayed correctly and Seatbelt is displayed correctly and Audio is displayed correctly and FPS is displayed correctly')
def verify_vehicle_info_audio_fps():
    assert EVENT_REVIEW_PAGE.vehicle_id().get_text() == ERD.vehicle
    assert EVENT_REVIEW_PAGE.vehicle_type().get_text() == ERD.vehicle_type
    assert EVENT_REVIEW_PAGE.seatbelt().get_text() == ERD.seatbelt
    assert EVENT_REVIEW_PAGE.audio().get_text() == ERD.audio
    assert EVENT_REVIEW_PAGE.FPS().get_text() == ERD.fps

#LQ-15626
@when('"Reviewer" opens an event')
def open_an_event():
    sleep(1) # nothing to do there since the event is already opened

@then('the video automatically plays with both front and rear camera views and the Rear+Front is selected as default')
def verify_event_play():
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.is_button_active(EVENT_REVIEW_PAGE.rear_and_front()) is True
    assert EVENT_REVIEW_PAGE.is_button_active(EVENT_REVIEW_PAGE.rear()) is False
    assert EVENT_REVIEW_PAGE.is_button_active(EVENT_REVIEW_PAGE.front()) is False

@then('the video controller bar is displayed with backward button, play button, forward button, backward -1 button, forward +1 button, Rear+Front button, Rear button, Front button, Full Screen button, Stopwatch button')
def verify_video_controls():
    assert EVENT_REVIEW_PAGE.backward().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.play_and_pause().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.forward().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.backward_1().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.forward_1().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.full_screen().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.stop_watch().element_is_displayed() is True

# When step is the same with previous scenario

@then('the review page is start at Outcome & Event Trigger tab')
def verify_review_page_start_at_outcome_trigger_tab():
    assert EVENT_REVIEW_PAGE.is_tab_active(EVENT_REVIEW_PAGE.outcome_trigger_tab(), True) is True

#LQ-11159
# When step is the same with previous test case LQ-15626

@then('user still sees these info at top of event video: "Lytx ReviewCenter", "Reviewing for: Company A", "Switch Companies" buttons')
def verify_titles():
    assert EVENT_REVIEW_PAGE.top_bar_title().get_text() == 'Lytx ReviewCenter'
    assert EVENT_REVIEW_PAGE.top_bar_review_text().get_text() == 'Reviewing for: ' + ERD.company_name
    assert EVENT_REVIEW_PAGE.top_bar_switch_company().get_text() == 'Switch Companies'

#LQ-11698
@when('"Reviewer" opens an event by clicking one review ID')
def open_an_event_by_clicking_review_id():
    if EVENT_REVIEW_PAGE.back_to_home().wait_for_element_is_clickable() is False:
        EVENT_REVIEW_PAGE.refresh_page()
        EVENT_REVIEW_PAGE.back_to_home().wait_for_element_is_clickable()
    EVENT_REVIEW_PAGE.back_to_home().click()
    EVENT_LIST_PAGE.review_id_1st().click()

@then('both front and rear camera views are shown and the video automatically plays')
def verify_video_and_autoplay():
    assert EVENT_REVIEW_PAGE.play_and_pause().get_text() == 'pause'
    assert EVENT_REVIEW_PAGE.play_and_pause().get_text('play_arrow', 10) == 'play_arrow'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'

@then('the video height is set to 352 and the video width is set to 1280')
def verify_video_size():
    assert EVENT_REVIEW_PAGE.video().size() == {'height': 352, 'width': 1280}

@then('the following event information is displayed for the corresponding time that is shown on the video: FWD, LAT, TIME, GPS SPEED and the scrubber on the force graph moves along the timeline in sync with the video as it’s playing and the video time is displayed next to the scrubber correctly')
def verify_fwd_lat_time_speed():
    assert EVENT_REVIEW_PAGE.scrubber().element_is_displayed() is True

    i = 0
    while i < ERD.num_of_back_steps_1:
        i += 1
        EVENT_REVIEW_PAGE.backward_1().click()

    assert EVENT_REVIEW_PAGE.fwd().get_text() == ERD.fwd_of_back_steps_1
    assert EVENT_REVIEW_PAGE.lat().get_text() == ERD.lat_of_back_steps_1
    assert EVENT_REVIEW_PAGE.time().get_text() == ERD.time_of_back_steps_1
    assert EVENT_REVIEW_PAGE.gps_speed().get_text() == ERD.speed_of_back_steps_1
    assert EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_of_back_steps_1

    i = 0
    while i < ERD.num_of_back_steps_2:
        i += 1
        EVENT_REVIEW_PAGE.backward_1().click()

    assert EVENT_REVIEW_PAGE.fwd().get_text() == ERD.fwd_of_back_steps_2
    assert EVENT_REVIEW_PAGE.lat().get_text() == ERD.lat_of_back_steps_2
    assert EVENT_REVIEW_PAGE.time().get_text() == ERD.time_of_back_steps_2
    assert EVENT_REVIEW_PAGE.gps_speed().get_text() == ERD.speed_of_back_steps_2
    assert EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_of_back_steps_2

# LQ-12479
@when('the user enters the event review page')
def enter_event_review_page():
    EVENT_REVIEW_PAGE.forward().click()

@then('the X-axis represents time on the force graph and the Y-axis represents force on the force graph')
def verify_x_axis_y_axis():
    assert EVENT_REVIEW_PAGE.telemetry_graph().element_is_displayed() is True

@then('the force graph could display correctly for the event same as FWD/LAT/TIME data')
def verify_fwd_lat_time_on_force_graph():
    i = 0
    while i < ERD.num_of_back_steps_1:
        i += 1
        EVENT_REVIEW_PAGE.backward_1().click()

    EVENT_REVIEW_PAGE.backward_1().move_to_element(0, -30)

    assert EVENT_REVIEW_PAGE.fwd_force_graph().get_text() == ERD.fwd_value_by_click
    assert EVENT_REVIEW_PAGE.lat_force_graph().get_text() == ERD.lat_value_by_click
    assert EVENT_REVIEW_PAGE.time_force_graph().get_text() == ERD.time_value_by_click
    assert EVENT_REVIEW_PAGE.gps_speed_force_graph().get_text() == ERD.speed_value_by_click

@then('there is a scrubber shows on the force graph with the video time displayed')
def verify_scrubber():
    assert EVENT_REVIEW_PAGE.scrubber().element_is_displayed() is True
    assert EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_of_back_steps_1

# LQ-11700
@when('the user click full-screen button and the user clicks Rear')
def enter_rear_view_full_screen_mode():
    EVENT_REVIEW_PAGE.full_screen().click()
    EVENT_REVIEW_PAGE.rear().click()

@then('the video shows the Rear view only in full-screen mode')
def verify_rear_view_full_screen_mode():
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.front_view_text().get_attribute('class') == 'no-front-label'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'rear-full-screen'

@when('the user click full-screen button and the user clicks Front')
def enter_front_view_full_screen_mode():
    EVENT_REVIEW_PAGE.front().click()

@then('the video shows the Front view only in full-screen mode')
def verify_front_view_full_screen_mode():
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_attribute('class') == 'no-rear-label'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'front-full-screen'

@when('the user click full-screen button and the user clicks Front and the user clicks Full Screen')
def enter_and_exit_full_screen_mode():
    EVENT_REVIEW_PAGE.full_screen().click()

@then('the video shows the Front view and exits full-screen mode')
def verify_front_view_exit_full_screen_mode():
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_attribute('class') == 'no-rear-label'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'front'

@when('the user click full-screen button and the user clicks Rear+Front')
def enter_full_screen_mode_rear_front():
    EVENT_REVIEW_PAGE.full_screen().click()
    EVENT_REVIEW_PAGE.rear_and_front().click()

@then('the video shows the Rear+Front view and exits full-screen mode')
def verify_rear_front_view_exist_full_screen_mode():
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'default'

@when('the user clicks Rear in default mode')
def enter_default_mode_rear_view():
    EVENT_REVIEW_PAGE.back_to_home().click()
    EVENT_LIST_PAGE.review_id_1st().click()
    EVENT_REVIEW_PAGE.rear().click()

@then('the video enter full screen mode and shows the Rear view')
def verify_full_screen_mode_with_rear_view():
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.front_view_text().get_attribute('class') == 'no-front-label'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'rear-full-screen'

@when('the user clicks Front in default mode')
def enter_default_mode_front_view():
    EVENT_REVIEW_PAGE.full_screen().click() # click full screen to exist full screen mode
    EVENT_REVIEW_PAGE.front().click()

@then('the video enter full screen mode and shows the Front view')
def verify_full_screen_mode_with_front_view():
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_attribute('class') == 'no-rear-label'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'front-full-screen'

@when('the user clicks Rear+Front in default mode')
def enter_default_mode_rear_front_view():
    EVENT_REVIEW_PAGE.full_screen().click() # click full screen to exist full screen mode
    EVENT_REVIEW_PAGE.rear_and_front().click()

@then('the video shows the Rear+Front view in default mode')
def verify_rear_front_view_default_mode():
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_text() == 'REAR VIEW'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'default'

@when('the user clicks full-screen button in default mode')
def enter_full_screen_mode():
    EVENT_REVIEW_PAGE.full_screen().click()

@then('the video shows the Front view in full-screen mode')
def verify_enter_full_screen_mode():
    assert EVENT_REVIEW_PAGE.front_view_text().get_text() == 'FRONT VIEW'
    assert EVENT_REVIEW_PAGE.rear_view_text().get_attribute('class') == 'no-rear-label'
    assert EVENT_REVIEW_PAGE.video().get_attribute('class') == 'front-full-screen'

@when('the user clicks pause button')
def pause_event():
    EVENT_REVIEW_PAGE.back_to_home().click()
    EVENT_LIST_PAGE.review_id_1st().click()
    EVENT_REVIEW_PAGE.event_play_time().wait_for_expected_text_change(ERD.end_time, 60, 1)
    EVENT_REVIEW_PAGE.event_play_time().wait_for_expected_text_change(ERD.start_time, 60, 1)
    EVENT_REVIEW_PAGE.play_and_pause().click()

@then('the event video is paused')
def verify_event_pause():
    assert EVENT_REVIEW_PAGE.play_and_pause().get_text() == 'play_arrow'

@when('the user clicks play button')
def play_event():
    sleep(1)
    EVENT_REVIEW_PAGE.play_and_pause().click()

@then('the event video plays with correct timeline')
def verify_event_play():
    event_play_time = EVENT_REVIEW_PAGE.event_play_time().get_text()

    assert EVENT_REVIEW_PAGE.play_and_pause().wait_for_expected_text('pause') == 'pause'

    EVENT_REVIEW_PAGE.event_play_time().wait_for_expected_text_change(event_play_time, 60, 1)
    assert EVENT_REVIEW_PAGE.event_play_time().get_text() != event_play_time

@when('the user clicks backward button')
def backward_event():
    EVENT_REVIEW_PAGE.backward().click()

@then('the event video goes to the beginning of the video')
def verify_backward_event():
    assert EVENT_REVIEW_PAGE.play_and_pause().get_text() == 'play_arrow'
    assert EVENT_REVIEW_PAGE.event_play_time().get_text() == ERD.start_time

@when('the user clicks forward button')
def forward_event():
    EVENT_REVIEW_PAGE.forward().click()

@then('the event video goes to the end of the video')
def verify_forward_event():
    assert EVENT_REVIEW_PAGE.play_and_pause().get_text() == 'play_arrow'
    assert EVENT_REVIEW_PAGE.event_play_time().get_text() == ERD.end_time

@when('the user clicks on force graph')
def click_on_force_graph():
    EVENT_REVIEW_PAGE.backward_1().move_to_element_and_click(0, -30)

@then('the event video jumps to the time point user clicked')
def verify_clicking_on_force_graph():
    assert 'FWD: ' + EVENT_REVIEW_PAGE.fwd().get_text() == ERD.fwd_value_by_click
    assert 'LAT: ' + EVENT_REVIEW_PAGE.lat().get_text() == ERD.lat_value_by_click
    assert 'TIME: ' + EVENT_REVIEW_PAGE.time().get_text() == ERD.time_value_by_click
    assert 'GPS SPEED: ' + EVENT_REVIEW_PAGE.gps_speed().get_text() == ERD.speed_value_by_click
    assert 'TIME: ' + EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_value_by_click

@when('the user drags on force graph')
def drag_on_force_graph():
    EVENT_REVIEW_PAGE.drag_and_drop(50, 0)

@then('the event video jumps to the time point user drags')
def verify_dragging_on_force_graph():
    assert 'FWD: ' + EVENT_REVIEW_PAGE.fwd().get_text() == ERD.fwd_value_by_drag
    assert 'LAT: ' + EVENT_REVIEW_PAGE.lat().get_text() == ERD.lat_value_by_drag
    assert 'TIME: ' + EVENT_REVIEW_PAGE.time().get_text() == ERD.time_value_by_drag
    assert 'GPS SPEED: ' + EVENT_REVIEW_PAGE.gps_speed().get_text() == ERD.speed_value_by_drag
    assert 'TIME: ' + EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_value_by_drag

@when('the user clicks backward -1 button')
def backward_1_step():
    EVENT_REVIEW_PAGE.forward().click()

    i = 0
    while i < ERD.num_of_back_steps_2 + ERD.num_of_back_steps_1:
        i += 1
        EVENT_REVIEW_PAGE.backward_1().click()

@then('the event video jumps backward 1 step')
def verify_backward_1_step():
    assert EVENT_REVIEW_PAGE.fwd().get_text() == ERD.fwd_of_back_steps_2
    assert EVENT_REVIEW_PAGE.lat().get_text() == ERD.lat_of_back_steps_2
    assert EVENT_REVIEW_PAGE.time().get_text() == ERD.time_of_back_steps_2
    assert EVENT_REVIEW_PAGE.gps_speed().get_text() == ERD.speed_of_back_steps_2
    assert EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_of_back_steps_2

@when('the user clicks forward +1 button')
def forward_1_step():
    i = 0
    while i < ERD.num_of_back_steps_2:
        i += 1
        EVENT_REVIEW_PAGE.forward_1().click()

@then('the event video jumps forward 1 step')
def verify_forward_1_step():
    assert EVENT_REVIEW_PAGE.fwd().get_text() == ERD.fwd_of_back_steps_1
    assert EVENT_REVIEW_PAGE.lat().get_text() == ERD.lat_of_back_steps_1
    assert EVENT_REVIEW_PAGE.time().get_text() == ERD.time_of_back_steps_1
    assert EVENT_REVIEW_PAGE.gps_speed().get_text() == ERD.speed_of_back_steps_1
    assert EVENT_REVIEW_PAGE.current_time().get_text() == ERD.time_of_back_steps_1

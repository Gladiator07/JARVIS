## happy path greet 
* greet
  - utter_greet
  
## happy path without 4g sim
* thanks
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## happy path
* network_issue
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* affirm
  - utter_tell_issue
* facing_issue
  - utter_change_settings
* guide_me
  - utter_solution
* have_to_do
  - utter_solution_4G
* thanks
  - utter_anything_else
* deny
 - utter_thanks

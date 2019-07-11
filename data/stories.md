## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## recommendation no city
* recommendation
  - utter_ask_city
* input_city{"city": "boston"}
  - action_recommend_poi
  - utter_recommendation

## recommendation
* recommendation{"city": "boston"}
  - action_recommend_poi
  - utter_recommendation
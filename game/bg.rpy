init python:
  flash_img = "bg/flash.png"
  kanae_room_raining = "bg/p_room_raining.png"
  p_room_night = "bg/p_room.png"
  itawa_kyoto_house_fire = "bg/itawa_inner_house_kyoto_fire.png"
  itawa_inner_house = "bg/itawa_inner_house.png"
  road_car_cooled = "bg/road_cooled.png"
  road_night = "bg/road_night.png"
  oyab_motorhome = "bg/oyab_motorhome.png"
  town_morning = "bg/town.png"
  alan_house_exploding = "bg/alan_room_exploding.png"

######################

image bg dark = "bg/dark.png"
image bg flash = flash_img
image bg red_layer = "red_layer.png"

image bg school_morning = "bg/school.png"
image bg school_evening = "bg/school_evening.png"

image bg itawa_house_front_before_evening = "bg/itawa_house_front_evening.png"
image bg itawa_house_front_before = "bg/itawa_house_front.png"

image bg itawa_house_front = "bg/itawa_house_after.png"
image bg itawa_house_front_evening = "bg/itawa_house_after_evening.png"
image bg itawa_house_front_night = "bg/itawa_house_after_night.png"

image bg kanae_room_morning = "bg/p_room.png"
image bg kanae_room_evening = "bg/p_room.png"
image bg kanae_room_raining = kanae_room_raining
image bg kanae_room_night = "bg/p_room.png"
image bg kanae_room_colder = "bg/p_room_cold.png"

image bg main_living = "bg/p_living.png"
image bg main_living_evening = "bg/p_living_evening.png"
image bg kitchen = "bg/kitchen.png"

image bg itawa_inner_house = itawa_inner_house

image bg itawa_kyoto_house_normal = "bg/itawa_inner_house_kyoto.png"
image bg itawa_kyoto_house_fire = itawa_kyoto_house_fire

image bg police_station = "bg/police_room.png"

image bg highway_home = "bg/road.png"

image bg town evening = "bg/town_evening.png"
image bg town morning = town_morning

image bg park_morning = "bg/park.png"
image bg park_evening = "bg/park_evening.png"

image bg road day = "bg/road.png"
image bg road car = "bg/road_evening.png"
image bg road car cooled = road_car_cooled
image bg road night = road_night
image bg road night police = "bg/road_police.png"

image bg oyab motorhome = oyab_motorhome
image bg oyab motorhome eyelids = "bg/oyab_motorhome_eyelids.png"
image bg oyab house = "bg/oyab_house.png"
image bg oyab house room evening = "bg/alan_room.png"
image bg oyab house room morning = "bg/alan_room.png"
image bg oyab house faraway = "bg/desert.png"
image bg oyab house faraway dust = "bg/desert_dust.png"

image bg hospital room = "bg/hospital_room.png"
image bg hospital room distorted = "bg/hospital_room_distorted.png"
image bg hospital corridor = "bg/hospital_corridor.png"
image bg hospital corridor distorted = "bg/hospital_corridor_distort.png"
image bg hospital morgue = "bg/hospita_morgue.png"
image bg hospital front = "bg/hospital.png"

image bg shadow_tree = "bg/tree.png"
image bg time_madness animated: 
  "bg/itawa_house_front.png" with Dissolve(0.2, alpha=True)
  pause 0.3
  "bg/desert.png" with Dissolve(0.1, alpha=True)
  pause 0.6
  "bg/p_room.png" with Dissolve(0.2, alpha=True)
  pause 0.3
  "bg/park.png" with Dissolve(0.1, alpha=True)
  pause 0.3
  "bg/road_evening.png" with Dissolve(0.2, alpha=True)
  pause 0.6
  "bg/hospital.png" with Dissolve(0.1, alpha=True)
  pause 0.8
  repeat

image bg car chase = "bg/car.png"

image bg alan_house normal = "bg/alan_room.png"
image bg alan_house exploding = alan_house_exploding

image red_layer = "hurt.png"
image dark = "bg/dark.png"
image white = flash_img
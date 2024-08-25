from modules import project as Proj

all_projects: list[Proj.Project_obj] = []

#EMP Project
EMP_proj = Proj.Project_obj("EMP", "This experiment was done to see if electromagnetic waves of a diffrent frequency of light could trigger photo synthesis.", project_date="Jan 2018", thumbnail_src="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/Photon_EMP/spark_gap_magnified.gif")
hero_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://live.staticflickr.com/65535/52798783778_0624d7202e_b.jpg")


# Creating the EMP
emp_creation_group = Proj.Content_group(heading="EMP Design and Build")
emp_case_2d_sketch = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/EMP_Case_2D_Sketch2.jpeg")
emp_case_pre_print = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/EMP_Case_Pre_Print.jpeg")
emp_creation_group.add_content(emp_case_2d_sketch)
emp_creation_group.add_content(emp_case_pre_print)

# Spark Gap Info Group
sparkgap_info_group = Proj.Content_group()
sparkgap_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/Photon_EMP/spark_gap_magnified.gif", position=Proj.content_position.LEFT)
sprakgap_info_text = Proj.proj_content_obj(Proj.proj_content_type.TEXT, position=Proj.content_position.CENTER, text_content="One of the First Initial test of the electronics. This is a view of the spark gap for the EMP device.")
circuit_view_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/EMP_Circuit_View.JPG", position=Proj.content_position.RIGHT)
sparkgap_info_group.add_content(sparkgap_gif)
sparkgap_info_group.add_content(circuit_view_img)
sparkgap_info_group.add_content(sprakgap_info_text)

# experiment Emp Group
running_experiment_group = Proj.Content_group()
photon_emp_test_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/photon_emp_test.jpeg", position=Proj.content_position.RIGHT)
experiment_desc = Proj.proj_content_obj(Proj.proj_content_type.TEXT,"Control Plant in the rear away from EMP Device. The Treatment plant is the center of the EMP device.", position=Proj.content_position.RIGHT)
running_experiment_group.add_content(experiment_desc)
running_experiment_group.add_content(photon_emp_test_img)

# experiment results Group
experiment_results_group = Proj.Content_group(heading="Plant Results after EMP Treatmeant")
emp_test_results = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/photon_emp_test_results.jpeg")
carbon_deoxide_results_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE,content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/carbon_deoxide_results.jpeg")
dissolved_oxygen_scale_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/dissolved_oxygen_scale.jpeg")
experiment_results_group.add_content(emp_test_results)
experiment_results_group.add_content(carbon_deoxide_results_img)
experiment_results_group.add_content(dissolved_oxygen_scale_img)

EMP_proj.add_content(hero_img)
EMP_proj.add_content(emp_creation_group)
EMP_proj.add_content(sparkgap_info_group)
EMP_proj.add_content(running_experiment_group)
EMP_proj.add_content(experiment_results_group)




#Teaching Project
teaching_proj = Proj.Project_obj("Instructor", "Instructor for Digipen Instituite of technology.", project_date="2021-2022")
teaching_desc = Proj.proj_content_obj(Proj.proj_content_type.TEXT, text_content="Taught in person at two school and online classes.")
teaching_proj.add_content(teaching_desc)

#Game Dev
#Super Cube Game
super_cube_proj = Proj.Project_obj("SuperCube", "A hypercasual game where levels are dynamically generated based on how far the player makes it throug the game.", project_date="2018", thumbnail_src="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/super_cube_game/super_cube_gif.gif")

super_cuber_header_group = Proj.Content_group()
hero_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/super_cube_game/super_cube_gif.gif")
super_cuber_header_group.add_content(hero_gif)

super_cube_experimentation_group = Proj.Content_group(heading="Game Core Loop Experimentation")
super_cube_early_mechanics_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/super_cube_game/Super_Cube_Experimentation.gif")
super_cube_early_mechanics2_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/super_cube_game/Super_Cube_Experimentation2.gif")
super_cube_experimentation_group.add_content(super_cube_early_mechanics_gif)
super_cube_experimentation_group.add_content(super_cube_early_mechanics2_gif)

super_cube_proj.add_content(super_cuber_header_group)
super_cube_proj.add_content(super_cube_experimentation_group)

#Blast Up Game
blast_up_proj = Proj.Project_obj("Blast-Up", "A hypercasual game where players protect a rocket ship as aireborne obstacles try to bring the ship down. ", project_date="2018", thumbnail_src="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/blast_up_game/Blast_up_game.gif")

blast_up_header_group = Proj.Content_group()
hero_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/blast_up_game/Blast_up_game.gif")
blast_up_header_group.add_content(hero_gif)

blast_up_lvl_design_group = Proj.Content_group(heading="Game Level Design")
blast_up_lvl_design_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Blast_Up_game/Blast_Up_Art_Design.jpg")
blast_up_scrolling_bg_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/blast_up_game/Blast_Up_Scrolling_Background.gif")
blast_up_lvl_design_group.add_content(blast_up_lvl_design_img)
blast_up_lvl_design_group.add_content(blast_up_scrolling_bg_gif)

blast_up_leader_board_group = Proj.Content_group(heading="Leader Board System")
blast_up_leader_board_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Blast_Up_game/Blast_Up_Leader_board_2.PNG")
blast_up_leader_board_entry = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Blast_Up_game/New_leader_board_entry.PNG")
blast_up_leader_board_group.add_content(blast_up_leader_board_img)
blast_up_leader_board_group.add_content(blast_up_leader_board_entry)

blast_up_play_testing_group = Proj.Content_group(heading="Development Play Testing")
blast_up_beta_test_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Blast_Up_game/Blast_up_beta_testing.JPG")
blast_up_play_testing_group.add_content(blast_up_beta_test_img)

blast_up_proj.add_content(blast_up_header_group)
blast_up_proj.add_content(blast_up_leader_board_group)
blast_up_proj.add_content(blast_up_lvl_design_group)
blast_up_proj.add_content(blast_up_play_testing_group)

#App Dev

#Robotics
robotics_competing = Proj.Project_obj("competitive-robotics", "During Middle/Highschool I enoyed being a contributing member to the competitve robotics clubs. particpating in FTC events in middle school and FRC events in highschool.", project_date="2016-2017", thumbnail_src="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/robotics_3588_robot.JPG")

robotics_competing_header_group = Proj.Content_group()
hero_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/highschool-robotics-team-group.PNG", position=Proj.content_position.RIGHT)
robotics_competing_header_group.add_content(hero_img)

team_info_group = Proj.Content_group(heading="Team 3588")
team_bot_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/robotics_3588_robot.JPG")
team_bot_side_view = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/team_bot_side_view.JPG")
team_info_group.add_content(team_bot_side_view)
team_info_group.add_content(team_bot_img)

pre_comp_group = Proj.Content_group(heading="Pre-Competition")
robot_pre_comp_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/robot_pre_competition.gif")
pre_comp_group.add_content(robot_pre_comp_gif)

pneumatic_system_group = Proj.Content_group(heading="Robot pneumatic system experimentaiton")
pneumatic_system_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/experimenting_bot_pneumatic_system.gif")
pneumatic_sys_desc = Proj.proj_content_obj(Proj.proj_content_type.TEXT, text_content="Our Team bot Utilized pneumatic controlled actuators. We wanted to test if we were able to use this mechanism to pick up gears. During the competition the robot will have the ability to transport gears as part of the objective to score point during a competitive match.")
pneumatic_system_group.add_content(pneumatic_system_gif)
pneumatic_system_group.add_content(pneumatic_sys_desc)


bot_climbing_mechanism_group = Proj.Content_group(heading="Climbing Mechanism")
climbing_mechanism_test = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/bot_climbing_mechanism_experiment.gif")
bot_climbing_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/bot_climbing_test.gif")
bot_climbing_mechanism_group.add_content(bot_climbing_gif)
bot_climbing_mechanism_group.add_content(climbing_mechanism_test)

bot_drive_system_group = Proj.Content_group(heading="Robot Drive System")
locomototion_example_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/robot_movement_show_case.gif")
omni_wheel_close_up_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/Omni_Wheel_Close_Up.JPG")
locomotion_intial_test_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/bot_locomotion_intial_test.gif")
bot_drive_system_group.add_content(locomototion_example_gif)
bot_drive_system_group.add_content(omni_wheel_close_up_img)
bot_drive_system_group.add_content(locomotion_intial_test_gif)

drive_system_design_group = Proj.Content_group(heading="Robot Chassis Design")
bot_base_initial_design_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/bot_base_initial_design.JPG")
bot_cad_view_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/bot_chassis_cad_view.JPG")
bot_measurements_view_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/bot_frame_measurements_view.JPG")
drive_system_design_group.add_content(bot_base_initial_design_img)
drive_system_design_group.add_content(bot_cad_view_img)
drive_system_design_group.add_content(bot_measurements_view_img)

robotics_competing.add_content(robotics_competing_header_group)
robotics_competing.add_content(team_info_group)
robotics_competing.add_content(pneumatic_system_group)
robotics_competing.add_content(bot_climbing_mechanism_group)
robotics_competing.add_content(bot_drive_system_group)
robotics_competing.add_content(drive_system_design_group)
robotics_competing.add_content(pre_comp_group)

# Smart Mirror
printed_smart_mirror_proj = Proj.Project_obj("3D Printed Smart Mirror",project_desc="This Mirrors casing is entierly 3D-printed making the mirror exceptionaly light. this mirror features include Chat-GPT, Augment Reality, Sound System, and More!", project_date="2022", thumbnail_src="https://live.staticflickr.com/65535/52727321385_a748270f52_b.jpg")

printed_mirror_header_group = Proj.Content_group()
printed_mirror_hero_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://live.staticflickr.com/65535/52727321385_a748270f52_b.jpg")
printed_mirror_header_group.add_content(printed_mirror_hero_img)

# Smart Mirror - Design Group
printed_mirror_design_group = Proj.Content_group(heading="Mirror Design")

mirror_frame_design_carousel = Proj.Carousel_obj("Mirror_Case_Components")
mirror_frame_front_top_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727162194_d0f8b5cc21_b.jpg",desc="Front Section: Top View - Mirror Frame")
mirror_frame_front_bottom_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727385888_981ba69fcf_b.jpg",desc="Front Section: Rear View - Mirror Frame")
mirror_frame_mid_rear_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52726903611_db4f470b44_b.jpg", desc="Mid Section: Rear View - Mirror Frame")
mirror_frame_mid_top_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727162129_6fa00fd814_b.jpg", desc="Mid Section : Top View - Mirror Frame")
mirror_frame_rear_iso_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52726384467_e76e8852d3_b.jpg", desc="Rear Section : Isometric View - Mirror Frame")
mirror_frame_assembled_rear = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52726384452_e36de61e4d_b.jpg", desc="Assembeld Mirror - Rear without Case Cover")
mirror_frame_assembled_iso = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727162074_cc11d4f607_b.jpg", desc="Assembled Mid Section - With partial rear case ")
mirror_assembled_front = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727385818_8f1f8a3a5b_b.jpg", desc="Assembled Front View")
mirror_front_frame_pins = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727162159_e8815de294_b.jpg", desc="Front Section Pin View")
mirror_front_and_mirror = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52726384512_824d541671_b.jpg", desc="Front Section and Mirror")
mirror_front_and_monitor = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52727321370_f5c671d178_b.jpg", desc="Front Section and Monitor")
mirror_complete_rear = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52726903696_8fd70b912f_b.jpg", desc="Complete Rear Section")

mirror_frame_design_carousel.add_item(mirror_frame_front_top_img)
mirror_frame_design_carousel.add_item(mirror_frame_front_bottom_img)
mirror_frame_design_carousel.add_item(mirror_front_frame_pins)
mirror_frame_design_carousel.add_item(mirror_frame_mid_rear_img)
mirror_frame_design_carousel.add_item(mirror_frame_mid_top_img)
mirror_frame_design_carousel.add_item(mirror_complete_rear)
mirror_frame_design_carousel.add_item(mirror_frame_rear_iso_img)
mirror_frame_design_carousel.add_item(mirror_frame_assembled_rear)
mirror_frame_design_carousel.add_item(mirror_frame_assembled_iso)
mirror_frame_design_carousel.add_item(mirror_assembled_front)
mirror_frame_design_carousel.add_item(mirror_front_and_mirror)
mirror_frame_design_carousel.add_item(mirror_front_and_monitor)

printed_mirror_design_group.add_content(mirror_frame_design_carousel)

# Smart Mirror - Manufacturing Group
mirror_manufacturing_group = Proj.Content_group(heading="Mirror Manufacturing")

mirror_manufacturing_carousel = Proj.Carousel_obj("Mirror_Manufacturing")
mirror_frame_first_print = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52723297712_51f774acff_b.jpg", desc="First Print For the Mirror Build!")
mirror_print_rear_view1_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52744938228_4e0379b6f7_b.jpg", desc="Rear Section Piece")
mirror_insert_install_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744697279_bde64e339f_b.jpg", desc="Process of inserting frame inserts.")
mirror_sections_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744939028_b3a429ecfa_b.jpg", desc="Finished Front Frame Sections")
mirror_LED_seats = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744938623_fd79014197_b.jpg", desc="Mirror LED Seats")

mirror_manufacturing_carousel.add_item(mirror_frame_first_print)
mirror_manufacturing_carousel.add_item(mirror_print_rear_view1_img)
mirror_manufacturing_carousel.add_item(mirror_insert_install_img)
mirror_manufacturing_carousel.add_item(mirror_sections_img)
mirror_manufacturing_carousel.add_item(mirror_LED_seats)

mirror_manufacturing_group.add_content(mirror_manufacturing_carousel)

# Smart Mirror - Software Group
mirror_software_group = Proj.Content_group(heading="Mirror Software")

mirror_software_carousel = Proj.Carousel_obj("Mirror_Software_Carousel")
mirror_software_hero_img = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52743904582_b1c9842672_b.jpg", desc="Mirror Electronics and Frame Mid Finished. Time to create the software")
mirror_monitor_test = Proj.Carousel_Item(content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/3D_Printed_Mirror/Mirror_Monitor_test.gif", desc="Mirror Monitor Test")
mirror_ambient_lighting = Proj.Carousel_Item(content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/3D_Printed_Mirror/Ambient_Lighting_Test.gif", desc="Intial Test of the Ambient Lighting")

mirror_software_carousel.add_item(mirror_monitor_test)
mirror_software_carousel.add_item(mirror_software_hero_img)
mirror_software_carousel.add_item(mirror_ambient_lighting)

mirror_software_group.add_content(mirror_software_carousel)


# Smart Mirror - Hardware
mirror_hardware_group = Proj.Content_group(heading="Mirror Hardware")
mirror_hardware_carousel = Proj.Carousel_obj("Mirror_Hardware_Carousel")
mirror_hardware_carousel_hero = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744840285_d7abf50270_b.jpg", desc="Mirror Hardware")
mirror_accel_sensor_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744910853_dd3edf8757_b.jpg", desc="Accelerometer Sensor")
mirror_microphone_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744911473_79c7d0912a_b.jpg", desc="Microphone Sensor") # left off here..
mirror_camera_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744911898_cef36291cf_b.jpg", desc="Camera Sensor")
mirror_led_bottom_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744672039_54ea56c7f5_b.jpg", desc="Ambient Lighting - LED Array Bottom")
mirror_led_top_img = Proj.Carousel_Item("https://live.staticflickr.com/65535/52744839695_23d761315d_b.jpg", desc="Ambient Lighting - LED Array Top")
mirror_electronics_test = Proj.Carousel_Item("https://live.staticflickr.com/65535/52723295407_f5481a89ee_b.jpg", desc="Intial Testing of Mirror Electronics")

mirror_hardware_carousel.add_item(mirror_hardware_carousel_hero)
mirror_hardware_carousel.add_item(mirror_accel_sensor_img)
mirror_hardware_carousel.add_item(mirror_microphone_img)
mirror_hardware_carousel.add_item(mirror_camera_img)
mirror_hardware_carousel.add_item(mirror_led_bottom_img)
mirror_hardware_carousel.add_item(mirror_led_top_img)
mirror_hardware_carousel.add_item(mirror_electronics_test)

mirror_hardware_group.add_content(mirror_hardware_carousel)

#Smart Mirror - Build
mirror_build_group = Proj.Content_group(heading="Mirror Build")
mirror_build_carousel = Proj.Carousel_obj(content_title="Mirror_Build_Carousel")
mirror_build_mid_sections = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52723298062_75ec0447c4_b.jpg", desc="Complete Mirror Mid Sections")
mirror_build_front_sections = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724230780_0fa5f4053e_b.jpg", desc="Complete Mirror Front Sections")
mirror_build_top_corner_fitment = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724079699_84f0058846_b.jpg", desc="Mirror Top Left Corner Fitment")
mirror_build_bottom_corner_fitment = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724228765_677c494728_b.jpg", desc="Mirror Bottom Corner Fitment")
mirror_front_adhesive_sitting = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52723823976_bb74025321_b.jpg", desc="Front Section Adhesion Support")
complete_front_section_adhesive_sitting = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724079009_83e6cb5971_b.jpg", desc="Complete Front Section Adhesion Sitting for 20 min.")
cured_front_section = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724230040_f31af4d849_b.jpg", desc="Front Section Cured")
cured_front_section_rear = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724298308_327c07a157_b.jpg", desc="Front Section - Rear Cured")
printed_front_section_mirror_fit = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724078464_fc1fb21fc1_b.jpg",desc="Front Section with fitment of mirror.")
half_mid_section_install = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724078319_c11779602e_b.jpg", desc="Half Mid Section Installed.")
mirror_electronics_install = Proj.Carousel_Item(content_url="https://live.staticflickr.com/65535/52724228950_af67a84043_b.jpg", desc="Installing Electronics to prepare for mirror software development.")

mirror_build_carousel.add_item(mirror_build_mid_sections)
mirror_build_carousel.add_item(mirror_build_front_sections)
mirror_build_carousel.add_item(mirror_build_top_corner_fitment)
mirror_build_carousel.add_item(mirror_build_bottom_corner_fitment)
mirror_build_carousel.add_item(mirror_front_adhesive_sitting)
mirror_build_carousel.add_item(complete_front_section_adhesive_sitting)
mirror_build_carousel.add_item(cured_front_section)
mirror_build_carousel.add_item(cured_front_section_rear)
mirror_build_carousel.add_item(printed_front_section_mirror_fit)
mirror_build_carousel.add_item(half_mid_section_install)
mirror_build_carousel.add_item(mirror_electronics_install)

mirror_build_group.add_content(mirror_build_carousel)

printed_smart_mirror_proj.add_content(printed_mirror_header_group)
printed_smart_mirror_proj.add_content(printed_mirror_design_group)
printed_smart_mirror_proj.add_content(mirror_manufacturing_group)
printed_smart_mirror_proj.add_content(mirror_build_group)
printed_smart_mirror_proj.add_content(mirror_hardware_group)
printed_smart_mirror_proj.add_content(mirror_software_group)


#3D Printing

# GNSS

# Electric Bike Project
electric_bikes_proj =  Proj.Project_obj("Electric-Bikes", "multiple scrapy working ebike builds. with the intentions of being a prototype. while we are currently working on the design of an offroad frame.","2023-2024") # add thumbnail later
ebike_vid = Proj.proj_content_obj(Proj.proj_content_type.VIDEO,"E-Bike Build Video","https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/videos/Off_road_Ebike_Build.mp4",Proj.content_position.CENTER)
ebike_vid_group = Proj.Content_group("E-Bike Build Vid")
ebike_vid_group.add_content(ebike_vid)
electric_bikes_proj.add_content(ebike_vid)

# keep this section at the bottom of the file
all_projects.append(printed_smart_mirror_proj)
all_projects.append(blast_up_proj)
all_projects.append(super_cube_proj)
all_projects.append(teaching_proj)
all_projects.append(EMP_proj)
all_projects.append(robotics_competing)
all_projects.append(electric_bikes_proj)



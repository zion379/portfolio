from modules import project as Proj

all_projects: list[Proj.Project_obj] = []

#EMP Project
EMP_proj = Proj.Project_obj("EMP", "This experiment was done to see if electromagnetic waves of a diffrent frequency of light could trigger photo synthesis.")
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
teaching_proj = Proj.Project_obj("Instructor", "Instructor for Digipen Instituite of technology.")
teaching_desc = Proj.proj_content_obj(Proj.proj_content_type.TEXT, text_content="Taught in person at two school and online classes.")
teaching_proj.add_content(teaching_desc)

#Game Dev
#Super Cube Game
super_cube_proj = Proj.Project_obj("SuperCube", "A hypercasual game where levels are dynamically generated based on how far the player makes it throug the game.")
hero_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/super_cube_game/super_cube_gif.gif")
super_cube_proj.add_content(hero_gif)

#Blast Up Game
blast_up_proj = Proj.Project_obj("Blast-Up", "A hypercasual game where players protect a rocket ship as aireborne obstacles try to bring the ship down. ")
hero_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/blast_up_game/Blast_up_game.gif")
blast_up_proj.add_content(hero_gif)

#App Dev

#Robotics
robotics_competing = Proj.Project_obj("competitive-robotics", "During Middle/Highschool I enoyed being a contributing member to the competitve robotics clubs. particpating in FTC events in middle school and FRC events in highschool.")
hero_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/highschool-robotics-team-group.PNG", position=Proj.content_position.RIGHT)


team_info_group = Proj.Content_group()
team_bot_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/robotics_3588_robot.JPG")
team_bot_side_view = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/team_bot_side_view.JPG")
team_info_group.add_content(team_bot_side_view)
team_info_group.add_content(team_bot_img)

pre_comp_group = Proj.Content_group(heading="Pre-Competition")
robot_pre_comp_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/competitive%20robotics/robot_pre_competition.gif")
pre_comp_group.add_content(robot_pre_comp_gif)

pneumatic_system_group = Proj.Content_group(heading="Robot pneumatic system experimentaiton")
pneumatic_system_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/experimenting_bot_pneumatic_system.gif")
pneumatic_sys_desc = Proj.proj_content_obj(Proj.proj_content_type.TEXT, text_content="Our Team bot Utilized pneumatic controlled actuators. We wanted to test if we were able to use this mechanism to pick up gears. During the competition the robot will have the ability to transport gears as part of the objective to score point during a competitive match.")
pneumatic_system_group.add_content(pneumatic_system_gif)
pneumatic_system_group.add_content(pneumatic_sys_desc)


bot_climbing_mechanism_group = Proj.Content_group(heading="Climbing Mechanism")
bot_climbing_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/competitive_robotics/bot_climbing_test.gif")
bot_climbing_mechanism_group.add_content(bot_climbing_gif)

robotics_competing.add_content(hero_img)
robotics_competing.add_content(team_info_group)
robotics_competing.add_content(pre_comp_group)
robotics_competing.add_content(pneumatic_system_group)
robotics_competing.add_content(bot_climbing_mechanism_group)



#3D Printing
all_projects.append(blast_up_proj)
all_projects.append(super_cube_proj)
all_projects.append(teaching_proj)
all_projects.append(EMP_proj)
all_projects.append(robotics_competing)

from modules import project as Proj

all_projects: list[Proj.Project_obj] = []

#EMP Project
EMP_proj = Proj.Project_obj("EMP", "This experiment was done to see if electromagnetic waves of a diffrent frequency of light could trigger photo synthesis.")
hero_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://live.staticflickr.com/65535/52798783778_0624d7202e_b.jpg")
circuit_view_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/EMP_Circuit_View.JPG")
sparkgap_gif = Proj.proj_content_obj(Proj.proj_content_type.GIF, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/gifs/Photon_EMP/spark_gap_magnified.gif")
photon_emp_test_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/photon_emp_test.jpeg")
emp_test_results = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/photon_emp_test_results.jpeg")
carbon_deoxide_results_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE,content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/carbon_deoxide_results.jpeg")
dissolved_oxygen_scale_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/dissolved_oxygen_scale.jpeg")

EMP_proj.add_content(hero_img)
EMP_proj.add_content(circuit_view_img)
EMP_proj.add_content(sparkgap_gif)
EMP_proj.add_content(photon_emp_test_img)
EMP_proj.add_content(emp_test_results)
EMP_proj.add_content(dissolved_oxygen_scale_img)
EMP_proj.add_content(carbon_deoxide_results_img)


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
hero_img = Proj.proj_content_obj(Proj.proj_content_type.IMAGE, content_url="https://zionjohnsonportfolio.nyc3.cdn.digitaloceanspaces.com/images/Photon_EMP/highschool-robotics-team-group.PNG")

robotics_competing.add_content(hero_img)

#3D Printing
all_projects.append(blast_up_proj)
all_projects.append(super_cube_proj)
all_projects.append(teaching_proj)
all_projects.append(EMP_proj)
all_projects.append(robotics_competing)

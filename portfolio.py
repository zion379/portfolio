from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    intro_header_text = "Hello and welcome to my electrical and software engineering portfolio! My name is Zion,"
    intro_paragraph_text = "and I am a self-taught programmer and electrical engineer with a passion for teaching. Over the years, I have developed expertise in programming languages, game development, and electronics. As a K12 instructor, I have had the opportunity to teach various subjects, including circuit building and micro-controller programming, on behalf of a technical college focused on STEM higher education. In this portfolio, you will find a collection of my projects, ranging from simple circuits to complex software programs, that showcase my technical skills and creativity. I hope that this portfolio serves as an inspiration for young students and aspiring engineers, and that it highlights the exciting possibilities of pursuing a career in electrical and software engineering."
    return render_template('index.html', intro_header_text=intro_header_text, intro_paragraph_text=intro_paragraph_text)

@app.route('/skills')
def skills():
    my_skills = ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'CAD', 'Embedded Software', 'Embedded Hardware', 'C Programming', 'Electronics', 'Game Development', 'App Develoment']
    return render_template('skills.html', skills=my_skills)

@app.route('/projects')
def projects():
    page_title = "My Projects"
    project_img_urls = ["https://live.staticflickr.com/65535/52727321385_a748270f52_b.jpg", "https://live.staticflickr.com/65535/52798783778_0624d7202e_b.jpg"]
    project_titles = ["3D Printed Smart Mirror","EMP Device"]
    project_Descriptions = ["This Mirrors casing is entierly 3D-printed making the mirror exceptionaly light. this mirror features include Chat-GPT, Augment Reality, Sound System, and More!","Using EMP to Stimulate Photosynthesis"]
    project_Link = ["/projects/3dprintedsmartmirror","/"]
    return render_template('projects.html', page_title=page_title, project_titles=project_titles, project_Descriptions=project_Descriptions, project_Link=project_Link, project_img_urls=project_img_urls)

#testing
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/projects/3dprintedsmartmirror')
def smartMirror():
    project_title = "3D Printed Smart Mirror V1"
    rendered_photos = ["https://live.staticflickr.com/65535/52727321385_a748270f52_b.jpg", "https://live.staticflickr.com/65535/52726903686_45fd1ceca9_b.jpg"]
    mirror_section_titles = ["Mirror Frame: Front Section - Top View","Mirror Frame: Front Section - Rear View","Mirror Frame: Mid Section - Rear View","Mirror Frame: Mid Section - Top View "]
    mirror_section_images = ["https://live.staticflickr.com/65535/52727162194_d0f8b5cc21_b.jpg", "https://live.staticflickr.com/65535/52727385888_981ba69fcf_b.jpg", "https://live.staticflickr.com/65535/52726903611_db4f470b44_b.jpg", "https://live.staticflickr.com/65535/52727162129_6fa00fd814_b.jpg"]
    manufac_images = ["https://live.staticflickr.com/65535/52744938228_4e0379b6f7_b.jpg", "https://live.staticflickr.com/65535/52724299978_8e50583315_b.jpg"]
    software_images = ["https://live.staticflickr.com/65535/52743904582_b1c9842672_b.jpg", "https://live.staticflickr.com/65535/52724299978_8e50583315_b.jpg"]
    return render_template('smart_mirror_project.html', project_title=project_title, rendered_photos=rendered_photos, mirror_section_titles=mirror_section_titles, mirror_section_images=mirror_section_images, manufac_images=manufac_images, software_images=software_images)

#app.run(debug=True)

if __name__ == '__main__':
    app.run()


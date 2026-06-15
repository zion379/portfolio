from flask import Flask, render_template, redirect, request, url_for
from openai import OpenAI
import os
from dotenv import load_dotenv
from modules import projects_content
from modules import project as Proj
from modules.item_tracker_app import item_tracker

load_dotenv()

app = Flask(__name__)
app.jinja_env.globals['asset_url'] = os.getenv('R2_PUBLIC_URL', '')

try:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
except Exception:
    client = None


@app.route('/')
def index():
    intro_header_text = "Hello and welcome to my electrical and software engineering portfolio! My name is Zion,"
    intro_paragraph_text = "and I am a self-taught programmer and electrical engineer with a passion for teaching. Over the years, I have developed expertise in programming languages, game development, and electronics. As a K12 instructor, I have had the opportunity to teach various subjects, including circuit building and micro-controller programming, on behalf of a technical college focused on STEM higher education. In this portfolio, you will find a collection of my projects, ranging from simple circuits to complex software programs, that showcase my technical skills and creativity. I hope that this portfolio serves as an inspiration for young students and aspiring engineers, and that it highlights the exciting possibilities of pursuing a career in electrical and software engineering."
    return render_template('index.html', intro_header_text=intro_header_text, intro_paragraph_text=intro_paragraph_text)

@app.route('/skills')
def skills():
    my_skills = ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'Java', 'CAD', 'Embedded Software', 'Embedded Hardware', 'C Programming', 'Electronics', 'Game Development', 'App Develoment']
    return render_template('skills.html', skills=my_skills)

@app.route('/projects')
def project():
    page_title = "My Projects"
    project_img_urls = ["https://live.staticflickr.com/65535/52727321385_a748270f52_b.jpg"]
    project_titles = ["3D Printed Smart Mirror"]
    project_Descriptions = ["This Mirrors casing is entierly 3D-printed making the mirror exceptionaly light. this mirror features include Chat-GPT, Augment Reality, Sound System, and More!"]
    project_Link = ["/projects/3dprintedsmartmirror"]

    all_projects = projects_content.all_projects
    return render_template('projects.html', all_projects=all_projects,page_title=page_title, project_titles=project_titles, project_Descriptions=project_Descriptions, project_Link=project_Link, project_img_urls=project_img_urls)


@app.route('/project_view/<project_name>')
def project_view(project_name: str):
    for project in projects_content.all_projects:
        if project.project_name.lower() == project_name.lower():
            if project.project_link:
                return redirect(project.project_link)
            return render_template('project_view.html', project=project)
    return render_template('project_view.html', project=None)

@app.route('/projects/high-altitude-media')
def high_altitude_media():
    return render_template('high_altitude_media_project.html')

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/projects/3dprintedsmartmirror')
def smartMirror():
    project_title = "3D PRINTED SMART MIRROR V1"
    rendered_photos = ["https://live.staticflickr.com/65535/52727321385_a748270f52_b.jpg", "https://live.staticflickr.com/65535/52726903686_45fd1ceca9_b.jpg"]
    mirror_section_titles = ["Front Section: Top View - Mirror Frame","Front Section: Rear View - Mirror Frame","Mid Section: Rear View - Mirror Frame","Mid Section : Top View - Mirror Frame", "Rear Section : Isometric View - Mirror Frame"]
    mirror_section_images = ["https://live.staticflickr.com/65535/52727162194_d0f8b5cc21_b.jpg", "https://live.staticflickr.com/65535/52727385888_981ba69fcf_b.jpg", "https://live.staticflickr.com/65535/52726903611_db4f470b44_b.jpg", "https://live.staticflickr.com/65535/52727162129_6fa00fd814_b.jpg", "https://live.staticflickr.com/65535/52726384467_e76e8852d3_b.jpg"]
    manufac_images = ["https://live.staticflickr.com/65535/52744938228_4e0379b6f7_b.jpg", "https://live.staticflickr.com/65535/52724299978_8e50583315_b.jpg"]
    software_images = ["https://live.staticflickr.com/65535/52743904582_b1c9842672_b.jpg", "https://live.staticflickr.com/65535/52724299978_8e50583315_b.jpg"]
    return render_template('smart_mirror_project.html', project_title=project_title, rendered_photos=rendered_photos, mirror_section_titles=mirror_section_titles, mirror_section_images=mirror_section_images, manufac_images=manufac_images, software_images=software_images)

@app.route('/smart-mirror-chatbot', methods=("GET", "POST"))
def MirrorCompletions():
    result = None
    if request.method == "POST":
        if client is None:
            result = "OpenAI API key not configured. Set OPENAI_API_KEY in your .env file."
        else:
            usr_response = request.form["userinput"]
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": usr_response}]
            )
            result = response.choices[0].message.content
    return render_template("gpt_completions.html", result=result)

@app.route('/smart-mirror-chat')
def MirrorChat():
    return render_template("gpt_completions.html")

# experimental routes
@app.route('/car-tracker-stream', methods=["GET"])
def car_tracker_stream():
    with open('static/Experimental/gps_stream.txt', "r") as file:
        contents = file.read()
    return contents


@app.route('/update-tracker-stream/<stream>', methods=['GET','POST'])
def update_tracker_stream(stream:str):
    with open('static/Experimental/gps_stream.txt', "w") as file:
        file.write(stream)
    return stream

@app.route('/car-tracker-app', methods=['GET'])
def car_tracker_app():
    try:
        with open('static/Experimental/gps_stream.txt', "r") as file:
            contents = file.read()

        opening_brackets_list = []
        closing_brackets_list = []

        char_index = 0
        for c in contents:
            if c == '[':
                opening_brackets_list.append(char_index)
            if c == ']':
                closing_brackets_list.append(char_index)
            char_index += 1

        packet_1 = contents[opening_brackets_list[1]:closing_brackets_list[0] + 1]
        packet_2 = contents[opening_brackets_list[2]:closing_brackets_list[1] + 1]

        packet_1 = packet_1[1:len(packet_1)-1]
        packet_2 = packet_2[1:len(packet_1)-1]

        packet_1_data = [str(x).replace("'", "") for x in packet_1.split(",")]
        packet_2_data = [str(x).replace("'", "") for x in packet_2.split(",")]

        lat = packet_1_data[0]
        long = packet_1_data[1]
        altitude_miles = packet_1_data[2]
        course_deg = packet_1_data[3]
        mph = packet_1_data[4]
        month = packet_1_data[5]
        day = packet_1_data[6]
        year = packet_1_data[7]
        altitude_f = packet_2_data[0]
        altitude_m = packet_2_data[1]
        hour = packet_2_data[2]
        min = packet_2_data[3]
        sec = packet_2_data[4]
        sat_v = packet_2_data[6]

        return render_template('car_tracker_app.html', lat=lat, long=long,
            altitude_miles=altitude_miles, course_deg=course_deg, mph=mph,
            month=month, day=day, year=year, altitude_f=altitude_f,
            altitude_m=altitude_m, hour=hour, min=min, sec=sec, sat_v=sat_v)

    except (FileNotFoundError, IndexError, ValueError) as e:
        return render_template('car_tracker_app.html', error=str(e),
            lat=0, long=0, altitude_miles=0, course_deg=0, mph=0,
            month=0, day=0, year=0, altitude_f=0, altitude_m=0,
            hour=0, min=0, sec=0, sat_v=0)


item_tracker_app = item_tracker.Item_tracker_manager()

@app.route('/item-tracker', methods=["GET"])
def item_tracker_route():
    return render_template('item_tracker_app/item_tracker.html', tracked_items=item_tracker_app.items)

@app.route('/item-tracker-increase-item-count/<item_name>', methods=['GET', 'POST'])
def item_tracker_increase_item_count(item_name:str):
    item_tracker_app.increase_item_count(item_name, "Anonymous")
    return item_name

@app.route('/item-tracker-decrease-item-count/<item_name>', methods=['GET', 'POST'])
def item_tracker_decrease_item_count(item_name:str):
    item_tracker_app.decrease_item_count(item_name, "Anonymous")
    return item_name

@app.route('/item-tracker-config', methods=["GET"])
def item_tracker_config():
    return render_template('item_tracker_app/item_tracker_config.html', tracked_items=item_tracker_app.items)

@app.route('/item-tracker-config/edit-name/', methods=["GET", "POST"])
def item_tracker_edit_item_name():
    item = request.args.get('item')
    new_name = request.args.get('name')
    item_tracker_app.update_item_name(item, new_name)
    return f'updated {item} name to {new_name}'

@app.route('/item-tracker-config/set-count/', methods=["POST", "GET"])
def item_tracker_set_count():
    count = request.args.get('count')
    item_name = request.args.get('item')
    item_tracker_app.set_item_count(item_name, count)
    return f'updated {item_name} count to {count}'

@app.route('/item-tracker-config/set-goal/', methods=["POST", "GET"])
def item_tracker_set_goal():
    goal = request.args.get('goal')
    item_name = request.args.get('item')
    item_tracker_app.set_item_goal(item_name, goal)
    return f'updated {item_name} goal to {goal}'

@app.route('/item-tracker-config/set-note/', methods=["POST", "GET"])
def item_tracker_set_note():
    note = request.args.get('notes')
    item_name = request.args.get('item')
    item_tracker_app.set_item_note(item_name, note)
    return f'updated {item_name} note to {note}'

@app.route('/item-tracker-config/delete-item/', methods=["POST", "GET"])
def item_tracker_delete_item():
    item_name = request.args.get('item')
    item_tracker_app.remove_item(item_name)
    return f'deleted {item_name}'

@app.route('/item-tracker-config/create-item/', methods=["POST", "GET"])
def item_tracker_create_item():
    item_name = request.args.get('item')
    item_tracker_app.create_new_item(item_name)
    return f'created {item_name}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

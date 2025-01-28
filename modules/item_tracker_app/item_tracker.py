from datetime import datetime

class track_item:
    def __init__(self, item_name: str):
        self.item_name:str = item_name
        self.item_count:int = 0
        self.item_notes:str = ""
        self.goal: int = 0

    def update_item_goal(self, new_goal: int):
        self.goal = new_goal

    def increase_item_count(self):
        self.item_count += 1

    def decrease_item_count(self):
        self.item_count -= 1

    def add_item_note(self, note: str):
        self.item_notes = note

    def set_count(self, count:int):
        self.item_count = count


class item_update_log:
    
    def __init__(self, item:track_item, tech: str , date: str):
        current_time = datetime.now()
        self.item_name:str = item.item_name
        self.tech: str = tech
        self.date: str = current_time.date()


class item_log:
    #save update log
    def save_item_update(update_log: item_update_log):
        # check if content exist
        contents:str

        with open("static/Experimental/item_tracker_app/item_update_log.txt", "r") as doc:
            contents = doc.read()

        with open("static/Experimental/item_tracker_app/item_update_log.txt", "w") as doc:
            contents += f"{update_log.item_name} Updated by {update_log.tech} - {update_log.date} \n"
            doc.write(contents)

    #save count of tracked items
    def save_items_count(items_data:list[track_item]):
        current_time = datetime.now()
        items_count_log_output: str = f"Updated: {current_time.date} {current_time.time}"

        # get and save date

        for item_data in items_data:
            items_count_log_output += f"{item_data.item_name} count: {item_data.item_count} notes: {item_data.item_notes} goal: {item_data.goal} \n"
        

        # update items count log
        with open("static/Experimental/item_tracker_app/items_count.txt", "w") as doc:
            contents = items_count_log_output
            doc.write(contents)

class Item_tracker_manager:

    def __init__(self):
        self.items:list[track_item] = []
        pass

    def create_new_item(self, item_name:str):
        item_log.save_item_update
        new_item = track_item(item_name)
        self.items.append(new_item)
        
    def remove_item(self, item_name:str):
        index: int = 0
        for item in self.items:
            if item.item_name == item_name:
                self.items.pop(index)
            index += 1

    def increase_item_count(self, item_name:str, tech: str):
        current_time = datetime.now()
        for item in self.items:
            if item.item_name == item_name:
                item.increase_item_count()
                update_log = item_update_log(item, tech, current_time.date)
                item_log.save_item_update(update_log)

    def decrease_item_count(self, item_name:str,  tech: str):
        current_time = datetime.now()
        for item in self.items:
            if item.item_name == item_name:
                if item.item_count <= 0:
                    item.set_count(0)
                else:
                    item.decrease_item_count()
                    update_log = item_update_log(item, tech, current_time.time)
                    item_log.save_item_update(update_log)

    def set_item_count(self, item_name:str, value:int):
        for item in self.items:
            if item.item_name == item_name:
                item.set_count(value)

    def save_items_count_to_file(self):
        item_log.save_items_count(self.items)

    def get_tracked_items(self):
        return self.items
    
    def set_item_note(self, item_name:str, note:str):
        for item in self.items:
            if item.item_name == item_name:
                item.add_item_note(note)

    def set_item_goal(self, item_name:str ,item_goal:int):
        for item in self.items:
            if item.item_name == item_name:
                item.update_item_goal(item_goal)

    def update_item_name(self, item_name:str, new_name:str):
        for item in self.items:
            if item.item_name == item_name:
                item.item_name = new_name

        
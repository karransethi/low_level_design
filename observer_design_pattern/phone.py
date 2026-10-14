from observer import Observer

class Phone(Observer):
    def update_weather(self, temp):
        print(f'Phone temp updated to {temp}')
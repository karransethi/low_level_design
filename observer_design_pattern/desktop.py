from observer import Observer

class Desktop(Observer):
    def update_weather(self, temp):
        print(f'Desktop temp updated to {temp}')
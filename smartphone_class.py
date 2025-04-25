class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.power_on = False
        self.current_app = None
    
    def power_toggle(self):
        self.power_on = not self.power_on
        status = "on" if self.power_on else "off"
        print(f"{self.brand} {self.model} is now {status}")
    
    def open_app(self, app_name):
        if not self.power_on:
            print("Please turn on the phone first!")
            return
        
        self.current_app = app_name
        print(f"Opening {app_name}...")
    
    def close_app(self):
        if self.current_app:
            print(f"Closing {self.current_app}...")
            self.current_app = None
        else:
            print("No app is currently open!")
    
    def check_storage(self):
        print(f"Storage available: {self.storage_gb}GB")
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage_gb}GB, {self.battery_mah}mAh)"


# Inheritance example - GamingPhone extends Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, gpu_model, cooling_system):
        super().__init__(brand, model, storage_gb, battery_mah)
        self.gpu_model = gpu_model
        self.cooling_system = cooling_system
        self.game_mode = False
    
    def toggle_game_mode(self):
        self.game_mode = not self.game_mode
        status = "enabled" if self.game_mode else "disabled"
        print(f"Game mode {status}. GPU {self.gpu_model} is {'boosted' if self.game_mode else 'normal'}.")
    
    def open_app(self, app_name):
        super().open_app(app_name)
        if "game" in app_name.lower() and self.game_mode:
            print(f"Optimizing {app_name} for gaming performance!")
    
    def __str__(self):
        return f"{super().__str__()} | GPU: {self.gpu_model} | Cooling: {self.cooling_system}"


# Testing the classes
print("=== Regular Smartphone ===")
phone1 = Smartphone("Apple", "iPhone 15", 128, 4000)
phone1.power_toggle()
phone1.open_app("Camera")
phone1.close_app()
print(phone1)

print("\n=== Gaming Phone ===")
gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 256, 6000, "Adreno 740", "Vapor Chamber")
gaming_phone.power_toggle()
gaming_phone.toggle_game_mode()
gaming_phone.open_app("Genshin Impact")
print(gaming_phone)
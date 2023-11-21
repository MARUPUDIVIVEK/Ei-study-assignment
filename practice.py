from datetime import datetime, time

class Observer:
    def update(self, message):
        pass

class DeviceObserver(Observer):
    def __init__(self, device):
        self.device = device

    def update(self, message):
        print(f"Update for {self.device}: {message}")

class DeviceFactory:
    def create_device(self, device_type, device_id):
        pass

class LightFactory(DeviceFactory):
    def create_device(self, device_id):
        return Light(device_id)

class ThermostatFactory(DeviceFactory):
    def create_device(self, device_id):
        return Thermostat(device_id)

class DoorLockFactory(DeviceFactory):
    def create_device(self, device_id):
        return DoorLock(device_id)

class DeviceProxy:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        print(f"Turning on {self.device}")
        self.device.turn_on()

    def turn_off(self):
        print(f"Turning off {self.device}")
        self.device.turn_off()

    def set_schedule(self, time, action):
        print(f"Setting schedule for {self.device} at {time}: {action}")

    def set_temperature(self, temperature):
        print(f"Setting temperature for {self.device} to {temperature}")
        self.device.set_temperature(temperature)

    # Corrected: Added lock and unlock methods
    def lock(self):
        print(f"Locking {self.device}")
        self.device.lock()

    def unlock(self):
        print(f"Unlocking {self.device}")
        self.device.unlock()

class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

class Light(Device):
    def __str__(self):
        return f"Light {self.device_id}"

    def turn_on(self):
        self.notify_observers("Light is On")

    def turn_off(self):
        self.notify_observers("Light is Off")

class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 70

    def __str__(self):
        return f"Thermostat {self.device_id}"

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers(f"Thermostat is set to {self.temperature} degrees")

class DoorLock(Device):
    def __str__(self):
        return f"Door Lock {self.device_id}"

    def lock(self):
        self.notify_observers("Door is Locked")

    def unlock(self):
        self.notify_observers("Door is Unlocked")

class SmartHomeSystem:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def execute_command(self, command):
        exec(command)

if __name__ == "__main__":
    smart_home = SmartHomeSystem()

    light_factory = LightFactory()
    thermostat_factory = ThermostatFactory()
    door_lock_factory = DoorLockFactory()

    light = light_factory.create_device(1)
    thermostat = thermostat_factory.create_device(2)
    door_lock = door_lock_factory.create_device(3)

    light.add_observer(DeviceObserver(light))
    thermostat.add_observer(DeviceObserver(thermostat))
    door_lock.add_observer(DeviceObserver(door_lock))

    smart_home.add_device(DeviceProxy(light))
    smart_home.add_device(DeviceProxy(thermostat))
    smart_home.add_device(DeviceProxy(door_lock))

    smart_home.execute_command("smart_home.devices[0].turn_on()")
    smart_home.execute_command("smart_home.devices[1].set_temperature(75)")
    smart_home.execute_command("smart_home.devices[2].lock()")

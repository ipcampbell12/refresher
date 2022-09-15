class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        # assume it's connected
        self.connected = True

    def __str__(self):
        return f"{self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


printer = Device("Printer", "USB")
printer.disconnect()
print(printer)

# creating class that inherits from Device - uses all same methods


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # calls init method of parent class
        super().__init__(name, connected_by)
        self.capcity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return (f"{super().__str__()} ({self.remaining_pages} pages remaining)")

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Pring {pages} pages")
        self.remaining_pages -= pages


printer2 = Printer("Printer2", "USB", 500)
printer2.print(35)
print(printer2)

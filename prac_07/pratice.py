class Monitor:
    """Represent a computer monitor with model, width and height."""

    def __init__(self, model, width, height):
        """Initialise a Monitor with model, width and height."""
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self):
        """Return the resolution as a (width, height) tuple."""
        return self.width, self.height

    def get_total_pixels(self):
        """Return the total number of pixels."""
        return self.width * self.height

    def __eq__(self, other):
        """Return True if monitors have the same width and height."""
        if isinstance(other, Monitor):
            return (self.width, self.height) == (other.width, other.height)
        return False

monitor1 = Monitor("Dell-U2412M", 1920, 1200)

print(monitor1.get_resolution())
print(monitor1.get_total_pixels())


monitor1 = Monitor("Dell-U2412M", 1920, 1200)
monitor2 = Monitor("LG-24MP88", 1920, 1200)
monitor3 = Monitor("Samsung-27", 2560, 1440)

print(monitor1 == monitor2)   # True (same width & height)
print(monitor2 == monitor3)   # False

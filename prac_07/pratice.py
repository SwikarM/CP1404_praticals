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


monitor1 = Monitor("Dell-U2412M", 1920, 1200)

print(monitor1.get_resolution())
print(monitor1.get_total_pixels())
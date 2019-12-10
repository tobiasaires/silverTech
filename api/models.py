from django.db import models

# Create your models here.


class Processor(models.Model):

    processors_options = [
        ("Intel Core i5", "Intel Core i5"),
        ("Intel Core i7", "Intel Core i7"),
        ("AMD Athlon", "AMD Athlon"),
        ("AMD Ryzen 7", "AMD Ryzen 7")]
    processors_brand_options = [
        ("Intel", "Intel"),
        ("AMD", "AMD")
    ]

    processor = models.CharField(
        max_length=50, choices=processors_options)
    processor_brand = models.CharField(
        max_length=20, choices=processors_brand_options)

    def __str__(self):
        return f"{self.processor}"


class Memory(models.Model):
    ram_brand_options = [("Hiper X", "Hiper X")]

    ram_size_options = [(4, "4"), (8, "8"),
                        (16, "16"), (32, "32"), (64, "64")]

    ram_brand = models.CharField(max_length=25, choices=ram_brand_options)
    ram_size = models.PositiveIntegerField(choices=ram_size_options)

    def __str__(self):
        return f"{self.ram_brand} {self.ram_size}GB"


class VideoBoard(models.Model):
    video_board_options = [
        ("Gigabyte Geforce GTX 1060 6GB", "Gigabyte Geforce GTX 1060 6GB"),
        ("PNY RTX 2060 6GB", "PNY RTX 2060 6GB"),
        ("Radeon RX 580 8GB", "Radeon RX 580 8GB"),
    ]

    video_board = models.CharField(
        max_length=100, choices=video_board_options
    )

    def __str__(self):
        return f"{self.video_board}"


class MotherBoard(models.Model):

    mother_board_options = [
        ("Asus Prime", "Asus Prime"),
        ("Gigabyte", "Gigabyte"),
        ("ASRock Fatal", "ASRock Fatal"),
    ]

    processors_options = [
        ("Intel", "Intel"),
        ("AMD", "AMD"),
        ("Ambos", "Ambos")
    ]

    ram_slots_options = [
        (2, "2"),
        (4, "4")
    ]

    max_ram_options = [
        (16, "16"),
        (64, "64")
    ]

    mother_board = models.CharField(
        max_length=25, choices=mother_board_options)
    processor = models.CharField(max_length=25, choices=processors_options)
    ram_slots = models.PositiveIntegerField(choices=ram_slots_options)
    ram_max_size = models.PositiveIntegerField(choices=max_ram_options)
    has_integrated_video = models.BooleanField()

    def __str__(self):
        return f"{self.mother_board}"

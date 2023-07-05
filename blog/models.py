from django.db import models

# Create your models here.
from datetime import date, datetime

from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.email}"


class Entry(models.Model):
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    big_integer_field = models.BigIntegerField(default=12)
    # big_auto_field = models.BigAutoField()
    # binary_field = models.BinaryField(default=0)

    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, "Freshman"),
        (SOPHOMORE, "Sophomore"),
        (JUNIOR, "Junior"),
        (SENIOR, "Senior"),
        (GRADUATE, "Graduate"),
    ]
    MEDIA_CHOICES = [
        (
            "Audio",
            (
                ("vinyl", "Vinyl"),
                ("cd", "CD"),
            ),
        ),
        (
            "Video",
            (
                ("vhs", "VHS Tape"),
                ("dvd", "DVD"),
            ),
        ),
        ("unknown", "Unknown"),
    ]

    year_in_school = models.CharField(
        db_comment="Date and time when the article was published",
        help_text="just for testing help_text",
        db_index=True,
        db_tablespace="test_it",
        max_length=8,
        verbose_name="test year school",
        choices=MEDIA_CHOICES,
        # default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

    class Vehicle(models.TextChoices):
        CAR = "C"
        TRUCK = "T"
        JET_SKI = "J"

    vehicle_choice = models.CharField(max_length=2,
                                      choices=Vehicle.choices,
                                      default=Vehicle.TRUCK)
    # auto_field1 = models.AutoField()
    # big_auto_field = models.BigAutoField()


    # class MoonLandings(datetime.date, models.Choices):
    #     APOLLO_11 = 1969, 7, 20, "Apollo 11 (Eagle)"
    #     APOLLO_12 = 1969, 11, 19, "Apollo 12 (Intrepid)"
    #     APOLLO_14 = 1971, 2, 5, "Apollo 14 (Antares)"
    #     APOLLO_15 = 1971, 7, 30, "Apollo 15 (Falcon)"
    #     APOLLO_16 = 1972, 4, 21, "Apollo 16 (Orion)"
    #     APOLLO_17 = 1972, 12, 11, "Apollo 17 (Challenger)"
    #
    # moonlanding_choice = models.CharField(max_length=14,
    #                                       choices=MoonLandings.choices,
    #                                       default=MoonLandings.APOLLO_16)

    # class Answer(models.IntegerChoices):
    #     NO = 0, _("No")
    #     YES = 1, _("Yes")
    #
    #     __empty__ = _("(Unknown)")
    #
    # answer_choice = models.CharField(max_length=5,
    #                                  choices=Answer.choices,
    #                                  )

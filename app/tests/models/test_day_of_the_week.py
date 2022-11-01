"""DayOfTheWeek tests module."""


from app.models import DayOfTheWeek
from django.db.utils import DataError, IntegrityError
from django.test import TestCase
from mixer.backend.django import mixer


class DayOfTheWeekTestCase(TestCase):
    """DayOfTheWeek TestCase"""

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        day_of_the_week = mixer.blend(
            DayOfTheWeek,
            description="Saturday"
        )

        self.assertEqual(day_of_the_week.description, "Saturday")

    def test_create_model_with_invalid_data(self):
        """Create model with invalid data should raise data error."""

        too_long_description = "Lorem ipsum dolor sit amet consectetur."
        with self.assertRaises(DataError):
            mixer.blend(
                DayOfTheWeek,
                description=too_long_description
            )

    def test_create_model_with_duplicate_description(self):
        """
        Create model with duplicate description should raise integrity
        error.
        """
        mixer.blend(
            DayOfTheWeek,
            description="Sunday"
        )

        with self.assertRaises(IntegrityError):
            mixer.blend(
                DayOfTheWeek,
                description="Sunday"
            )

    def test_str_method(self):
        """Test str method of Model."""
        dotw = mixer.blend(DayOfTheWeek, description="Thursday")
        self.assertEqual(str(dotw), "Thursday")


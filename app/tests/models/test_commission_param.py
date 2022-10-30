"""DayOfTheWeek tests module."""


from app.models import CommissionParam, DayOfTheWeek
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from mixer.backend.django import mixer


class CommissionParamTestCase(TestCase):
    """CommissionParam TestCase"""

    def setUp(self) -> None:
        self.valid_min_percentage = 2.75
        self.valid_max_percentage = 15.5

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        day_of_the_week = mixer.blend(
            DayOfTheWeek,
            description="Saturday"
        )

        commission_param = mixer.blend(
            CommissionParam,
            min_percentage=self.valid_min_percentage,
            max_percentage=self.valid_max_percentage,
            day_of_the_week=day_of_the_week
        )

        self.assertEqual(
            commission_param.min_percentage,
            self.valid_min_percentage
        )
        self.assertEqual(
            commission_param.max_percentage,
            self.valid_max_percentage
        )
        self.assertEqual(
            commission_param.day_of_the_week.description,
            day_of_the_week.description
        )

    def test_create_model_with_invalid_data(self):
        """
        Create model with invalid percentage should raise ValidationError.
        """
        day_of_the_week = mixer.blend(
            DayOfTheWeek,
            description="Friday"
        )

        invalid_data = [
            'abc',
            {"invalid": "data"},
            [1, 1, 3, 5, 8],
            {2, 4, 6}
        ]

        for invalid_percentage in invalid_data:
            with self.assertRaises(ValidationError):
                mixer.blend(
                    CommissionParam,
                    min_percentage=invalid_percentage,
                    max_percentage=invalid_percentage,
                    day_of_the_week=day_of_the_week
                )

    def test_create_model_with_duplicate_day_of_the_week(self):
        """
        Create model with duplicate day_of_the_week should raise integrity
        error.
        """
        day_of_the_week = mixer.blend(
            DayOfTheWeek,
            description="Saturday"
        )

        mixer.blend(
            CommissionParam,
            min_percentage=self.valid_min_percentage,
            max_percentage=self.valid_max_percentage,
            day_of_the_week=day_of_the_week
        )

        with self.assertRaises(IntegrityError):
            mixer.blend(
                CommissionParam,
                min_percentage=self.valid_min_percentage,
                max_percentage=self.valid_max_percentage,
                day_of_the_week=day_of_the_week
            )

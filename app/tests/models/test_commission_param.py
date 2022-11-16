"""DayOfTheWeek tests module."""


from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from mixer.backend.django import mixer

from app.models import CommissionParam, DayOfTheWeek


class CommissionParamTestCase(TransactionTestCase):
    """CommissionParam TestCase"""

    def setUp(self) -> None:
        self.valid_min_percentage = Decimal(2.75)
        self.valid_max_percentage = Decimal(9.89)

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        day_of_the_week = mixer.blend(DayOfTheWeek, description="Saturday")

        commission_param = mixer.blend(
            CommissionParam,
            min_percentage=self.valid_min_percentage,
            max_percentage=self.valid_max_percentage,
            day_of_the_week=day_of_the_week,
        )

        self.assertEqual(commission_param.min_percentage, self.valid_min_percentage)
        self.assertEqual(commission_param.max_percentage, self.valid_max_percentage)
        self.assertEqual(
            commission_param.day_of_the_week.description, day_of_the_week.description
        )

    def test_create_model_with_invalid_data(self):
        """
        Create model with invalid percentage should raise ValidationError.
        """
        with self.subTest(
            "Invalid type of data for percentage values should raise exception."
        ):
            day_of_the_week = mixer.blend(DayOfTheWeek, description="Friday")
            invalid_data = ["abc", {"invalid": "data"}, [1, 1, 3, 5, 8], {2, 4, 6}]

            for invalid_percentage in invalid_data:
                with self.assertRaises(ValidationError):
                    mixer.blend(
                        CommissionParam,
                        min_percentage=invalid_percentage,
                        max_percentage=invalid_percentage,
                        day_of_the_week=day_of_the_week,
                    )

        with self.subTest(
            "Invalid range for min_percentage field should raise exception."
        ):
            invalid_min_percentage_range = Decimal(-1)

            day_of_the_week = mixer.blend(DayOfTheWeek, description="Monday")

            with self.assertRaises(IntegrityError):
                mixer.blend(
                    CommissionParam,
                    min_percentage=invalid_min_percentage_range,
                    max_percentage=self.valid_max_percentage,
                    day_of_the_week=day_of_the_week,
                )

        with self.subTest(
            "Invalid range for max_percentage field should raise exception."
        ):
            invalid_max_percentage_range = Decimal(11)

            day_of_the_week = mixer.blend(DayOfTheWeek, description="Tuesday")

            with self.assertRaises(IntegrityError):
                mixer.blend(
                    CommissionParam,
                    min_percentage=self.valid_min_percentage,
                    max_percentage=invalid_max_percentage_range,
                    day_of_the_week=day_of_the_week,
                )

    def test_create_model_with_duplicate_day_of_the_week(self):
        """
        Create model with duplicate day_of_the_week should raise integrity
        error.
        """
        day_of_the_week = mixer.blend(DayOfTheWeek, description="Saturday")

        mixer.blend(
            CommissionParam,
            min_percentage=self.valid_min_percentage,
            max_percentage=self.valid_max_percentage,
            day_of_the_week=day_of_the_week,
        )

        with self.assertRaises(IntegrityError):
            mixer.blend(
                CommissionParam,
                min_percentage=self.valid_min_percentage,
                max_percentage=self.valid_max_percentage,
                day_of_the_week=day_of_the_week,
            )

    def test_str_method(self):
        """Test str method of Model."""
        day_of_the_week = mixer.blend(DayOfTheWeek, description="Wednesday")

        commission_param = mixer.blend(
            CommissionParam,
            min_percentage=self.valid_min_percentage,
            max_percentage=self.valid_max_percentage,
            day_of_the_week=day_of_the_week,
        )
        self.assertEqual(str(commission_param), "Wednesday")

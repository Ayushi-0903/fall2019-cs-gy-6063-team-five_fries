# Generated by Django 2.2.1 on 2019-10-05 22:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SignUp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=120)),
                ("user_name", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("confirm_password", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("current_location", models.CharField(max_length=255)),
                ("work_location", models.CharField(max_length=255)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("T", "Tenant"), ("R", "Renter"), ("L", "Landlord")],
                        default="R",
                        max_length=2,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        )
    ]

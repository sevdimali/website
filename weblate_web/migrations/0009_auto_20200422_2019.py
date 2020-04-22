# Generated by Django 2.2.12 on 2020-04-22 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("weblate_web", "0008_service_limit_projects"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="donation",
            options={"verbose_name": "Donation", "verbose_name_plural": "Donations"},
        ),
        migrations.AlterModelOptions(
            name="image",
            options={"verbose_name": "Image", "verbose_name_plural": "Images"},
        ),
        migrations.AlterModelOptions(
            name="package",
            options={
                "verbose_name": "Service package",
                "verbose_name_plural": "Service packages",
            },
        ),
        migrations.AlterModelOptions(
            name="pastpayments",
            options={
                "verbose_name": "Past payment",
                "verbose_name_plural": "Past payments",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Blog post", "verbose_name_plural": "Blog posts"},
        ),
        migrations.AlterModelOptions(
            name="report",
            options={
                "verbose_name": "Weblate report",
                "verbose_name_plural": "Weblate reports",
            },
        ),
        migrations.AlterModelOptions(
            name="service",
            options={
                "verbose_name": "Customer service",
                "verbose_name_plural": "Customer services",
            },
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={
                "verbose_name": "Customer subscription",
                "verbose_name_plural": "Customer subscription",
            },
        ),
    ]

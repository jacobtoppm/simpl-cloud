# Generated by Django 3.2.8 on 2021-11-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simpl", "0019_auto_20211027_1812"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="_date_finished",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="gameexperience",
            name="allow_facilitator_continuous_management",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="Allow facilitators to disable enrollment for continuous runs. If unset, this becomes configurable at the run level.",
                null=True,
            ),
        ),
    ]

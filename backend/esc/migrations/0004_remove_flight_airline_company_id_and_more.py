# Generated by Django 4.1.4 on 2022-12-25 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0001_initial"),
        ("users", "0001_initial"),
        ("esc", "0003_customer_user_alter_booking_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flight",
            name="airline_company_id",
        ),
        migrations.RemoveField(
            model_name="flight",
            name="departure_time",
        ),
        migrations.RemoveField(
            model_name="flight",
            name="destination_airport",
        ),
        migrations.RemoveField(
            model_name="flight",
            name="landing_time",
        ),
        migrations.RemoveField(
            model_name="flight",
            name="origin_airport",
        ),
        migrations.AddField(
            model_name="booking",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="flight",
            name="airline",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="geo.airline_company",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="flight",
            name="arrive_calculated",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="flight",
            name="depart_sched",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="flight",
            name="duration",
            field=models.IntegerField(
                blank=True, default=None, verbose_name="minutes of flight"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="flight",
            name="flight_route",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="geo.flattenedflightroutes",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="flight",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="supplier",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="supplier",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.userprofile",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="booking",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="esc.customer"
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="available_tickets",
            field=models.IntegerField(blank=True, default=380),
        ),
        migrations.AlterField(
            model_name="flight",
            name="flight_number",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="flight",
            name="flight_range",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

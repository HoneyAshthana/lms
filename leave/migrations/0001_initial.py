# Generated by Django 2.0.4 on 2018-04-23 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('is_leave', models.BooleanField(default=False)),
                ('note', models.TextField(max_length=100, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Approved'), (3, 'Rejected')], default=1)),
                ('time_generated', models.DateTimeField(auto_now_add=True)),
                ('time_approved', models.DateTimeField(null=True)),
                ('reply_note', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_new', models.BooleanField(default=True)),
                ('is_credit', models.BooleanField(default=False)),
                ('leave_type', models.IntegerField(choices=[(1, 'Earned Leave'), (2, 'Half pay leave'), (3, 'Commuted leave')])),
                ('date_from', models.DateField(null=True)),
                ('date_to', models.DateField(null=True)),
                ('days', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Deleted'), (1, 'Pending'), (2, 'Approved'), (3, 'Rejected')], default=1)),
                ('reason', models.TextField(max_length=200)),
                ('new_date_from', models.DateField(null=True)),
                ('new_date_to', models.DateField(null=True)),
                ('time_generated', models.DateTimeField(auto_now_add=True)),
                ('time_received', models.DateTimeField(null=True)),
                ('time_approved', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('activity', models.TextField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, max_length=100, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qci_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('earned_balance', models.IntegerField(default=0)),
                ('hp_balance', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Department')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeUpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_new', models.BooleanField(default=False)),
                ('new_name', models.CharField(max_length=100)),
                ('new_email', models.EmailField(max_length=75)),
                ('new_is_active', models.BooleanField(default=False)),
                ('old_name', models.CharField(max_length=100)),
                ('old_email', models.EmailField(max_length=75)),
                ('old_is_active', models.BooleanField(default=True)),
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='update_log', to='leave.Action')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Employee')),
                ('new_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update_new_dept', to='leave.Department')),
                ('old_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update_old_dept', to='leave.Department')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('earned_balance', models.IntegerField()),
                ('earned_change', models.IntegerField(default=0)),
                ('hp_balance', models.IntegerField()),
                ('hp_change', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.Action')),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.Application')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[(1, 'admin'), (2, 'employees')])),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Employee'),
        ),
        migrations.AddField(
            model_name='application',
            name='original',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.Application'),
        ),
    ]

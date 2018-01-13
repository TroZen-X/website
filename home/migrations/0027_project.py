# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20171227_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longevity', models.CharField(choices=[('3M', '0-3 months'), ('6M', '3-6 months'), ('1Y', '6-12 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text='How long has the project accepted contributions from external contributors?', max_length=2)),
                ('community_size', models.CharField(choices=[('3', '1-3 people'), ('5', '3-5 people'), ('10', '5-10 people'), ('20', '11-20 people'), ('50', '21-50 people'), ('100', '50-100 people'), ('999', 'More than 100 people')], default='3', help_text='How many people are contributing to this project regularly?', max_length=3)),
                ('approved_license', models.BooleanField(help_text='I assert that my project is released under an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a>) or a <a href="https://creativecommons.org/share-your-work/licensing-types-examples/">Creative Commons license</a>)')),
                ('short_title', models.CharField(help_text='Short project title - 100 characters or less, assuming the person has never heard of your technology before, and starting with a verb like "Create", "Improve", "Extend", "Survey", "Document"', max_length=100)),
                ('project_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Participation')),
            ],
        ),
    ]
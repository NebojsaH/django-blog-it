# Generated by Django 2.0.2 on 2018-03-04 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0014_post_slugs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_on']},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'ordering': ['-id']},
        ),
    ]
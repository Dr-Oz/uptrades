from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO app_treemenucategory (id, name, verbose_name) 
                VALUES (1, 'main_menu', 'Main menu');

            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (1, 'Home', 'home', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (2, 'Markets', 'markets', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (3, 'Platforms', 'platforms', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (4, 'Mt4', 'mt4', 1, 3);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (5, 'Download', 'download', 1, 4);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (6, 'Mt5', 'mt5', 1, 3);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (7, 'Desktop', 'desktop', 1, 6);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (8, 'Phone', 'phone', 1, 6);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (9, 'Investment', 'investment', 1, null);
            INSERT INTO app_treemenu (id, name, path, category_id, parent_id) 
                VALUES (10, 'GitHub', 'https://github.com/Dr-Oz', 1, 3);
        """)
    ]
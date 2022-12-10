# Generated by Django 4.1.2 on 2022-12-10 16:45

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Формат: обязательный, максимальная длина символов - 255', max_length=255, unique=True, verbose_name='Имя категории товара')),
                ('slug', models.SlugField(blank=True, help_text='Формат: обязательный, максимальная длина символов - 255', max_length=255, null=True, unique=True, verbose_name='Путь до товаров этой категории')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если категория используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если категория должна быть удалена')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Формат: необязательный', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='core.category', verbose_name='Дочерняя категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White')], max_length=25, null=True, verbose_name='Цвет товара')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если цвет товара используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если цвет товара должен быть удален')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/')),
                ('is_default', models.BooleanField(default=False, help_text='Формат: необязательный', verbose_name='Выбрать, если фото товара главное ')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если фото товара используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если фото товара должно быть удалено')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Формат: обязательный, максимальная длина символов - 255', max_length=255, unique=True, verbose_name='Имя типа товара')),
                ('slug', models.SlugField(help_text='Формат: обязательный, максимальная длина символов - 255, название такое же, как и у категории', max_length=255, unique=True, verbose_name='Путь до товаров этого типа')),
                ('description', models.TextField(help_text='Формат: обязательный', verbose_name='Описание типа товара')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если тип товара используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если тип товара должен быть удалена')),
                ('category', mptt.fields.TreeManyToManyField(blank=True, help_text='Формат: обязательный', null=True, to='core.category', verbose_name='Выбрать категорию к которой привязан данный тип товара')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Формат: обязательный, максимальная длина - 255', max_length=255, verbose_name='Имя товара')),
                ('slug', models.CharField(help_text='Формат: обязательный, максимальная длина - 255', max_length=255, verbose_name='Путь до товара')),
                ('store_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'Цена товара должна быть между 0 и 99999.99.'}}, help_text='Формат: число, максимальное значение - 99999.99', max_digits=7, verbose_name='Базовая стоимость товара')),
                ('retail_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'Цена товара должна быть между 0 и 99999.99.'}}, help_text='Формат: число, максимальное значение - 99999.99', max_digits=7, verbose_name='Цена продажи')),
                ('description', models.TextField(help_text='Формат: обязательный', verbose_name='Описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Определяется автоматически, возможно редактирование', verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если товар используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если товар должен быть удалена')),
                ('media', models.ManyToManyField(blank=True, help_text='Связана с Медиа', null=True, to='core.media', verbose_name='Фото товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_inventory', to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'XLARGE')], max_length=20, null=True, verbose_name='Размер товара')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если размер товара используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если размер товара должен быть удален')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, help_text='Формат: обязательный', verbose_name='Количество комбинации')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если вариация товара используется в каталоге')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если вариация товара должна быть удалена')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variations', to='core.productinventory')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.size')),
            ],
            options={
                'ordering': ['size'],
                'unique_together': {('color', 'size')},
            },
        ),
    ]

from django.db import migrations, models
import django.db.models.deletion


def link_repairs_to_clients(apps, schema_editor):
    Reparaciones = apps.get_model('faenas', 'Reparaciones')
    Clientes = apps.get_model('faenas', 'Clientes')

    for repair in Reparaciones.objects.all():
        if not repair.Cliente:
            continue

        cliente = Clientes.objects.filter(Nombre__iexact=repair.Cliente.strip()).first()
        if cliente:
            repair.ClienteRelacionado_id = cliente.id
            repair.save(update_fields=['ClienteRelacionado'])


class Migration(migrations.Migration):

    dependencies = [
        ('faenas', '0004_reparaciones_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparaciones',
            name='ClienteRelacionado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reparaciones', to='faenas.clientes', verbose_name='Cliente'),
        ),
        migrations.RunPython(link_repairs_to_clients, migrations.RunPython.noop),
    ]
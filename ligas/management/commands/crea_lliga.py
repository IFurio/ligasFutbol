    from django.core.management.base import BaseCommand, CommandError
    from django.utils import timezone
    from faker import Faker
    from datetime import timedelta
    from random import randint
     
    from lliga.models import *
     
    faker = Faker(["es_CA","es_ES"])
     
    class Command(BaseCommand):
        help = 'Crea una lliga amb equips i jugadors'
     
        def add_arguments(self, parser):
            parser.add_argument('titol_lliga', nargs=1, type=str)
     
        def handle(self, *args, **options):
            titol_lliga = options['titol_lliga'][0]
            lliga = Lliga.objects.filter(titol=titol_lliga)
            if lliga.count()>0:
                print("Aquesta lliga ja està creada. Posa un altre nom.")
                return
     
            print("Creem la nova lliga: {}".format(titol_lliga))
            lliga = Lliga(  titol=titol_lliga,
                            inici=timezone.now(),
                            final=timezone.now()+timedelta(days=11*30))
            lliga.save()
     
            print("Creem equips")
            prefixos = ["RCD", "Athletic", "", "Deportivo", "Unión Deportiva"]
            for i in range(20):
                ciutat = faker.city()
                prefix = prefixos[randint(0,len(prefixos)-1)]
                if prefix:
                    prefix += " "
                nom =  prefix + ciutat
                equip = Equip(nom=nom)
                #print(equip)
                equip.save()
                lliga.equips.add(equip)
     
                print("Creem jugadors de l'equip "+nom)
                for j in range(25):
                    nom = faker.first_name()
                    cognom1 = faker.last_name()
                    cognom2 = faker.last_name()
                    jugador = Jugador(nom=nom,cognom1=cognom1,cognom2=cognom2,alias=nom+" "+cognom1)
                    #print(jugador)
                    jugador.save()
     
            print("Creem partits de la lliga")
            for local in lliga.equips.all():
                for visitant in lliga.equips.all():
                    if local!=visitant:
                        partit = Partit(local=local,visitant=visitant)
                        partit.local = local
                        partit.visitant = visitant
                        partit.lliga = lliga
                        partit.save()
                        # gols
                        gols_local = randint(0,7)
                        gols_visitant = randint(0,4)
                        for i in range(0, gols_local):
                            jugador = local.jugardor_set.all()[randint(0,25)]
                            gol = Event(
                                tipus=Event.EventType.GOL,
                                jugador=jugador,
                                equip=local,
                                partit=partit,
                                temps=timezone.now() )
                            gol.save()
                            partit.event_set.add(gol)
                        for i in range(0, gols_visitant):
                            jugador = visitant.jugardor_set.all()[randint(0,25)]
                            gol = Event(
                                tipus=Event.EventType.GOL,
                                jugador=jugador,
                                equip=local,
                                partit=partit,
                                temps=timezone.now() )
                            gol.save()
                            partit.event_set.add(gol)

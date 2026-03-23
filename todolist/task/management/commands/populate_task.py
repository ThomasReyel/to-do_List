import random
from django.core.management.base import BaseCommand
from task.models import Task
from datetime import timedelta,date

class Command(BaseCommand):
    help = "Popular banco com exemplos de tarefas"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('iniciando'))
        if Task.objects.exists():
            self.stdout.write(self.style.WARNING('O banco já possui tarefas'))
            decision = input('Deseja apagar os existentes? (s/n): ')
            
            if decision.lower() == 's':
                Task.objects.all().delete()
                self.stdout.write(self.style.SUCCESS('Tarefas removidas'))
            else:
                self.stdout.write('Operação cancelada')
                return
        
        titles = [
            'Estudar Python',
            'Fazer exercícios',
            'Ler documentação',
            'Praticar Django',
            'Revisar código',
        ]

        descriptions = [
            'Assistir aulas e praticar',
            'Completar todos os exercícios',
            'Ler capítulos 1-5',
            'Criar projeto exemplo',
            'Revisar e refatorar',
        ]

        # Opções para situação
        states = ['nova', 'em_andamento', 'concluida', 'cancelada']

        count = 0

        for i in range(12):
            data = date.today() + timedelta(days=random.randint(1, 60))
            data = data.strftime('%Y-%m-%d')
            new_title = random.choice(titles)
            new_description = random.choice(descriptions)
            new_deadline = data
            new_completion_date = None
            new_state = random.choice(states)

            task = Task.objects.create(
                title = new_title,
                description = new_description,
                deadline = new_deadline,
                completion_date = new_completion_date,
                state = new_state
            )
            count += 1
        
        self.stdout.write(self.style.SUCCESS(f'\n {count} tarefas foram criadas com sucesso'))
        

import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from quiz.models import Answer, Category, Question

class Command(BaseCommand):
    help = 'Takes txt file as input and looks up each word, creating question:answer pairs'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)
        parser.add_argument('category', nargs='+', type=str)

    def handle(self, *args, **options):
        url = settings.DICTIONARY_API_ENDPOINT
        filename = options['filename'].pop()
        categoryname = options['category'].pop()
        count = 0
        with open(filename, 'r') as file:
            for line in file.readlines():
                res=requests.get(url.format(word=line.strip()))
                if res.json():
                    category, success = Category.objects.get_or_create(title=categoryname)
                    question = Question.objects.create(
                        question_text=' '.join(res.json()[0]['Definitions']),
                        category=category
                    )
                    Answer.objects.create(
                        answer_text=line.strip(),
                        question=question
                    )
                    count += 1

        self.stdout.write(self.style.SUCCESS('Successfully added {} words'.format(count)))

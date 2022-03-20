
import django_tables2 as tables
from .models import Paper

class PaperTable(tables.Table):
    class Meta:
        model = Paper
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'title',
            'researcher',
            'supervisor',
            'degree',
            'date_of_publishing',
            'paper_number'
            )
        #attrs = {"class": "papers-table"}
    
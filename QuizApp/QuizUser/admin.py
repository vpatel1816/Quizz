from django.contrib import admin
from .models import quiz_que
# Register your models here.

class quiz_quee(admin.ModelAdmin):
	list_display = ('qno','question','ans')


admin.site.register(quiz_que, quiz_quee)
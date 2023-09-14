from django.contrib import admin
from .models import Post, Webcontent, BannerPost, RecommededPost, Call_to_Action1, Call_to_Action2, Call_to_Action3, Services, RecommededPost, Report_Section, Final_Section
# Register your models here.
admin.site.register(Post)
admin.site.register(Webcontent)
admin.site.register(BannerPost)
admin.site.register(RecommededPost)
admin.site.register(Call_to_Action1)
admin.site.register(Call_to_Action2)
admin.site.register(Call_to_Action3)
admin.site.register(Services)
admin.site.register(Report_Section)
admin.site.register(Final_Section)

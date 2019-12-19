from django.contrib import admin
from MECboard.models import Board, Comment,Profile, Finished_board
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class BoardAdmin(admin.ModelAdmin):
    list_display = ("writer", "title", "content","win_score")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("writer", "content", "vote")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "nickname")
class Finished_boardAdmin(admin.ModelAdmin):
    list_display = ("writer", "title", "content")

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Finished_board, Finished_boardAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
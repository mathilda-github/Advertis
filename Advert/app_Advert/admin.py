from django.contrib import admin

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' , 'descr', 'price', 'auction', 'created_date', 'update_date', 'user', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общие', {
            'fields': ('title', 'descr', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('auction', 'price'),
            'classes': ['wide', 'extrapretty']
        })
    )
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

#https://docs.djangporpject.com/en/4.2/reg/contrib/admin

admin.site.register(Advertisement, AdvertisementAdmin)

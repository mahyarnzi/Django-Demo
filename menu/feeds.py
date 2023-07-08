from django.contrib.syndication.views import Feed
from menu.models import Menu


class MenuFeed(Feed):
    title = "Menu"
    link = "/menu/rss/feed"
    description = ""

    def items(self):
        return Menu.objects.all()

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return {'price': item.price, 'meal': item.meal.name, 'image': item.image.url, 'content': item.content}

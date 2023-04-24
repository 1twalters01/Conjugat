from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.cache import cache

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_active=True)
        backtrace = 7

        for user in users:
            try:
                cacheData = cache.get(key=user.username)
            except:
                cacheData = None
            
            if cacheData:
                for data in cacheData:
                    result = cache.get(key=data)
                    
                    if result['EndDateTime'].date() <= datetime.now().date() - timedelta(days=backtrace):
                        cacheData.remove(data)
                        cache.delete(key=data)
                if cacheData != None:
                    cache.set(key=user.username, value=cacheData)
                else:
                    cache.delete(key=user.username)
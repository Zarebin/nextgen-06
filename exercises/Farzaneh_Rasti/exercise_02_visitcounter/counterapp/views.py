from django.conf import settings
import redis
from django.shortcuts import render
from django.http import HttpResponse
from .models import browser_count
#from django.core.cache import cache

redis_instance = redis.StrictRedis(host='redis_service',#settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

# Create your views here.
def visitcount(request):
    browserType = request.user_agent.browser.family 
    
    #totalCount = int(redis_instance.get('visitscount')) + 1
    #redis_instance.set('visitscount', totalCount)
    totalCount = redis_instance.incr('hits')
    try:
        bc = browser_count.objects.get(browser=browserType)
        count = bc.visitsCount + 1
        bc.visitsCount = count
        bc.save()
    except:
        bc = browser_count(browser=browserType)
        bc.save()
    
    allbrowsers = browser_count.objects.all()
    response = ' '.join([f"<p> {cnt.browser}: {cnt.visitsCount} requests </p>" for cnt in allbrowsers])

    '''
    return HttpResponse("""
        <h2> Redis output: </h2>
        <p> # visits </p>
        <br></br>
        <h2> Postgresql Output: </h2>
        <p> # chromes </p>
        </p> # mozillas </p>
    """)
    '''
    response = f"<p>Total requests: {totalCount} </p>" + response
    return HttpResponse(response)

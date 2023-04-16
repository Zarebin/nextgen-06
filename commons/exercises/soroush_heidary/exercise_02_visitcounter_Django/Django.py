from django.http import HttpResponse
from django.views.decorators.http import require_GET
import redis

client = redis.Redis(host='redis-server', port=6379)

client.set('mozilla_count', 0)
client.set('curl_count', 0)
client.set('other_count', 0)

@require_GET
def handle_visit(request):
    user_agent = request.GET.get('User-Agent')
    app_name = user_agent[:user_agent.find('/')].lower()
    counts = {'curl': 0, 'mozilla': 0, 'other': 0}
    counts['curl'] = int(client.get('curl_count') or 0)
    counts['mozilla'] = int(client.get('mozilla_count') or 0)
    counts['other'] = int(client.get('other_count') or 0)

    if app_name == 'curl':
        counts['curl'] += 1
        client.set('curl_count', counts['curl'])
    elif app_name == 'mozilla':
        counts['mozilla'] += 1
        client.set('mozilla_count', counts['mozilla'])
    else:
        counts['other'] += 1
        client.set('other_count', counts['other'])
 
    response_text = 'Number of visits on Mozzila: {0}</br> Number of visits on Curl: {1}'.format(
        counts['mozilla'], counts['curl'], counts['other'])
    return HttpResponse(response_text)



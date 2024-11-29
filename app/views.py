import sqlite3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def db_query(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            result = cursor.fetchone() 
            return JsonResponse({'status': 'success', 'data': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        finally:
            conn.close()
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'})

from django.http import HttpResponse
def index(request):
    html ="""
          <html>
            <body>
              <p>
                If you seek api documentations,you can find them <a href="http://api.fumcbm.tk/docs">here.</a>
                <br>
                This url should return 404 in the future(or maybe redirect to <b>/docs</b>).
              </p>
            </body>
          </html>      
          """
    return HttpResponse(html)

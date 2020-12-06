from django.http import HttpResponse
def index(request):
    html ="""
          <html>
            <body>
              <p>
                If you seek api documentations,you can find them <a href="http://api.fumcbm.tk/docs">here.</a>
                <br>
                Maybe we should redirect this url to <b>/docs</b> ....
              </p>
            </body>
          </html>      
          """
    return HttpResponse(html)

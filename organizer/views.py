from django.http.response import HttpResponse

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    html_output = "<html>\n"
    html_output += "<head>\n"
    html_output += "  <title>"
    html_output += "Don't Do This!</title>\n"
    html_output += "</head>\n"
    html_output += "<body>\n"
    html_output += "  <ul>\n"
    for tag in tag_list:
        html_output += "    <li>"
        html_output += tag.name.title()
        html_output += "</li>\n"
    html_output += "  </ul>\n"
    html_output += "</body>\n"
    html_output += "</html>\n"
    return HttpResponse(html_output)

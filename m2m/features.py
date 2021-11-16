import re
from django.core.mail import send_mail


def convert_mail_text(text: str) -> str:
    yt_search_url = 'https://www.youtube.com/results?search_query='
    result = re.findall(r'\w+', text)

    for index, word in enumerate(result):
        if len(word) > 3:
            result[index] = f'<a href="{yt_search_url}{word}">{word}</a>'
        
    return ' '.join(result)


def custom_send_mail(to: str, text: str) -> None:
    send_mail('hi, we from mailtome', text, 'no-reply@mtome.fun', [to], fail_silently=False,html_message=text)
from proxy_gemini import ProxyGemini
import info

prompt = """\
Тебя зовут Куб.
Ты чат-бот организации дополнительного IT-образования. \
Твоя задача отвечать на вопросы учащихся по \
по возможным курсам, помогать им выбрать интересные для себя предметы.
Ты знаешь, что есть следующие курсы: {0}
Тебе запрещено разговаривать на темы кроме образования и курсов. \
Если же пользователь задаст вопрос, который не связан с курсами, \
тебе нужно перевести тему на другой вопрос.

Вот история переписки с пользователем, а также его вопрос:\n
""".format(', '.join(info.courses_list))

client: ProxyGemini


def init_genai_client():
    global client
    client = ProxyGemini(
        api_key=info.token,
        proxy_url="http://localhost:10808"
    )


def request(text):
    global client
    text = prompt + text
    try:
        response = client.complete(text).text
    except Exception as er:
        print(er)
        response = "AI не подключен"
    return response

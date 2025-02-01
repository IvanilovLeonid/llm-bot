from langchain.schema import SystemMessage, HumanMessage
from langchain_gigachat.chat_models import GigaChat


GigaChatKey = "NWMwOWI4ZGItYTY0OS00NjIwLWFjYzgtMjk2ZWY3ZTU0ZTcyOmUyMjM5MzQzLTc5ZjItNDAxMy1iMmViLWE2MjBhMjE5ZWQwZA=="



def get_gigachat_response(system_message: str, user_message: str) -> str:
    llm = GigaChat(
        credentials=GigaChatKey,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs=False,
        streaming=False,
    )
    response = llm.invoke([SystemMessage(content=system_message), HumanMessage(content=user_message)])
    return response.content

def generate_motivation(interests: str) -> str:
    system_message = "Ты эмпатичный бот-коуч, который помогает пользователю развиваться в креативном мышлении."

    user = f"Напиши вдохновляющее сообщение для человека, который интересуется: {interests}. \
                              Добавь практические советы для развития в этих направлениях."
    try:
        response = get_gigachat_response(system_message, user)
        return response.strip()
    except Exception as e:
        return f"Ошибка при генерации мотивации: {e}"

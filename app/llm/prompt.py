from langchain_core.prompts import PromptTemplate


TEMPLATE = """Вы — эксперт по PostgreSQL. 
Учитывая вопрос пользователя, создайте синтаксически верный запрос PostgreSQL, выполните его и верните ТОЛЬКО результат выполнения из базы данных.
Никаких пояснений, вступительных фраз и лишних слов.
В ответе выводи ТОЛЬКО чистый SQL код. 
НЕ используй разметку markdown (не пиши ```sql).
НЕ пиши никаких пояснений.

Схема базы данных:
{table_info}

Вопрос: {input}

SQL-script:"""

def get_prompt():
    return PromptTemplate(
        input_variables=["input", "table_info"], 
        template=TEMPLATE
    )

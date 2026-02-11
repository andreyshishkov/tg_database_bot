from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


from .prompt import get_prompt
from db import DATABASE_INFO

from dotenv import load_dotenv
load_dotenv() 

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, base_url="https://api.vsegpt.ru/v1",)
sql_chain = get_prompt() | llm | StrOutputParser()


async def transform_text_to_sql(question: str):
    raw_sql = await sql_chain.ainvoke({
        "input": question,
        "table_info": DATABASE_INFO
    })
    clean_sql = raw_sql.replace("```sql", "").replace("```", "").strip()
    return clean_sql

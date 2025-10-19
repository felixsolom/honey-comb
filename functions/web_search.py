from ddgs import DDGS
from bs4 import BeautifulSoup
import requests

def web_search(query: str, **kwargs) -> str:
    try:
        with DDGS() as ddgs:
            search_results = list(ddgs.text(query, max_results=1))
            if not search_results:
                return "No search results found"
            
            top_result_url = search_results[0]['href']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(top_result_url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        if soup.body:
            text_content = soup.body.get_text(' ', strip=True)
        else:
            text_content = soup.get_text(' ', strip=True)

        max_length = 4000
        if len(text_content) > max_length:
            text_content = text_content[:max_length] + "..."

        return f'Content from {top_result_url}:\n\n{text_content}'
    
    except Exception as e:
        return f'En error occured during web search: {e}'
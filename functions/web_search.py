from googlesearch import search 

def web_search(query: str, **kwargs) -> str:
    try:
        search_results = list(search(query, num_results=5))
        if not search_results:
            return "No search results found"
        return '\n\n'.join(search_results)
    except Exception as e:
        return f'En error occured during web search: {e}'
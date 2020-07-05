# Features:
 - Upload snippet.
 - Read snippet.
 - Search snippets.
 - Edit snippet.
 - Snippet expiration.
 - Snippet analytics -> View count.

# Basic design
- Load balancers in front.
- One read and write API sharing a memory cache.
- Note that there will not be any registration feature.
- All users will be anonymous.

# Load estimation
- Number of snippets per day.
- Average size of snippet.

# Upload Snippet.
- Request goes through reverse proxy -> Write API.
- Then a shortlink is requested from the shortlink service.
- Then all the data goes to Database + Search Engine.
- The shortlink vs snippet-url mapping goes to the cache.

# Read snippet.
- Reverse proxy -> Read API.
- Search for shortlink in cache. If not found, then fetch from db.
- Then fetch the details from the object store.

# Search snippet.
- Hit the search engine.

# Edit snippet
- A combination of read+write.

# Snippet Expiration
- A dedicated snippet expiration service runs periodically to check for expired snippets in the database.
- For every expired snippet, delete it from the database + cache + search engine.

# Shortlink Service
- Generate a unique integer, or use the current timestamp.
- Convert to base 62.

# Tech used
- SQL database with sharding maybe.
- Or Amazon Aurora.
- Amazon S3 for snippet storage.
- Elasticsearch for search.
- Redis for cache.

# Database design
- Table *Snippet* - `{id, author_id, file_url, created_at, url, expiration_date}`, with index on `id`, `author_id`, `url`.

# API design.
- getSnippet(url) -> {contents}
- addSnippet(content) -> {url, created_at}
- getShortlink() -> {url}
- deleteSnippet(url)
- searchSnippet(search_string) -> {list_of_urls}

![](assets/pastebin1.png)  
![](assets/pastebin2.png)  
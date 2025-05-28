import sqlite3;

def init_db():
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            language TEXT,
            tags TEXT,
            description TEXT,
            code TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def add_snippet(name,language,tags,description,code):
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO snippets (name, language, tags, description, code)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, language, tags, description, code))
    conn.commit()
    conn.close()
def list_snippets():
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("SELECT id, name, language, tags FROM snippets")
    results = c.fetchall()
    conn.close()
    return results
def delete_snippet_by_id(snippet_id):
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    c.execute("DELETE FROM snippets WHERE id = ?", (snippet_id,))
    conn.commit()
    conn.close()
def search_snippets(keyword):
    conn = sqlite3.connect("snippets.db")
    c = conn.cursor()
    query = """
        SELECT id, name, language, tags, description
        FROM snippets
        WHERE name LIKE ? OR description LIKE ? OR tags LIKE ?
    """
    pattern = f"%{keyword}%"
    c.execute(query, (pattern, pattern, pattern))
    results = c.fetchall()
    conn.close()
    return results

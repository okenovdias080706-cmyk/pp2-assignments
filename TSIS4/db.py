import psycopg2
import config

def save_game_result(username, score, level):
    try:
        conn = psycopg2.connect(**config.DB_CONFIG)
        cur = conn.cursor()
        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (username,))
        cur.execute("SELECT id FROM players WHERE username = %s", (username,))
        p_id = cur.fetchone()[0]
        cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", (p_id, score, level))
        conn.commit()
        cur.close()
        conn.close()
    except: pass

def get_top_scores():
    try:
        conn = psycopg2.connect(**config.DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT p.username, s.score FROM game_sessions s JOIN players p ON s.player_id = p.id ORDER BY s.score DESC LIMIT 5")
        res = cur.fetchall()
        cur.close()
        conn.close()
        return res
    except: return []
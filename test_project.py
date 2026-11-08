import os
import sqlite3
from project import init_db, add_task, complete_task, delete_task

def setup_module(module):
    if os.path.exists("todo.db"):
        try:
            os.remove("todo.db")
        except PermissionError:
            pass
    init_db()

def test_add_task():
    add_task("CS50 Test Görevi")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM tasks WHERE title = 'CS50 Test Görevi'")
    task = cursor.fetchone()
    conn.close()
    assert task is not None
    assert task[0] == "CS50 Test Görevi"

def test_complete_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE title = 'CS50 Test Görevi'")
    task_id = cursor.fetchone()[0]
    conn.close()

    complete_task(task_id)

    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM tasks WHERE id = ?", (task_id,))
    status = cursor.fetchone()[0]
    conn.close()
    assert status == "Tamamlandı"

def test_delete_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE title = 'CS50 Test Görevi'")
    task_id = cursor.fetchone()[0]
    conn.close()

    delete_task(task_id)

    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    assert task is None

def teardown_module(module):
    if os.path.exists("todo.db"):
        try:
            os.remove("todo.db")
        except PermissionError:
            pass

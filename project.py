import sqlite3
import sys

def init_db():
    """Veritabanını ve tabloyu otomatik olarak hazırlar."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'Bekliyor'
        )
    """)
    conn.commit()
    conn.close()

def add_task(title):
    """Yeni bir görev ekler."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, status) VALUES (?, 'Bekliyor')", (title,))
    conn.commit()
    conn.close()
    print(f"\n[+] '{title}' başarıyla eklendi.")

def list_tasks():
    """Görevleri sembolleriyle listeler."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, status FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("\nHenüz hiç görev eklenmemiş.")
        conn.close()
        return

    print("\n--- GÖREV LİSTESİ ---")
    for task in tasks:
        durum_sembolu = "✔" if task[2] == "Tamamlandı" else "❌"
        print(f"[{task[0]}] {task[1]} - {durum_sembolu}")
    print("--------------------")
    conn.close()

def complete_task(task_id):
    """Görevi tamamlandı yapar."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'Tamamlandı' WHERE id = ?", (task_id,))
    if cursor.rowcount > 0:
        print(f"\nID {task_id} olan görev tamamlandı!")
    else:
        print("\nBu ID'ye ait bir görev bulunamadı.")
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Görevi siler."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount > 0:
        print(f"\nID {task_id} olan görev silindi!")
    else:
        print("\nBu ID'ye ait bir görev bulunamadı.")
    conn.commit()
    conn.close()

def main():
    init_db()

    while True:
        print("\n--- AKILLI GÖREV YÖNETİCİSİ ---")
        print("1. Yeni Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görevi Tamamlandı Olarak İşaretle")
        print("4. Görevi Sil")
        print("5. Çıkış")

        secim = input("Lütfen bir işlem seçin (1-5): ").strip()

        if secim == "1":
            title = input("Eklenecek görev başlığı: ").strip()
            if title:
                add_task(title)
            else:
                print("\nGörev başlığı boş olamaz!")

        elif secim == "2":
            list_tasks()

        elif secim == "3":
            list_tasks()
            try:
                task_id = int(input("Tamamlanan görevin ID'sini girin: "))
                complete_task(task_id)
            except ValueError:
                print("\nLütfen geçerli bir sayı girin!")

        elif secim == "4":
            list_tasks()
            try:
                task_id = int(input("Silmek istediğiniz görevin ID'sini girin: "))
                delete_task(task_id)
            except ValueError:
                print("\nLütfen geçerli bir sayı girin!")

        elif secim == "5":
            print("\nGörüşmek üzere, hoşça kalın!")
            sys.exit(0)

        else:
            print("\nGeçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

if __name__ == "__main__":
    main()

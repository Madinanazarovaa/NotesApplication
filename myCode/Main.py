import json
import os
from datetime import datetime

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp,
    }
    notes.append(note)
    save_notes()
    print("Заметка успешно создана!")

def read_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def list_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print(f"Текст: {note['body']}\n")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            print(f"Текущий заголовок: {note['title']}")
            new_title = input("Введите новый заголовок (оставьте пустым для сохранения текущего): ")
            if new_title:
                note["title"] = new_title
            print(f"Текущий текст: {note['body']}")
            new_body = input("Введите новый текст (оставьте пустым для сохранения текущего): ")
            if new_body:
                note["body"] = new_body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена!")
            return
    print("Заметка с указанным ID не найдена.")

if __name__ == "__main__":
    notes = read_notes()

    while True:
        print("\nМеню:")
        print("1. Создать новую заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            if not notes:
                print("У вас пока нет заметок.")
            else:
                list_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
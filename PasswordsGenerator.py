import random 
import tkinter as tk

# строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_'
ambiguous_chars = 'il1Lo0O'

# Функция генерации паролей
def generate_password(length, chars):
  password = ''
  for _ in range(length):
    password += random.choice(chars)
  return password

# Вводим данные
def generate_passwords():
    password_count = int(password_count_entry.get())
    password_length = int(password_length_entry.get())
    integers = integers_var.get()
    up_letters = up_letters_var.get()
    low_letters = low_letters_var.get()
    symbols = symbols_var.get()
    exclude_ambiguous = exclude_ambiguous_var.get()

# Добавляем символы в переменную chars
    chars = ''
    if integers == 1:
        chars += digits
    if up_letters == 1:
        chars += uppercase_letters
    if low_letters == 1:
        chars += lowercase_letters
    if symbols == 1:
        chars += punctuation
    if exclude_ambiguous == 1:
        for char in ambiguous_chars:
            chars = chars.replace(char, '')

# Генерация паролей
    passwords = []
    for _ in range(password_count):
        password = generate_password(password_length, chars)
        passwords.append(password)

# Вывод сгенерированных паролей
    passwords_text.delete(1.0, tk.END)
    for password in passwords:
        passwords_text.insert(tk.END, password + '\n')

root = tk.Tk()
root.title("Password Generator")

# Создаём элементы интерфейса 
password_count_label = tk.Label(root, text="Количество паролей:")
password_count_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
password_count_entry = tk.Entry(root)
password_count_entry.grid(row=0, column=1, padx=10, pady=10)

password_length_label = tk.Label(root, text="Длина пароля:")
password_length_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=1, column=1, padx=10, pady=10)

integers_var = tk.IntVar()
integers_checkbox = tk.Checkbutton(root, text="Включать цифры", variable=integers_var)
integers_checkbox.grid(row=2, column=0, padx=10, pady=10, sticky='w')

up_letters_var = tk.IntVar()
up_letters_checkbox = tk.Checkbutton(root, text="Включать прописные буквы", variable=up_letters_var)
up_letters_checkbox.grid(row=3, column=0, padx=10, pady=10, sticky='w')
low_letters_var = tk.IntVar()
low_letters_checkbox = tk.Checkbutton(root, text="Включать строчные буквы", variable=low_letters_var)
low_letters_checkbox.grid(row=4, column=0, padx=10, pady=10, sticky='w')

symbols_var = tk.IntVar()
symbols_checkbox = tk.Checkbutton(root, text="Включать символы", variable=symbols_var)
symbols_checkbox.grid(row=5, column=0, padx=10, pady=10, sticky='w')

exclude_ambiguous_var = tk.IntVar()
exclude_ambiguous_checkbox = tk.Checkbutton(root, text="Исключать неоднозначные символы", variable=exclude_ambiguous_var)
exclude_ambiguous_checkbox.grid(row=6, column=0, padx=10, pady=10, sticky='w')

generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='w')

passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky='w')

root.mainloop()

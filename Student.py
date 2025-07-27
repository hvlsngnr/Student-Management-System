from tkinter import *
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import pymysql


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Öğrenci Yönetim Sistemi")
        self.master.geometry("400x400")
        self.master.configure(bg='#2C2C2C')
        self.master.resizable(False, False)

        self.header = Frame(master, bg='#EF7C03', height=50)
        self.header.pack(fill='x')

        self.title_label = Label(self.header, text="Giriş Yap",
                                 bg='#EF7C03', fg='black', font=('Arial', 18, 'bold'))
        self.title_label.pack(pady=10)

        self.username_var = StringVar()
        self.password_var = StringVar()

        Label(master, text="Kullanıcı Adı:", bg='#2C2C2C',
              fg='white', font=('Arial', 12)).pack(pady=(30, 5))
        Entry(master, textvariable=self.username_var, bd=2,
              relief='groove', font=('Arial', 12)).pack(ipady=5, padx=50)

        Label(master, text="Şifre:", bg='#2C2C2C', fg='white',
              font=('Arial', 12)).pack(pady=(20, 5))
        Entry(master, show='*', textvariable=self.password_var, bd=2,
              relief='groove', font=('Arial', 12)).pack(ipady=5, padx=50)

        self.login_btn = Button(master, text="Giriş Yap", command=self.check_login, bg='#EF7C03', fg='black',
                                font=('Arial', 14, 'bold'), activebackground='#FFA733', activeforeground='black')
        self.login_btn.pack(pady=30, ipadx=20, ipady=5)

        self.login_btn.bind("<Enter>", self.on_enter)
        self.login_btn.bind("<Leave>", self.on_leave)

    def check_login(self):

        username = self.username_var.get()
        password = self.password_var.get()

        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
        result = cur.fetchone()
        con.close()

        if result:
            self.master.destroy()
            root = Tk()
            Ogrenci(root)
            root.mainloop()
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

    def on_enter(self, e):
        self.login_btn['background'] = '#FFA733'

    def on_leave(self, e):
        self.login_btn['background'] = '#EF7C03'


class Ogrenci:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('Öğrenci Kayıt Sistemi')
        self.root.configure(background='white')

        self.header = Frame(root, bg='#3498DB', height=30)
        self.header.pack(fill='x')

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.dell_var = StringVar()
        self.se_var = StringVar()
        self.se_by = StringVar()

        self.create_input_frame()
        self.create_button_frame()
        self.create_search_frame()
        self.create_table_frame()
        self.fetch_all()

    def create_input_frame(self):
        frame = Frame(self.root, bg='white')
        frame.place(x=1, y=80, width=210, height=400)

        for label, var in [("Seri numarası", self.id_var),
                           ("Öğrencinin adı", self.name_var),
                           ("Öğrenci mail adresi", self.email_var)]:
            Label(frame, text=label, bg='white').pack()
            Entry(frame, textvariable=var, bd=2).pack()

        Label(frame, text='Cinsiyet', bg='white').pack()
        gender_combo = ttk.Combobox(
            frame, textvariable=self.gender_var, values=['Erkek', 'Kadın'])
        gender_combo.pack()

        Label(frame, text='Öğrenciyi adına göre sil',
              fg='red', bg='white').pack()
        Entry(frame, textvariable=self.dell_var, bd=2).pack()

    def create_button_frame(self):
        frame = Frame(self.root, bg='white')
        frame.place(x=1, y=400, width=210, height=400)
        Label(frame, text='Kontrol Paneli', font=('Deco', 14),
              fg='white', bg='#2980B9').pack(fill=X)

        buttons = [("Öğrenci Ekle", '#3498DB', self.add_student),
                   ("Düzeltme", '#3498DB', self.update),
                   ("Temizle", '#3498DB', self.clear),
                   ("Şifre Değiştir", '#3498DB', self.change_password),
                   ("transkript", '#3498DB', self.open_grades_window),
                   ("Öğrenci Sil", 'red', self.delete),
                   ("Çıkış", 'black', self.root.quit)]

        for i, (text, color, command) in enumerate(buttons):
            Button(frame, text=text, bg=color,  fg='white', activebackground='#5DADE2',
                   activeforeground='white', command=command).place(x=30, y=33 + i * 40, width=150, height=30)

    def create_search_frame(self):
        frame = Frame(self.root, bg='white')
        frame.place(x=215, y=30, width=1320, height=50)

        Label(frame, text='öğrenci ara', bg='white').place(x=25, y=12)
        ttk.Combobox(frame, textvariable=self.se_by, values=[
                     'id', 'name', 'email']).place(x=125, y=12)
        Entry(frame, textvariable=self.se_var).place(x=275, y=12)
        search_button = Button(frame, text='Ara', bg='#3498DB', fg='white',
                               activebackground='#5DADE2', activeforeground='white', command=self.search)
        search_button.place(x=415, y=12, width=100, height=25)

    def create_table_frame(self):
        frame = Frame(self.root, bg='#F5F6FA')
        frame.place(x=213, y=82, width=1250, height=720)

        scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame, orient=VERTICAL)
        style = ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white",
                        bordercolor='#D5D8DC',
                        borderwidth=1)

        style.map('Treeview', background=[('selected', '#5DADE2')])

        self.student_table = ttk.Treeview(frame, columns=('id', 'name', 'email',  'cinsiyet'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        self.student_table.place(x=1, y=1, width=1200, height=697)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        for col in self.student_table["columns"]:
            self.student_table.heading(col, text=f"Öğrenci {col}")
            self.student_table.column(col, width=100)

        self.student_table['show'] = 'headings'
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_student(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute("INSERT INTO students (id, name, email, gender) VALUES (%s, %s, %s, %s)", (
            self.id_var.get(), self.name_var.get(), self.email_var.get(),  self.gender_var.get()
        ))
        con.commit()
        con.close()
        self.fetch_all()
        self.clear()

    def fetch_all(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        self.student_table.delete(*self.student_table.get_children())
        for row in rows:
            self.student_table.insert("", END, values=row)
        con.close()

    def delete(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE name=%s",
                    (self.dell_var.get(),))
        con.commit()
        con.close()
        self.fetch_all()

    def update(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute("UPDATE students SET name=%s, email=%s, gender=%s WHERE id=%s", (
            self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.id_var.get()
        ))
        con.commit()
        con.close()
        self.fetch_all()
        self.clear()

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.gender_var.set('')

    def open_grades_window(self):
        grades_win = Toplevel(self.root)
        grades_win.title("transkript")
        grades_win.geometry("800x500")
        grades_win.configure(bg='white')
        grades_win.resizable(False, False)

        Label(grades_win, text="transkript", font=(
            'Arial', 16), bg='white').pack(pady=10)

        columns = ('id', 'isim', 'yazılım_muh',
                   'veri_taban', 'mat1', 'ortalama')
        self.grades_table = ttk.Treeview(
            grades_win, columns=columns, show='headings')
        for col in columns:
            text = col.capitalize() if col != 'final' else 'Final'
            self.grades_table.heading(col, text=text)
            self.grades_table.column(col, width=100)
        self.grades_table.pack(fill=BOTH, expand=True, padx=20, pady=10)

        self.grades_table.bind("<ButtonRelease-1>",
                               self.open_student_grade_details)
        self.load_grades()

    def open_student_grade_details(self, event):
        selected = self.grades_table.focus()
        values = self.grades_table.item(selected)['values']
        if not values:
            return

        student_id, student_name = values[0], values[1]
        grade_win = Toplevel(self.root)
        grade_win.title(f"Transkript: {student_name}")
        grade_win.geometry("550x500")
        grade_win.configure(bg='white')

        Label(grade_win, text=f"Öğrenci: {student_name}", font=(
            'Arial', 14, 'bold'), bg='white').pack(pady=10)

        subjects = ['yazılım_muh', 'veri_taban', 'mat1']
        self.quiz_vars = {}
        self.exam_vars = {}
        self.final_labels = {}

        table_frame = Frame(grade_win, bg='white')
        table_frame.pack(pady=10)

        headers = ["Ders", "Vize", "Final", "Ortalama"]
        for j, header in enumerate(headers):
            Label(table_frame, text=header, bg='white', font=(
                'Arial', 10, 'bold')).grid(row=0, column=j, padx=10, pady=5)

        for i, subject in enumerate(subjects, start=1):
            Label(table_frame, text=subject.capitalize(), bg='white').grid(
                row=i, column=0, padx=10, pady=5, sticky='w')

            self.quiz_vars[subject] = StringVar()
            self.exam_vars[subject] = StringVar()

            Entry(table_frame, textvariable=self.quiz_vars[subject], width=7).grid(
                row=i, column=1, padx=5)
            Entry(table_frame, textvariable=self.exam_vars[subject], width=7).grid(
                row=i, column=2, padx=5)

            final_label = Label(table_frame, text="0", width=7, bg='#E8F8F5')
            final_label.grid(row=i, column=3, padx=5)
            self.final_labels[subject] = final_label

            self.quiz_vars[subject].trace(
                "w", lambda *_, s=subject: self.calculate_final(s))
            self.exam_vars[subject].trace(
                "w", lambda *_, s=subject: self.calculate_final(s))

        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute(
            "SELECT subject_id, quiz_mark, exam_mark FROM grades WHERE student_id=%s", (student_id,))
        grades = cur.fetchall()
        con.close()

        subj_map = {1: 'yazılım_muh', 2: 'veri_taban', 3: 'mat1'}
        for subject_id, quiz, exam in grades:
            field = subj_map.get(subject_id)
            if field:
                self.quiz_vars[field].set(quiz or 0)
                self.exam_vars[field].set(exam or 0)
                self.calculate_final(field)

        button_frame = Frame(grade_win, bg='white')
        button_frame.pack(pady=20)

        Button(button_frame, text="Kaydet", bg='#27AE60', fg='white',
               font=('Arial', 10, 'bold'),
               command=lambda: self.save_student_grades(student_id)).grid(row=0, column=0, padx=10)

        Button(button_frame, text="Yazdır", bg='#2980B9', fg='white',
               font=('Arial', 10, 'bold'),
               command=lambda: self.print_single_grade(
                   student_id, student_name)
               ).grid(row=0, column=1, padx=10)

    def calculate_final(self, subject):
        try:
            quiz = float(self.quiz_vars[subject].get())
            exam = float(self.exam_vars[subject].get())
            final = round((quiz * 0.4) + (exam * 0.6), 2)
        except ValueError:
            final = 0
        self.final_labels[subject].config(text=str(final))

    def save_student_grades(self, student_id):
        mapping = {'yazılım_muh': 1, 'veri_taban': 2, 'mat1': 3}
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()

        for subject, subj_id in mapping.items():
            try:
                q = float(self.quiz_vars[subject].get())
                e = float(self.exam_vars[subject].get())
            except ValueError:
                q, e = 0.0, 0.0

            cur.execute("""
                SELECT id
                  FROM grades
                 WHERE student_id=%s AND subject_id=%s
            """, (student_id, subj_id))
            exists = cur.fetchone()

            if exists:
                cur.execute("""
                    UPDATE grades
                       SET quiz_mark=%s, exam_mark=%s
                     WHERE student_id=%s AND subject_id=%s
                """, (q, e, student_id, subj_id))
            else:
                cur.execute("""
                    INSERT INTO grades (student_id, subject_id, quiz_mark, exam_mark)
                    VALUES (%s, %s, %s, %s)
                """, (student_id, subj_id, q, e))

        con.commit()
        con.close()
        messagebox.showinfo(
            " kaydedildi", "Öğrenci notları başarıyla kaydedildi!")
        self.load_grades()

    def load_grades(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        cur.execute("""
            SELECT s.id, s.name,
                ROUND(g1.quiz_mark*0.4 + g1.exam_mark*0.6, 2) AS yazılım_muh,
                ROUND(g2.quiz_mark*0.4 + g2.exam_mark*0.6, 2) AS veri_taban,
                ROUND(g3.quiz_mark*0.4 + g3.exam_mark*0.6, 2) AS language,
                ROUND(
                  ( (g1.quiz_mark*0.4 + g1.exam_mark*0.6)
                  + (g2.quiz_mark*0.4 + g2.exam_mark*0.6)
                  + (g3.quiz_mark*0.4 + g3.exam_mark*0.6)
                  )/3
                , 2) AS final
            FROM students s
            LEFT JOIN grades g1 ON s.id = g1.student_id AND g1.subject_id = 1
            LEFT JOIN grades g2 ON s.id = g2.student_id AND g2.subject_id = 2
            LEFT JOIN grades g3 ON s.id = g3.student_id AND g3.subject_id = 3
        """)
        rows = cur.fetchall()
        con.close()

        self.grades_table.delete(*self.grades_table.get_children())
        for row in rows:
            self.grades_table.insert("", END, values=row)

    
    def print_single_grade(self, student_id, student_name):
        file_name = f"transkript_{student_id}.pdf"
        c = canvas.Canvas(file_name, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, height - 50, f"Transkript: {student_name}")

        headers = ["Ders", "Vize", "Final", "Ortalama"]
        x_positions = [50, 200, 300, 380]
        y = height - 100
        c.setFont("Helvetica-Bold", 12)
        for i, header in enumerate(headers):
            c.drawString(x_positions[i], y, header)

        c.setFont("Helvetica", 11)
        y -= 20
        for subject in ['yazılım_muh', 'veri_taban', 'mat1']:
            try:
                q = float(self.quiz_vars[subject].get())
                e = float(self.exam_vars[subject].get())
            except (ValueError, KeyError):
                q, e = 0.0, 0.0
            f = round(q * 0.4 + e * 0.6, 2)

            c.drawString(x_positions[0], y, subject.capitalize())
            c.drawString(x_positions[1], y, str(q))
            c.drawString(x_positions[2], y, str(e))
            c.drawString(x_positions[3], y, str(f))
            y -= 20

        c.save()

        try:
            os.startfile(file_name)
        except AttributeError:
            import webbrowser
            webbrowser.open(file_name)

    def get_cursor(self, event):
        selected = self.student_table.focus()
        values = self.student_table.item(selected)['values']
        if values:
            self.id_var.set(values[0])
            self.name_var.set(values[1])
            self.email_var.set(values[2])
            self.gender_var.set(values[3])

    def search(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='student')
        cur = con.cursor()
        try:
            if self.se_by.get() not in ['id', 'name', 'email']:
                raise ValueError("Geçersiz arama ölçütü")
            query = f"SELECT * FROM students WHERE {self.se_by.get()} LIKE %s"
            cur.execute(query, ('%' + self.se_var.get() + '%',))
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        finally:
            con.close()

    def change_password(self):
        self.root.withdraw()
        pw_win = Toplevel()
        pw_win.title("Şifre Değiştir")
        pw_win.geometry("300x250")
        pw_win.configure(bg='white')
        pw_win.resizable(False, False)

        Label(pw_win, text="Kullanıcı Adı:", bg='white').pack(pady=5)
        username_entry = Entry(pw_win)
        username_entry.pack()

        Label(pw_win, text="Eski Şifre:", bg='white').pack(pady=5)
        old_pass_entry = Entry(pw_win, show='*')
        old_pass_entry.pack()

        Label(pw_win, text="Yeni Şifre:", bg='white').pack(pady=5)
        new_pass_entry = Entry(pw_win, show='*')
        new_pass_entry.pack()

        def save_new_password():
            con = pymysql.connect(
                host='localhost', user='root', password='', database='student')
            cur = con.cursor()
            cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s",
                        (username_entry.get(), old_pass_entry.get()))
            if cur.fetchone():
                cur.execute("UPDATE admin SET password=%s WHERE username=%s",
                            (new_pass_entry.get(), username_entry.get()))
                con.commit()
                messagebox.showinfo(
                    "Başarılı", "Şifre başarıyla değiştirildi!")
            else:
                messagebox.showerror("Hata", "Eski şifre yanlış!")
            con.close()
            pw_win.destroy()
            self.root.destroy()
            login_root = Tk()
            LoginPage(login_root)
            login_root.mainloop()

        Button(pw_win, text="Kaydet", bg='#3498DB', fg='white', activebackground='#5DADE2',
               activeforeground='white', command=save_new_password).pack(pady=15)
        pw_win.protocol("WM_DELETE_WINDOW", lambda: [
                        pw_win.destroy(), self.root.deiconify()])


if __name__ == "__main__":
    login_root = Tk()
    LoginPage(login_root)
    login_root.mainloop()

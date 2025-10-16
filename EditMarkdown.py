# Arquivo do Python
import tkinter as tk
import markdown
import sys

# Tenta importar o Text com a classe Tkinter, se não, usa a classe padrão
try:
    from tkinter.scrolledtext import ScrolledText as Text
except ImportError:
    from idlelib.colorizer import ColorDelegator
    from idlelib.percolator import Percolator

class MarkdownEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Markdown Editor")
        self.geometry("800x600")

        # Cria os painéis de texto
        self.text_editor = Text(self, wrap=tk.WORD, font=("Arial", 12))
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.text_editor.bind("<<Modified>>", self.update_preview)
        
        # Cria a pré-visualização (usando o Text widget para simplicidade)
        self.preview_text = Text(self, wrap=tk.WORD, font=("Arial", 12), state='disabled')
        self.preview_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def update_preview(self, event=None):
        markdown_text = self.text_editor.get("1.0", tk.END)
        html_output = markdown.markdown(markdown_text)

        # Atualiza o widget de pré-visualização
        self.preview_text.config(state='normal')
        self.preview_text.delete("1.0", tk.END)
        self.preview_text.insert("1.0", html_output)
        self.preview_text.config(state='disabled')
        self.text_editor.edit_modified(False)

if __name__ == "__main__":
    app = MarkdownEditor()
    app.mainloop()

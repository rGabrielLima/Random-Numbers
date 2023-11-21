import random
import time
import tkinter as tk

class RandomSum:
    def __init__(self):
        self.total_sum = 0
        self.results = {}
        self.xpos = 0

        self.root = tk.Tk()
        self.root.title("Teorema da Aleatoriedade")
        self.root.resizable(True, True)  # permite redimensionar a janela

        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()//2)
        self.canvas.pack(side=tk.BOTTOM)

        self.label_author = tk.Label(self.root, text="rGabrielDev", fg="#006400", font=("Arial", 15, "bold"))
        self.label_author.pack(side=tk.BOTTOM, pady=10)

        self.label_results = tk.Label(self.root, text="", font=("Arial", 8))
        self.label_results.pack(side=tk.RIGHT, padx=10)

        self.run()

    def run(self):
        while True:
            value1 = random.randint(0, 100)
            value2 = random.randint(0, 100)
            result = value1 + value2
            self.total_sum += result
            self.results[result] = self.results.get(result, 0) + 1

            self.update_display(value1, value2, result)

            time.sleep(0.1)

    def update_display(self, value1, value2, result):
        # Clear canvas
        self.canvas.delete("all")

        # Draw histogram
        max_count = max(self.results.values())
        if max_count == 0:
            max_count = 1
        bar_width = self.canvas.winfo_width() // 200
        for i in range(226):
            count = self.results.get(i, 0)
            height = self.canvas.winfo_height() * count // max_count
            xpos = i * bar_width
            ypos = self.canvas.winfo_height() - height
            self.canvas.create_rectangle(xpos, ypos, xpos + bar_width, self.canvas.winfo_height(), fill="#4169E1")
            self.canvas.create_text(xpos + bar_width//2, ypos - 10, text=f"{i}", font=("Arial", 1))

        # Draw current sum
        current_sum_text = f"{value1}+{value2} = {result}"

        # Draw results list
        sorted_results = sorted(self.results.items(), key=lambda x: x[1], reverse=True)
        results_text = ""
        for i in range(20):
            if i >= len(sorted_results):
                break
            result, count = sorted_results[i]
            percent = count / sum(self.results.values()) * 100
            results_text += f"{result}: {count} ({percent:.2f}%)\n"
        self.label_results.config(text=results_text)

        self.root.update()

RandomSum().root.mainloop()

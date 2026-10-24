import tkinter as tk
from tkinter import ttk
import psutil


class SystemMonitorApp:

  def __init__(self, root):
    self.root = root
    self.root.title("SUPER MEGA SIGMA ULTRA PRO VIP PLUS SYSTEM MONITOR (demo)(demo x2)(demo x3)(demo x4)(demo x5)(demo x6)(demo x7)(demo x8)(demo x9)(demo x10)")
    self.root.geometry("500x600")
    self.root.config(bg="#f4f4f4")
    self.root.resizable(False, False)

    # настройка
    style = ttk.Style()
    style.theme_use("clam")

    self.notebook = ttk.Notebook(root)
    self.notebook.pack(fill="both", expand=True)

    self.tab1 = ttk.Frame(self.notebook)
    self.tab2 = ttk.Frame(self.notebook)
    self.tab3 = ttk.Frame(self.notebook)

    self.notebook.add(self.tab1, text="Монитор")
    self.notebook.add(self.tab2, text="Процессы")
    self.notebook.add(self.tab3, text="Диаграмма")

    # шикарный заголовок
    title_label = tk.Label(
        self.tab1,
        text="ultra pro vip plus супер мега монитор системы",
        font=("Arial", 12, "bold"),
        bg="#f4f4f4",
        fg="#333",
    )
    title_label.pack(pady=10)

    # создание супер мега четко красивых визуалов
    self.create_widgets()

    # ракета с обновлением данных 
    self.update_data()
    self.update_processes()
    self.update_chart()

  def create_widgets(self):
    # процессор (CPU)
    cpu_frame = tk.LabelFrame(
        self.tab1,
        text=" процессор (CPU) ",
        bg="#f4f4f4",
        font=("Arial", 10, "bold"),
    )
    cpu_frame.pack(fill="x", padx=15, pady=5)

    self.cpu_label = tk.Label(
        cpu_frame, text="загрузка: 0%", bg="#f4f4f4", font=("Arial", 9)
    )
    self.cpu_label.pack(anchor="w", padx=10, pady=2)
    self.cpu_bar = ttk.Progressbar(
        cpu_frame, orient="horizontal", length=440, mode="determinate"
    )
    self.cpu_bar.pack(padx=10, pady=5)

    self.cpu_cores_label = tk.Label(
        cpu_frame, text="", bg="#f4f4f4", font=("Arial", 9), fg="#555"
    )
    self.cpu_cores_label.pack(anchor="w", padx=10, pady=2)

    # 🥀🥀🥀дорого🥀🥀🥀оперативка🥀🥀🥀
    ram_frame = tk.LabelFrame(
        self.tab1,
        text=" оперативная память (RAМ) ",
        bg="#f4f4f4",
        font=("Arial", 10, "bold"),
    )
    ram_frame.pack(fill="x", padx=15, pady=5)

    self.ram_label = tk.Label(
        ram_frame, text="использовано: 0%", bg="#f4f4f4", font=("Arial", 9), wraplength=460, justify="left"
    )
    self.ram_label.pack(anchor="w", padx=10, pady=2)
    self.ram_bar = ttk.Progressbar(
        ram_frame, orient="horizontal", length=440, mode="determinate"
    )
    self.ram_bar.pack(padx=10, pady=5)

    # диск (диск)
    disk_frame = tk.LabelFrame(
        self.tab1,
        text=" диск",
        bg="#f4f4f4",
        font=("Arial", 10, "bold"),
    )
    disk_frame.pack(fill="x", padx=15, pady=5)

    self.disk_label = tk.Label(
        disk_frame, text="использовано: 0%", bg="#f4f4f4", font=("Arial", 9)
    )
    self.disk_label.pack(anchor="w", padx=10, pady=2)
    self.disk_bar = ttk.Progressbar(
        disk_frame, orient="horizontal", length=440, mode="determinate"
    )
    self.disk_bar.pack(padx=10, pady=5)

    # сети и процессоры 
    info_frame = tk.LabelFrame(
        self.tab1,
        text=" сеть и процессы ",
        bg="#f4f4f4",
        font=("Arial", 10, "bold"),
    )
    info_frame.pack(fill="x", padx=15, pady=5)

    self.net_label = tk.Label(
        info_frame, text="сеть: отправлено и получено", bg="#f4f4f4", font=("Arial", 9)
    )
    self.net_label.pack(anchor="w", padx=10, pady=2)

    self.proc_label = tk.Label(
        info_frame, text="всего процессов: 0", bg="#f4f4f4", font=("Arial", 9)
    )
    self.proc_label.pack(anchor="w", padx=10, pady=2)

    self.tree_frame = ttk.Frame(self.tab2)
    self.tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

    self.tree = ttk.Treeview(
        self.tree_frame, columns=("name", "memory", "cpu"), show="headings"
    )
    self.tree.heading("name", text="Имя")
    self.tree.heading("memory", text="Память (%)")
    self.tree.heading("cpu", text="CPU (%)")

    self.tree.column("name", width=220)
    self.tree.column("memory", width=110)
    self.tree.column("cpu", width=110)

    # Настройка плавных цветов для градиента нагрузки процессов
    self.tree.tag_configure("lvl1", background="#e8f5e9")
    self.tree.tag_configure("lvl2", background="#f1f8e9")
    self.tree.tag_configure("lvl3", background="#fffde7")
    self.tree.tag_configure("lvl4", background="#fff3e0")
    self.tree.tag_configure("lvl5", background="#ffe0b2")
    self.tree.tag_configure("lvl6", background="#ffcdd2")

    tree_scroll = ttk.Scrollbar(
        self.tree_frame, orient="vertical", command=self.tree.yview
    )
    self.tree.configure(yscrollcommand=tree_scroll.set)

    self.tree.pack(side="left", fill="both", expand=True)
    tree_scroll.pack(side="right", fill="y")

    self.context_menu = tk.Menu(self.root, tearoff=0)
    self.context_menu.add_command(
        label="kill", command=self.kill_selected_process
    )
    self.tree.bind("<Button-3>", self.show_context_menu)

    self.chart_canvas = tk.Canvas(
        self.tab3, width=480, height=520, bg="white"
    )
    self.chart_canvas.pack(padx=10, pady=10)

  def show_context_menu(self, event):
    item = self.tree.identify_row(event.y)
    if item:
      self.tree.selection_set(item)
      self.context_menu.post(event.x_root, event.y_root)

  def kill_selected_process(self):
    selected_item = self.tree.selection()
    if selected_item:
      pid = int(selected_item[0])
      try:
        psutil.Process(pid).terminate()
        self.update_processes()
      except Exception:
        pass

  def update_data(self):
    # информация о процессах 
    physical_cores = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)

    # измеряем давление (нагрузку процессора)
    cpu_usage = psutil.cpu_percent(interval=None)

    self.cpu_label.config(text=f"нагрузка на процессоре: {cpu_usage}%")
    self.cpu_bar["value"] = cpu_usage
    self.cpu_cores_label.config(
        text=f"Физические ядра: {physical_cores} | Логических потоков: {total_cores}"
    )

    # измеряем пульс (оперативку) (оперативка дорого = страшно)
    # чтобы наши глаза не взорвались, мы из байтов переводим в мегабайты
    ram = psutil.virtual_memory()
    ram_used_mb = ram.used // (1024**2)
    ram_total_mb = ram.total // (1024**2)

    self.ram_label.config(
        text=f"использовано: {ram_used_mb} MB / {ram_total_mb} MB ({ram.percent}%)"
    )
    self.ram_bar["value"] = ram.percent

    # жестокое предупреждение
    if ram.percent > 60:
      self.ram_label.config(
          text=f"ВОУ ЩИТ БРОО, ЧТО С ОПЕРАТИВКОЙ?! ОНА БОЛЬШЕ 60%🥀🥀🥀: {ram_used_mb} MB / {ram_total_mb} MB ({ram.percent}%)",
          fg="red",
          font=("Arial", 9, "bold"),
      )
    else:
      self.ram_label.config(fg="black", font=("Arial", 9))

    # измеряем уровень кислорода (диск) здесь делаем красиво в гигабайтах
    disk = psutil.disk_usage('/')
    disk_used_gb = disk.used // (1024**3)
    disk_total_gb = disk.total // (1024**3)

    self.disk_label.config(
        text=f"использовано: {disk_used_gb} GB / {disk_total_gb} GB ({disk.percent}%)"
    )
    self.disk_bar["value"] = disk.percent

    # запускаемся в космос (что запущено)
    pids = psutil.pids()
    self.proc_label.config(text=f"процессы: {len(pids)}")

    # рыболовная сеть (сеть)
    net = psutil.net_io_counters()
    sent_mb = net.bytes_sent // (1024**2)
    recv_mb = net.bytes_recv // (1024**2)
    self.net_label.config(
        text=f"отправлено: {sent_mb} MB | получено: {recv_mb} MB"
    )

    # четкое обновление
    self.root.after(1000, self.update_data)

  def update_processes(self):
    for row in self.tree.get_children():
      self.tree.delete(row)

    procs = []
    for p in psutil.process_iter(["pid", "name", "memory_percent", "cpu_percent"]):
      try:
        procs.append(
            (
                p.info["pid"],
                p.info["name"],
                p.info["memory_percent"] or 0.0,
                p.info["cpu_percent"] or 0.0,
            )
        )
      except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

    procs.sort(key=lambda x: x[2], reverse=True)

    for p in procs[:50]:
      usage = p[2] + p[3]
      if usage < 2:
        tag = "lvl1"
      elif usage < 5:
        tag = "lvl2"
      elif usage < 15:
        tag = "lvl3"
      elif usage < 30:
        tag = "lvl4"
      elif usage < 60:
        tag = "lvl5"
      else:
        tag = "lvl6"

      self.tree.insert(
          "",
          "end",
          iid=str(p[0]),
          values=(p[1], f"{p[2]:.1f}%", f"{p[3]:.1f}%"),
          tags=(tag,),
      )

    self.root.after(3000, self.update_processes)

  def update_chart(self):
    self.chart_canvas.delete("all")

    procs = []
    for p in psutil.process_iter(["name", "memory_percent"]):
      try:
        procs.append((p.info["name"], p.info["memory_percent"] or 0.0))
      except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

    procs.sort(key=lambda x: x[1], reverse=True)
    top = procs[:5]
    other_sum = sum(p[1] for p in procs[5:])

    chart_data = [(name, mem) for name, mem in top if mem > 0]
    if other_sum > 0:
      chart_data.append(("другие (а вот кто гадай сам)", other_sum))

    total_mem = sum(mem for _, mem in chart_data)
    if total_mem == 0:
      total_mem = 1

    colors = ["#a8dadc", "#457b9d", "#1d3557", "#db2231", "#f1faee", "#b5838d"]

    start_angle = 0
    cx, cy, r = 240, 150, 100

    self.chart_canvas.create_text(
        240,
        30,
        text="кто больше жрет оперативки (которая дорогая🥀🥀🥀)",
        font=("Arial", 12, "bold"),
        fill="#333",
    )

    for i, (name, mem) in enumerate(chart_data):
      extent = (mem / total_mem) * 360
      color = colors[i % len(colors)]

      self.chart_canvas.create_arc(
          cx - r,
          cy - r,
          cx + r,
          cy + r,
          start=start_angle,
          extent=extent,
          fill=color,
          outline="white",
          width=2,
      )

      leg_y = 280 + (i * 22)
      self.chart_canvas.create_rectangle(
          50, leg_y, 65, leg_y + 12, fill=color, outline=""
      )
      self.chart_canvas.create_text(
          75,
          leg_y + 6,
          text=f"{name}: {mem:.1f}%",
          anchor="w",
          font=("Arial", 9),
      )

      start_angle += extent

    self.root.after(4000, self.update_chart)


if __name__ == "__main__":
  root = tk.Tk()
  app = SystemMonitorApp(root)
  root.mainloop()
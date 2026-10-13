# rubiks_ursina.py
# Ursina-based stable Rubik's Cube visualizer
# Make sure: pip install ursina
#
from ursina import *
from ursina.prefabs.editor_camera import EditorCamera
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re
import time

# -----------------------
# Basic cube model
# -----------------------
FACE_NAMES = ['U','D','L','R','F','B']
COLOR_CHARS = ['y','w','b','g','r','o']
COLOR_MAP = {
    'y': color.yellow,
    'w': color.white,
    'b': color.blue,
    'g': color.green,
    'r': color.red,
    'o': color.rgb(255,165,0),
    'x': color.gray
}

def solved_cube():
    return [[COLOR_CHARS[i] for _ in range(9)] for i in range(6)]

def clone_cube(c):
    return [f[:] for f in c]

def rotate_face(face):
    f = face[:]
    return [f[6],f[3],f[0], f[7],f[4],f[1], f[8],f[5],f[2]]

def move_U(c):
    c2 = clone_cube(c)
    c2[0] = rotate_face(c2[0])
    f = c[4][0:3]; r = c[3][0:3]; b = c[5][0:3]; l = c[2][0:3]
    c2[4][0:3] = r
    c2[3][0:3] = b
    c2[5][0:3] = l
    c2[2][0:3] = f
    return c2

def move_Ui(c): return move_U(move_U(move_U(c)))
def move_U2(c): return move_U(move_U(c))

def move_D(c):
    c2 = clone_cube(c)
    c2[1] = rotate_face(c2[1])
    f = c[4][6:9]; r = c[3][6:9]; b = c[5][6:9]; l = c[2][6:9]
    c2[4][6:9] = l
    c2[3][6:9] = f
    c2[5][6:9] = r
    c2[2][6:9] = b
    return c2

def move_Di(c): return move_D(move_D(move_D(c)))
def move_D2(c): return move_D(move_D(c))

def move_L(c):
    c2 = clone_cube(c)
    c2[2] = rotate_face(c2[2])
    u = [c[0][0],c[0][3],c[0][6]]
    f = [c[4][0],c[4][3],c[4][6]]
    d = [c[1][0],c[1][3],c[1][6]]
    b = [c[5][8],c[5][5],c[5][2]]
    c2[0][0],c2[0][3],c2[0][6] = f
    c2[4][0],c2[4][3],c2[4][6] = d
    c2[1][0],c2[1][3],c2[1][6] = b
    c2[5][8],c2[5][5],c2[5][2] = u
    return c2

def move_Li(c): return move_L(move_L(move_L(c)))
def move_L2(c): return move_L(move_L(c))

def move_R(c):
    c2 = clone_cube(c)
    c2[3] = rotate_face(c2[3])
    u = [c[0][2],c[0][5],c[0][8]]
    f = [c[4][2],c[4][5],c[4][8]]
    d = [c[1][2],c[1][5],c[1][8]]
    b = [c[5][6],c[5][3],c[5][0]]
    c2[0][2],c2[0][5],c2[0][8] = b
    c2[4][2],c2[4][5],c2[4][8] = u
    c2[1][2],c2[1][5],c2[1][8] = f
    c2[5][6],c2[5][3],c2[5][0] = d
    return c2

def move_Ri(c): return move_R(move_R(move_R(c)))
def move_R2(c): return move_R(move_R(c))

def move_F(c):
    c2 = clone_cube(c)
    c2[4] = rotate_face(c2[4])
    u = [c[0][6],c[0][7],c[0][8]]
    r = [c[3][0],c[3][3],c[3][6]]
    d = [c[1][2],c[1][1],c[1][0]]
    l = [c[2][8],c[2][5],c[2][2]]
    c2[0][6],c2[0][7],c2[0][8] = l
    c2[3][0],c2[3][3],c2[3][6] = u
    c2[1][2],c2[1][1],c2[1][0] = r
    c2[2][8],c2[2][5],c2[2][2] = d
    return c2

def move_Fi(c): return move_F(move_F(move_F(c)))
def move_F2(c): return move_F(move_F(c))

def move_B(c):
    c2 = clone_cube(c)
    c2[5] = rotate_face(c2[5])
    u = [c[0][2],c[0][1],c[0][0]]
    l = [c[2][0],c[2][3],c[2][6]]
    d = [c[1][6],c[1][7],c[1][8]]
    r = [c[3][8],c[3][5],c[3][2]]
    c2[0][2],c2[0][1],c2[0][0] = r
    c2[2][0],c2[2][3],c2[2][6] = u
    c2[1][6],c2[1][7],c2[1][8] = l
    c2[3][8],c2[3][5],c2[3][2] = d
    return c2

def move_Bi(c): return move_B(move_B(move_B(c)))
def move_B2(c): return move_B(move_B(c))

MOVE_FUNCS = {
    "U":move_U, "U'":move_Ui, "U2":move_U2,
    "D":move_D, "D'":move_Di, "D2":move_D2,
    "L":move_L, "L'":move_Li, "L2":move_L2,
    "R":move_R, "R'":move_Ri, "R2":move_R2,
    "F":move_F, "F'":move_Fi, "F2":move_F2,
    "B":move_B, "B'":move_Bi, "B2":move_B2
}

def tokenize_formula(s):
    return re.findall(r"(U2|U'|U|D2|D'|D|L2|L'|L|R2|R'|R|F2|F'|F|B2|B'|B)", s)

def invert_token(t):
    if t.endswith("2"): return t
    if t.endswith("'"): return t[:-1]
    return t + "'"
# -----------------------
# facelet → cubie mapping
# -----------------------
def facelet_mapping():
    mapping = []
    for face in FACE_NAMES:
        for r in range(3):
            for c in range(3):
                u = -1 + c
                v =  1 - r
                if face == 'U':
                    pos = (u, 1, v)
                    dirc = 'U'
                elif face == 'D':
                    pos = (u, -1, -v)
                    dirc = 'D'
                elif face == 'F':
                    pos = (u, v, 1)
                    dirc = 'F'
                elif face == 'B':
                    pos = (-u, v, -1)
                    dirc = 'B'
                elif face == 'L':
                    pos = (-1, v, -u)
                    dirc = 'L'
                else:  # R
                    pos = (1, v, u)
                    dirc = 'R'
                mapping.append((face, r*3+c, pos, dirc))
    return mapping

FACELET_MAP = facelet_mapping()
cubie_face_lookup = {}
for face, idx, pos, dirc in FACELET_MAP:
    cubie_face_lookup.setdefault(pos, {})[dirc] = (face, idx)

# --------------------------------
# Ursina 3D Visualizer
# --------------------------------
class RubikApp(Ursina):
    def __init__(self, initial_cube, steps):
        super().__init__()
        window.color = color.rgb(240,240,240)
        window.title = "Rubik's Cube 3D Visualizer (Ursina)"

        self.camera = EditorCamera(rotation_smoothing=0.2, enabled=True)

        self.cube = initial_cube
        self.steps = steps
        self.current_step = 0
        self.playing = (len(steps) > 0)
        self.paused = False

        self.anim_axis = None
        self.anim_layer = None
        self.anim_dir = 1
        self.anim_start = 0
        self.anim_duration = 0.25

        self.pause_after = 1.0
        self.pause_timer = None

        self.base = Entity()
        self.cubies = {}
        self._create_cubies()
        self.apply_facelet_colors()

        self.pause_btn = Button(
            text='Pause',
            color=color.azure,
            scale=(0.12,0.06),
            position=(-0.75,0.4)
        )
        self.pause_btn.on_click = self.toggle_pause

        self.info = Text(
            text=self.status_text(),
            position=(-0.75,0.32),
            color=color.black,
            scale=1.0
        )

        self._keyboard_loop()

    # ----------------------
    def _keyboard_loop(self):
        def check():
            if held_keys['space']:
                self.toggle_pause()
            if held_keys['r']:
                self.reset_cube()
        invoke(check, delay=0.15, loop=True)

    # ----------------------
    def status_text(self):
        return f"Step {self.current_step}/{len(self.steps)}  " + ("PAUSED" if self.paused else "")

    # ----------------------
    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_btn.text = "Resume" if self.paused else "Pause"
        self.info.text = self.status_text()

    # ----------------------
    def reset_cube(self):
        self.cube = solved_cube()
        self.steps = []
        self.current_step = 0
        self.playing = False
        self.apply_facelet_colors()
        self.info.text = self.status_text()

    # ----------------------
    def _create_cubies(self):
        spacing = 1.05
        for x in (-1,0,1):
            for y in (-1,0,1):
                for z in (-1,0,1):
                    parent = Entity(
                        parent=self.base,
                        position=(x*spacing,y*spacing,z*spacing),
                        model='cube',
                        color=color.gray,
                        visible=False
                    )
                    faces = {}
                    face_defs = [
                        ((0,0,0.51),(0,0,0),'F'),
                        ((0,0,-0.51),(0,180,0),'B'),
                        ((0,0.51,0),(90,0,0),'U'),
                        ((0,-0.51,0),(-90,0,0),'D'),
                        ((0.51,0,0),(0,90,0),'R'),
                        ((-0.51,0,0),(0,-90,0),'L')
                    ]
                    for pos, rot, d in face_defs:
                        quad = Entity(
                            parent=parent,
                            model='quad',
                            double_sided=True,
                            position=pos,
                            rotation=rot,
                            scale=(0.98,0.98)
                        )
                        faces[d] = quad

                    self.cubies[(x,y,z)] = {'parent': parent, 'faces': faces}

    # ----------------------
    def apply_facelet_colors(self):
        for (x,y,z), data in self.cubies.items():
            for d, quad in data['faces'].items():
                quad.color = color.gray
                lookup = cubie_face_lookup.get((x,y,z), {})
                if d in lookup:
                    faceName, idx = lookup[d]
                    ch = self.cube[FACE_NAMES.index(faceName)][idx]
                    quad.color = COLOR_MAP.get(ch, color.gray)

    # ----------------------
    def start_move(self):
        tok = self.steps[self.current_step]
        base = tok.replace("2","").replace("'","")
        axis_map = {
            'U':('y',1), 'D':('y',-1),
            'L':('x',-1), 'R':('x',1),
            'F':('z',1), 'B':('z',-1)
        }
        axis, layer = axis_map[base]
        self.anim_axis = axis
        self.anim_layer = layer
        self.anim_dir = -1 if tok.endswith("'") else 1
        self.anim_start = time.time()

    # ----------------------
    def commit_move(self):
        tok = self.steps[self.current_step]
        self.cube = MOVE_FUNCS[tok](self.cube)
        self.current_step += 1
        self.apply_facelet_colors()
        self.pause_timer = time.time()
        self.anim_axis = None
        self.info.text = self.status_text()

    # ----------------------
    def update(self):
        self.info.text = self.status_text()

        if not self.playing or self.paused:
            return

        # after animation, wait 1 sec
        if self.pause_timer is not None:
            if time.time() - self.pause_timer >= self.pause_after:
                self.pause_timer = None
                if self.current_step < len(self.steps):
                    self.start_move()
                else:
                    self.playing = False
            return

        # animation
        if self.anim_axis:
            elapsed = time.time() - self.anim_start
            frac = min(1.0, elapsed / self.anim_duration)
            ang = frac * 90 * self.anim_dir

            for (x,y,z), data in self.cubies.items():
                parent = data['parent']
                parent.rotation = (0,0,0)
                if self.anim_axis == 'x' and x == self.anim_layer:
                    parent.rotation_x = ang
                if self.anim_axis == 'y' and y == self.anim_layer:
                    parent.rotation_y = ang
                if self.anim_axis == 'z' and z == self.anim_layer:
                    parent.rotation_z = ang

            if frac >= 0.999:
                for info in self.cubies.values():
                    info['parent'].rotation = (0,0,0)
                self.commit_move()

        # idle start next move
        elif self.current_step < len(self.steps):
            self.start_move()

# --------------------------------
# tkinter 输入窗口
# --------------------------------
def show_input_window():
    root = tk.Tk()
    root.title("输入魔方状态 / scramble")
    tk.Label(root, text="选择输入方式：").grid(row=0,column=0,sticky='w')

    mode_var = tk.IntVar(value=2)
    tk.Radiobutton(root, text="54颜色 (y w b g r o) 顺序 U D L R F B", variable=mode_var, value=1)\
        .grid(row=1,column=0,sticky='w')
    tk.Radiobutton(root, text="打乱公式 (如: U R2 F' L...)", variable=mode_var, value=2)\
        .grid(row=2,column=0,sticky='w')

    tk.Label(root, text="输入内容：").grid(row=3,column=0,sticky='w')
    box = scrolledtext.ScrolledText(root, width=55, height=8)
    box.grid(row=4,column=0,padx=5,pady=5)

    def load_and_start():
        s = box.get("1.0","end").strip()
        if mode_var.get() == 2:
            toks = tokenize_formula(s)
            if not toks:
                messagebox.showerror("错误","无法识别公式")
                return
            cube = solved_cube()
            for t in toks:
                cube = MOVE_FUNCS[t](cube)
            steps = [invert_token(t) for t in reversed(toks)]
            root.destroy()
            RubikApp(cube, steps).run()
        else:
            arr = re.split(r'[\s,]+', s)
            arr = [x for x in arr if x]
            if len(arr) != 54:
                messagebox.showerror("错误", f"应输入54个颜色字符，目前 {len(arr)}")
                return
            faces = []
            for i in range(6):
                seg = arr[i*9:(i+1)*9]
                for ch in seg:
                    if ch not in COLOR_MAP:
                        messagebox.showerror("错误", f"未知颜色 {ch}")
                        return
                faces.append(seg)
            root.destroy()
            RubikApp(faces, []).run()

    tk.Button(root, text="开始", command=load_and_start).grid(row=5,column=0,pady=6)
    root.mainloop()

# --------------------------------
# main
# --------------------------------
if __name__ == "__main__":
    show_input_window()

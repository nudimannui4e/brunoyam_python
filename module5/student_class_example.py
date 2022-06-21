# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

class Student:
    tired = 0
    progress = 0

    def __init__(self, name):
        self.name = name

    def study(self):
        self.progress += 10
        self.tired += 15

    def relax(self):
        if self.tired > 5:
            self.tired -= 5
        else:
            self.tired = 0

    def is_done(self):
        if self.progress >= 100:
            print("Done")
        else:
            print("Not yet")


s = Student('Max')
for i in range(5):
    s.study()
    print(s.tired, s.progress)

print(s.name)

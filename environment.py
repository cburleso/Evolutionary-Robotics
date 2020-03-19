import constants as c

class ENVIRONMENT:
    def __init__(self, i):
        self.ID = i
        self.l = c.L
        self.w = c.L
        self.h = c.L
##        self.x = 0
##        self.y = 0
##        self.z = 0

        if self.ID == 0:
            self.Place_Light_Source_To_The_Front()

        print('Size (L-W-H):', self.l, '-', self.w, '-', self.h, '\nPosition (X-Y-Z):', self.x, '-', self.y, '-', self.z)

    def Place_Light_Source_To_The_Front(self):
        self.x = 0 
        self.y = c.L * 30 
        self.z = 0

    def Send_To(self, sim):
        self.lightSource = sim.send_box(position = (self.x, self.y, self.z), sides = (self.l, self.w, self.h), color = (0.5, 0.5, 0.5))

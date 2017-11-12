




class LinLine():
    
    def __init__(self, scale, limits, steps):
        self.scale = scale
        self.limits = limits if (limits[0] < limits[1]) else (limits[1],limits[0])
        self.steps = steps 
        self.segments = self.scale * "-" + "|"
        self.blank = self.scale * " "

    def __str__(self):
        return self.build_line()

    def __help__(self):
        print("""This Class deals with building a Numbered line.
                The Input of this class is defined as Follows:
                scale : <int> descripes how many hyphens shall be between
                        2 stepps on the line.
                limits: <tuple> describes at which number the line
                        begins, and where it ends.
                steps: <int> describes in how many smaller parts the intervall
                       given by the limits shall be sepparated.""")


    def build_line(self):
        rtrn_axis = ""
        rtrn_index = ""
        # how many Steps are needed ?
        difference = self.limits[1] -self.limits[0]
        intervall = difference / self.steps      
        # build the Line
        rtrn_axis += "|" + self.steps * self.segments + "-->"
        rtrn_index = "{}".format(float(self.limits[0])) 
        for index in range(1,  self.steps+1):
            rtrn_index += self.blank +"{}".format(self.limits[0] + index*intervall)

        return rtrn_axis + "\n" + rtrn_index



        
l= LinLine(steps=2, limits=(-3,-1), scale=10)
l.__help__()
print(l)



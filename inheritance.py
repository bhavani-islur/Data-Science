class parent:
    
    def __init__(self,f,m,nv):
        self.father=f
        self.mother=m
        self.netvalue=nv
    
    def parent_info(self):
        return f"{self.father} and {self.mother} has left {self.netvalue}"
    

class child(parent):
    
    def __init__(self, f, m, nv,cn,ca,cp):
        super().__init__(f, m, nv)
        self.child_name=cn
        self.child_age=ca
        self.child_profesion=cp
    
    def child_info(self):
        return f"{self.child_name} has his paretns {self.father} has net value {self.netvalue}"
    
# this grandchild class can have both the properties of child and parent
class grandchild(child):
    pass

gc=grandchild("a","b",54,"c",23,"e")
print(gc.child_age)
print(gc.parent_info())
print(gc.child_info())
class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f'{Point(self.x,self.y)}')
    def move(self, x1, y1):
        self.x+=x1
        self.y+=y1
    def dist(self, endpoint):
        dist_x=self.x-endpoint.x
        dist_y=self.y-endpoint.y
        return (dist_x**2+dist_y**2)**0.5

a = int(input()) 
b = int(input())  
c = int(input())  
d = int(input())   

p1 = Point(a, b)
p2 = Point(c, d)
print(p1.show())
print(p2.show())
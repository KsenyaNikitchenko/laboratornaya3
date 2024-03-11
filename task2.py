N=10
print("Задание 2. Вариант ",(N-1)%15+1,"Необходимо предусмотреть генерацию и обработку исключений для возможных ошибочных ситуаций")
class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print(self):
        return "".join(["[",str(self.x),"; ",str(self.y),"]"])
    
    def dist(self,point):
        return ((self.x-point.x)**2+(self.y-point.y)**2)**0.5
    
    def move(self,x,y):
        self.x+=x
        self.y+=y

class Triangle:

    def __init__(self,points):
        if not len(points)==3:
            raise Exception("В массиве должно быть 3 точки")
        self.points=points
        self.a=self.points[0].dist(self.points[1])
        self.b=self.points[1].dist(self.points[2])
        self.c=self.points[0].dist(self.points[2])

    def square(self):
        p=(self.a+self.b+self.c)/2
        return pow(p*(p-self.a)*(p-self.b)*(p-self.c),0.5)
    
    def print(self):
        print("Треугольник со сторонами",round(self.a,4),",",round(self.b,5),",",round(self.c,5))

    def move(self,x,y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Смещение по осями должно быть числом")
        for point in self.points:
            point.move(x,y)
        print("Кооординаты вершин треугольника были сдвинуты на",str(x),"по оси абсцисс и на",str(y),"по оси ординат")

    def coordinates(self):
        temp="Вершины треугольника имеют следующие координаты:"
        for point in self.points:
            temp+=" "+point.print()
        print(temp)

    def point_in_triangle(self,point):
        triangle1=Triangle([self.points[0],self.points[1],point])
        triangle2=Triangle([self.points[1],self.points[2],point])
        triangle3=Triangle([self.points[0],self.points[2],point])
        all_square=triangle1.square()+triangle2.square()+triangle3.square()
        return self.square()==all_square
    
    def is_intersect(self,figure):
        if len(figure.points)==3:
            result="Треугольники"
        else:
            result="Фигуры"
        if any(self.point_in_triangle(point) for point in figure.points):
            result+= " пересекаются"
        else:
            result+= " не пересекаются"
        return result
        
class Pentagon:

    def __init__(self,points):
        if not len(points)==5:
            raise Exception("В массиве должно быть 5 точек")
        self.points=points

    def move(self,x,y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Смещение по осями должно быть числом")
        for point in self.points:
            point.move(x,y)
        print("Кооординаты вершин пятиугольника были сдвинуты на",str(x),"по оси абсцисс и на",str(y),"по оси ординат")

    def coordinates(self):
        temp="Вершины пятиугольника имеют следующие координаты:"
        for point in self.points:
            temp+=" "+point.print()
        print(temp)

    def square(self):
        sumxy=self.points[-1].x*self.points[0].y
        sumyx=self.points[-1].y*self.points[0].x
        for i in range(1,len(self.points),+1):
            sumxy+=self.points[i-1].x*self.points[i].y
            sumyx+=self.points[i-1].y*self.points[i].x
        square=(sumxy-sumyx)/2
        return abs(square)
    
    def point_in_pentagon(self,point):
        result=False
        j=len(self.points)-1
        for i in range(len(self.points)):
            if((self.points[i].y<point.y and self.points[j].y>=point.y) or (self.points[j].y<point.y and self.points[i].y>=point.y)) and \
                (self.points[i].x+(point.y-self.points[i].y)/(self.points[j].y-self.points[i].y)*(self.points[j].x-self.points[i].x)<point.x):
                result=not result
            j=i
        return result
    
    def is_intersect(self,figure):
        if len(figure.points)==5:
            result="Пятиугольники"
        else:
            result="Фигуры"
        if any(self.point_in_pentagon(point) for point in figure.points):
            result+= " пересекаются"
        else:
            result+= " не пересекаются"
        return result


points3=[Point(0,0),Point(5,0),Point(5,2)]
triangle1=Triangle(points3)
triangle1.coordinates()

triangle1.move("0.3",2)
points5=[Point(-3,-2),Point(-1,4),Point(6,1),Point(3,10),Point(-4,9)]
pentagon1=Pentagon(points5)
pentagon1.coordinates()
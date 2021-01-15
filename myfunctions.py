from browser import svg

def example_text():
    return "this file comes from myfunctions.py"

def draw_star(canvas):
    canvas <= svg.polygon(fill="red", stroke="blue", stroke_width="10",
                    points=""" 75,38  90,80  135,80  98,107
                                111,150 75,125  38,150 51,107
                                15,80  60,80""")

def mouseenter(ev):
    document["trace1"].text = f'entering {ev.currentTarget.id}'

def mouseleave(ev):
    document["trace1"].text = f'leaving {ev.currentTarget.id}'

def draw_circle(paper,x,y):    
    # Creates circle at x,y with radius 10
    circle = paper.circle(x, y, 10)
    
    # Sets the fill attribute of the circle to red (#f00)
    circle.attr("fill", "#f00")
    
    # Sets the stroke attribute of the circle to white
    circle.attr("stroke", "#fff")

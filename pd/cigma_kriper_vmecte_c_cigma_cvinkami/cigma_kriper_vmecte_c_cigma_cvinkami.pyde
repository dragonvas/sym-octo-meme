q=0
def setup():
    size(1000,1000)
    # textAlign(CENTER,CENTER)
    textSize(20)
    fill(255)
def draw():
    global q
    background(0,0,0)
    rect (400,400,200,200)
    text (u'слоны:',450,100)
    text (q,520,100)
def mouseClicked():
    global q
    if mouseX > 400 and mouseX < 600 and mouseY > 400 and mouseY < 600:
        q=q+1
    

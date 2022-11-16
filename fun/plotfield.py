import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def createPitch():
    
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,80], color="black")
    plt.plot([0,120],[80,80], color="black")
    plt.plot([120,120],[0,80], color="black")
    plt.plot([0,120],[0,0], color="black")
    plt.plot([60,60],[0,80], color="black")
    
    #Left Penalty Area
    plt.plot([0,18],[62,62],color="black")
    plt.plot([0,18],[18,18],color="black")
    plt.plot([18,18],[18,62],color="black")
    
    #Right Penalty Area
    plt.plot([120,102],[62,62],color="black")
    plt.plot([120,102],[18,18],color="black")
    plt.plot([102,102],[18,62],color="black")
    
    #Left 6-yard Box
    plt.plot([0,6],[50,50],color="black")
    plt.plot([0,6],[30,30],color="black")
    plt.plot([6,6],[30,50],color="black")
    
    #Right 6-yard Box
    plt.plot([120,114],[50,50],color="black")
    plt.plot([120,114],[30,30],color="black")
    plt.plot([114,114],[30,50],color="black")
    
    #Prepare Circles
    centreCircle = plt.Circle((60,40),9.15,color="black",fill=False)
    centreSpot = plt.Circle((60,40),0.5,color="black")
    leftPenSpot = plt.Circle((12,40),0.5,color="black")
    rightPenSpot = plt.Circle((108,40),0.5,color="black")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((12,40),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
    rightArc = Arc((108,40),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    #Tidy Axes
    plt.axis('off')
    
    #Display Pitch
    plt.show()
    
createPitch()
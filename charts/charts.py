import matplotlib.pyplot as plot

def generate():
    labels=['a','b','c']
    values=[100,43,78]

    fig,ax=plot.subplots()
    ax.pie(values,labels=labels)
    plot.savefig('pie.png')
    plot.close()
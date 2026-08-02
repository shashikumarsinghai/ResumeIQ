import matplotlib.pyplot as plt

def skill_chart(matched, missing):
    labels = ["Matched Skills", "Missing Skills"]
    sizes = [len(matched), len(missing)]

    colors = ['#4CAF50', '#F44336']  # Green for matched, Red for missing
    explode = (0.02, 0.02) # explode the first slice (Matched Skills)
    
    fig, ax = plt.subplots(figsize=(3, 3), dpi = 100)

    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        pctdistance=0.72,
        labeldistance=1.08,
        startangle=90,
        radius=0.7,
        wedgeprops=dict(width=0.35, edgecolor='white')
    )
    
    plt.tight_layout()
    plt.setp(autotexts, color='white', fontsize=11, fontweight="bold")
    plt.setp(texts, fontsize=10)

    ax.set_title("Resume Skills Analysis", fontsize=15, fontweight="bold")
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return fig 
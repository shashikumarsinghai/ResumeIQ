import matplotlib.pyplot as plt

def skill_chart(matched, missing):
    labels = ["Matched", "Missing"]
    values = [len(matched), len(missing)]

    fig, ax = plt.subplots(figsize=(5, 3))

    ax.bar(labels, values)

    ax.set_title("Skills Analysis")

    return fig
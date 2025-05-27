import matplotlib.pyplot as plt
import os

def generate_charts(slides):
    chart_paths = []
    for slide in slides:
        if "Financial" in slide["title"] or "Market" in slide["title"]:
            fig, ax = plt.subplots()
            labels = ["Q1", "Q2", "Q3", "Q4"]
            values = [100, 200, 300, 400]
            ax.bar(labels, values)
            ax.set_title(slide["title"])
            path = f"output/{slide['title'].replace(' ', '_')}_chart.png"
            plt.savefig(path)
            chart_paths.append(path)
            plt.close()
        else:
            chart_paths.append(None)
    return chart_paths

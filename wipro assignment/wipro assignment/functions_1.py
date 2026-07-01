def sort_colors(color_string):
    colors = color_string.split("-")
    colors.sort()
    return "-".join(colors)
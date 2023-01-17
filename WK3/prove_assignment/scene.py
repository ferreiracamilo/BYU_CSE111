# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import start_drawing, draw_line, draw_oval, draw_arc, draw_rectangle, draw_polygon, draw_text, finish_drawing, draw_vertical_gradient, draw_circle_with_vert_grad
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_street(canvas, scene_width, scene_height)
    draw_bus_stop(canvas, scene_width, scene_height)
    draw_building(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, scene_width/22*18, 100, 200)
    draw_pine_tree(canvas, scene_width/22*21, 100, 130)
    draw_circle_with_vert_grad(canvas, round(scene_width/22*3), round(scene_height/22*18), round(scene_height/22*3), [161,161,156], [240,239,226])
    
    #Your program must be divided into functions such as draw_sky, draw_cloud, draw_ground, draw_bird, draw_flower, draw_insect, draw_fish, or draw_snowman.
    #draws objects in the order of farthest away to nearest. For example, you program should draw the sky first, then clouds, then the ground, then trees, then insects in the trees. Be creative.

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_street(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 5, width=0, fill="snow3")
    for x in range(10, scene_width, 50):
        draw_line(canvas, x, (scene_height / 5)/2, x+20, (scene_height / 5)/2, width=5, fill="gray99")

def draw_bus_stop(canvas, scene_width, scene_height):
    #initial structure
    draw_rectangle(canvas, scene_width/11, scene_height / 5, (scene_width/11)*2, (scene_height / 5) * 2, width=2, outline="tomato3")
    #advertising with text and light/lamp
    draw_rectangle(canvas, scene_width/11-12, (scene_height / 5) * 2, (scene_width/11)*2+12, (scene_height / 5) * 2 + 20, width=2,fill = "tomato3", outline="tomato3")
    draw_text(canvas, scene_width/11 + (scene_width/11)/2 , (scene_height / 5) * 2 + 10 , "BUS STOP", fill="black")
    draw_oval(canvas, scene_width/26*3, (scene_height / 5) * 2 - 10, scene_width/26*4, (scene_height / 5) * 2, width=0, outline="khaki1", fill="khaki1")

def draw_building(canvas, scene_width, scene_height):
    #Draw building structure
    draw_rectangle(canvas, (scene_width/11)*3, scene_height / 5, (scene_width/11)*8, scene_height, width=2, fill="skyBlue3", outline="skyBlue3")
    #Draw building windows
    for x in range(round((scene_width/11)*3)+8, round((scene_width/11)*8), 20):
        for y in range(round(scene_height / 5)*2,scene_height,20):
            if random.randint(0, 1) == 1:
                #if random gives 1, that means the flat lights are turned on
                draw_rectangle(canvas, x, y, x+10, y+10, width=0, fill="khaki1")
            else:
                draw_rectangle(canvas, x, y, x+10, y+10, width=0, fill="ivory1")
    #Draw door
    draw_rectangle(canvas, (scene_width/11)*5, scene_height / 5, (scene_width/11)*6, scene_height / 5 * 2 - 10, width=2, fill="oliveDrab1", outline="yellow3")
    draw_vertical_gradient(canvas, round((scene_width/22)*11), round(scene_height / 5), [76,69,57], round((scene_width/22)*12), round(scene_height / 5 * 2 - 10), [76,110,55])

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 5, scene_width, scene_height, width=0, fill="gray19")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

# Call the main function so that
# this program will start executing.
main()
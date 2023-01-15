# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    #Your program must be divided into functions such as draw_sky, draw_cloud, draw_ground, draw_bird, draw_flower, draw_insect, draw_fish, or draw_snowman.
    #draws objects in the order of farthest away to nearest. For example, you program should draw the sky first, then clouds, then the ground, then trees, then insects in the trees. Be creative.


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.



# Call the main function so that
# this program will start executing.
main()
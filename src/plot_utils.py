"""
 
 plot_utilities.py (author: Anson Wong / git: ankonzoid)

"""
import matplotlib.pyplot as plt
import random

def plot_query_answer(x_query=None, x_answer=None, filename=None, gray_scale=False, n=4):

    # n = maximum number of answer images to provide
    plt.clf()
    plt.figure(figsize=(2*n, 4))

    # Plot query images
    #find image numbers:
    painting_labels= [random.randrange(1, 400) for _ in range(4)]
    for j, img in enumerate(x_query):
        if(j >= n):
            break
        ax = plt.subplot(2, n, j + 1)  # display original
        plt.imshow(img)
        ax.get_yaxis().set_visible(False)
        for axis in ['top', 'bottom', 'left', 'right']:
            ax.spines[axis].set_linewidth(4)  # increase border thickness
            ax.spines[axis].set_color('black')  # set to black
        ax.set_title("\n you like:\n",  fontsize=14)  # set subplot title
        ax.set_xlabel(" Check out these: ", fontsize = 14)
        plt.subplots_adjust(hspace=1.1)
    # Plot answer images
    for j, img in enumerate(x_answer):
        if (j >= n):
            break

        ax = plt.subplot(2, n, n + j + 1)  # display original
        plt.imshow(img)
        if gray_scale:
            plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        for axis in ['top', 'bottom', 'left', 'right']:
            ax.spines[axis].set_linewidth(1)  # set border thickness
            ax.spines[axis].set_color('black')  # set to black
        

        ax.set_title(painting_labels[j], fontsize=14)  # set subplot title

    if filename == None:
        plt.show()
    else:
        plt.savefig(filename, bbox_inches='tight')

    plt.close()
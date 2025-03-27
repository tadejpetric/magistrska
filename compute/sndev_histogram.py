import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm

from random_regular_networkx import random_regular
from utils import second_eigenvalue

def plot_second_eigenvalue_histogram(n_vertices, d, num_samples=100, bins=30,
                                     figsize=(5.90666, 6), save_pgf=False,
                                     pgf_filename="/home/tadej/magistrska/article/images/histogram.pgf"):
    """
    Generates a histogram of the second eigenvalues for random d-regular graphs.
    
    Parameters:
      n_vertices (int): Number of vertices in each graph.
      d (int): Degree of each vertex (the graph is d-regular).
      num_samples (int): How many random graphs to sample.
      bins (int): Number of bins in the histogram.
      figsize (tuple): Figure size for the plot.
      save_pgf (bool): If True, saves the plot as a PGF file.
      pgf_filename (str): The filename to use when saving the PGF file.
      
    The function either displays the plot or saves it as a PGF file (for direct inclusion in LaTeX).
    
    Note: Ensure that your functions `random_regular(n_vertices, d)` and
          `second_eigenvalue(A, d=None)` are defined in your environment.
    """
    # Collect second eigenvalues from each random graph.
    second_eigenvalues = []
    for i in tqdm(range(num_samples)):
        A = random_regular(n_vertices, d)  # User-defined function
        sec_eig = second_eigenvalue(A, d)    # User-defined function
        second_eigenvalues.append(sec_eig)
    
    # Create the histogram.
    plt.figure(figsize=figsize)
    plt.hist(second_eigenvalues, bins=bins, edgecolor='black', alpha=0.7)
    
    # Add a dashed vertical line at 2sqrt(d-1).
    threshold = 2 * np.sqrt(d - 1)
    plt.axvline(x=threshold, color='red', linestyle='--', linewidth=2, label=r'$2\sqrt{d-1}$')
    plt.xlabel('Lastna vrednost')
    plt.ylabel('Število grafov')
    #plt.legend()
    plt.tight_layout()
    
    if save_pgf:
        # Optional: update matplotlib settings for PGF output.
        matplotlib.rcParams.update({
            "pgf.texsystem": "pdflatex",  # or 'lualatex', 'xelatex'
            "font.family": "serif",
            "text.usetex": True,
            "pgf.rcfonts": False,
        })
        # Save the figure as a PGF file.
        plt.savefig(pgf_filename)
        print(f"PGF file saved to {pgf_filename}")
    else:
        plt.show()

# Example usage:
# To display the plot:
plot_second_eigenvalue_histogram(n_vertices=500, d=5, num_samples=10000, bins=30, save_pgf=True)

# To save the plot as a PGF file (to be included in LaTeX):
# plot_second_eigenvalue_histogram(n_vertices=100, d=3, num_samples=200, bins=20,
#                                  save_pgf=True, pgf_filename="histogram.pgf")

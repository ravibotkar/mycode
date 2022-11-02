#!/usr/bin/python3
"""Alta3 Research | treich@alta3.com
Creating a histogram plot using Matplotlib and Numpy"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg') # used to render graphs to files

def main():
  # Generate a numpy array to represent normally distributed test grades for 100 students
  grades = np.random.normal(75, 10, 100)

  # Create a histogram using bins from 0-100 spaced 10 apart
  plt.hist(grades,
           bins=np.arange(0, 101, 10),  # defines bin edges, including left and right edge
           linewidth=0.5,               
           edgecolor="white")

  # Customize plot with labels and axis ticks that align with the bins
  plt.title("Test Grades Distribution for 100 Students")
  plt.xticks(np.arange(0,101,10))
  plt.xlabel("Test Score")
  plt.ylabel("Number of Students")

  # Save the graph locally and to the static folder
  plt.savefig("/home/student/mycode/graphing/grades_hist.png")
  plt.savefig("/home/student/static/grades_hist.png")
  
if __name__ == "__main__":
   main()


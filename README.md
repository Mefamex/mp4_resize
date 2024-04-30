# mp4_resize
This Python script resizes a video using the MoviePy library. The script prints the current directory, loads the video, sets its height to 720 pixels, and writes the resized video to a new file.
## Discussion
If you have any questions or feedback , please feel free to contact me [Instagram](https://www.instagram.com/mefamex/).
## Contributors
* [Mefamex](https://github.com/Mefamex)

# Requirements
- Python 3.6 or later
- MoviePy library

# Installation
- You can install the MoviePy library using pip:

``Bash
pip install moviepy``

# Usage
To run the script, use the following command:

``Bash
python mp4_resize.py``

This will print the current directory, load the video from the file "a.mp4", set the video's height to 720 pixels, and write the resized video to the file "movie_resized.mp4" .

# Notes
- You will need to change the file paths in the script to your own file paths.
- To preserve the aspect ratio of the video, the script sets the height and calculates the width automatically.
- To resize to a different resolution, see the documentation for the clip_resized.resize() method

# Related Projects
* [FFmpeg](https://ffmpeg.org/)
* [OpenCV](https://opencv.org/)

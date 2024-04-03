# Simple HEIC to JPEG converter

A simple graphical app to bulk convert .heic images to .jpeg, written in Python using Tkinter & Pillow.

## Usage

You can either start the graphical app from `src/run.py`, or use the simple conversion script from `heic_convert.py` as command line tool. **Example:**

```
python3 heic_convert.py -d /home/user/Images/my_folder
```

will convert all .heic-files inside my\_folder.

You can also install it as a local command:

```
sudo cp heic_convert.py /usr/local/bin/heic-convert
```

Now you can run

```
heic-convert -d /path/to/folder
```

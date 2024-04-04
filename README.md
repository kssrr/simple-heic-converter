# Simple HEIC to JPEG converter

A simple tool to bulk convert all .heic files in a directory to .jpeg or .png using Pillow, either on the command line or with a small tkinter-app (app only supports to .jpeg atm).

## Dependencies

For the command line tool, you only need to `pip install pillow-heif`.

## Usage

I recommend you use the simple conversion script from `heic_convert.py` as command line tool. **Example:**

```
python3 heic_convert.py /path/to/folder
```

will convert all .heic-files inside the provided directory. You can also install it as a local command:

```
sudo cp heic_convert.py /usr/local/bin/heic-convert
```

Now you can run

```
heic-convert /path/to/folder
```

Optionally, you can set the `-o` (or `--overwrite`) flag to overwrite/delete the original .heic files after conversion.

```
heic-convert -o /path/to/folder
```

By default, the script will convert .heic images to .jpeg. You can change to .png by setting the `-f` (or `--format`) argument:

```
heic-convert -f PNG /path/to/folder
```
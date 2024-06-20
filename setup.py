from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["tkinter", "unittest"],
}

setup(
    name="PlayThon",
    version="1.0",
    description="Video and Audio downloader",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="gui")],
)
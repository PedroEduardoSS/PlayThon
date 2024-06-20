import dearpygui.dearpygui as dpg
from pytube import YouTube as yt

dpg.create_context()

def download1():
    yt(dpg.get_value("url")).streams.filter(only_audio=True).first().download()

def download2():
    yt(dpg.get_value("url")).streams.first().download()
    
with dpg.window(tag="Primary Window"):
    dpg.add_text("PlayThon!")
    dpg.add_input_text(label="URL", tag="url")
    dpg.add_button(label="Download do Áudio", callback=download1)
    dpg.add_button(label="Download do video", callback=download2)

dpg.create_viewport(title='PlayThon', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
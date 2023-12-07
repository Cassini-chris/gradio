import gradio as gr
from pathlib import Path

base_root = Path(__file__).parent.resolve()

with gr.Blocks() as demo:
    with gr.Row():
        dd = gr.Dropdown(label="Select File Explorer Root",
                        value=str(base_root / "dir1"),
                        choices=[str(base_root / "dir1"), str(base_root / "dir2")])
        with gr.Group():
            dir_only_glob = gr.Checkbox(label="Show only directories", value=False)
            dir_only_glob_single = gr.Checkbox(label="Show only directories (single)", value=False)

    fe = gr.FileExplorer(root=str(base_root / "dir1"), interactive=True)
    textbox = gr.Textbox(label="Selected Directory")
    run = gr.Button("Run")
    
    dir_only_glob_single.select(lambda s: gr.FileExplorer(glob="**/" if s else "**/*.*",
                                                   file_count="single",
                                                   root=str(base_root / "dir3")) , inputs=[dir_only_glob_single], outputs=[fe])
    dir_only_glob.select(lambda s: gr.FileExplorer(glob="**/" if s else "**/*.*",
                                                   file_count="multiple",
                                                   root=str(base_root / "dir3")) , inputs=[dir_only_glob], outputs=[fe])
    dd.select(lambda s: gr.FileExplorer(root=s), inputs=[dd], outputs=[fe])
    run.click(lambda s: ",".join(s) if isinstance(s, list) else s, inputs=[fe], outputs=[textbox])


if __name__ == "__main__":
    demo.launch()
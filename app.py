import gradio as gr
from suggestions import main
from contents import PROMPT_INFO

CSS= """
    footer {visibility: hidden;}
    body {width: 60% !important; margin: 0 auto !important;}
"""

theme = gr.themes.Base(
    primary_hue="purple",
    secondary_hue="gray"
)

with gr.Blocks(
    css=CSS,
    fill_width=False,
    theme=theme,
    title="Books recs"
) as book_recs:
    with gr.Row():
        key = gr.Textbox(
            label="Chave da API Gemini",
            placeholder="Insira sua chave da API Gemini",
            type="password"
        )
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                info=PROMPT_INFO,
                label="Como posso ajudar você a encontrar sua próxima leitura?",
                lines=14,
                max_lines=14,
                placeholder="Digite aqui...",
                type="text"
            )

            submit_btn = gr.Button(
                "OK!",
                size="sm",
                variant="primary"
            )

        with gr.Column():
            response = gr.Textbox(
                label="Recomendações de livros",
                lines=18,
                max_lines=18,
                show_copy_button=True,
                type="text",
            )

    submit_btn.click(
        fn=main,
        inputs=[key, prompt],
        outputs=response
    )

book_recs.launch(favicon_path="favicon.ico")

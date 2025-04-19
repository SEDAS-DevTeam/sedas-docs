from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from tqdm import tqdm

import os
import torch


class Translator:
    # currently using M2M100_418M model from Meta AI https://huggingface.co/facebook/m2m100_418M
    def __init__(self, lang):
        self.checkpoint = "facebook/m2m100_418M"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = M2M100ForConditionalGeneration.from_pretrained(self.checkpoint).to(self.device)
        self.tokenizer = M2M100Tokenizer.from_pretrained(self.checkpoint)
        self.tokenizer.src_lang = "en"
        self.out_lang = lang

    def run(self, text):
        encoded = self.tokenizer(text, return_tensors="pt").to(self.device)
        generated_tokens = self.model.generate(**encoded, forced_bos_token_id=self.tokenizer.get_lang_id(self.out_lang))

        out = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return out[0]


class Rules:
    @staticmethod
    def is_header(line): #
        if "===" in line or "---" in line or "~~~" in line or "^^^" in line: return True

    @staticmethod
    def is_link_def(line):
        if "#." in line and ":ref:" in line: return True

    @staticmethod
    def is_link(line):
        if ".. _" in line and line[-1] == ":": return True

    @staticmethod
    def is_directive(line): #
        if ".." in line and "::" in line: return True

    @staticmethod
    def is_parameter(line): #
        if line[0] == ":" and line[-1] == ":": return True

    @staticmethod
    def is_code_block(line): #
        if ".. code-block::" in line: return True

    @staticmethod
    def is_table_block(line):
        if ".. list-table::" in line: return True

    @staticmethod
    def is_blank(line): #
        if len(line) == 0: return True


class RstIterator:
    def __init__(self, path):
        self.path = path

    def iterate(self, model: Translator):
        for file in os.listdir(self.path):
            if ".rst" not in file:
                continue

            in_code_block = False
            in_table_block = False
            is_space = False
            temp_iter = 0
            inp_lines = []
            translated_lines = []

            print(f"Translating {file}")

            file_path = os.path.join(self.path, file)

            # Read file contents
            with open(file_path, "r", encoding="utf-8") as rst_file:
                for line in rst_file:
                    inp_lines.append(line.strip())

            # Overwrite
            with open(file_path, "w", encoding="utf-8") as rst_file:
                for line_input in tqdm(inp_lines, desc=f"→ {file}", unit="line"):
                    if Rules.is_code_block(line_input):
                        in_code_block = True
                        temp_iter = 0
                    if Rules.is_table_block(line_input):
                        in_table_block = True
                        temp_iter = 0
                    if Rules.is_blank(line_input):
                        # Checking if code block exit/table block exit or just a newline before code

                        if temp_iter != 1 and in_code_block:
                            in_code_block = False
                            is_space = True
                        elif temp_iter != 1 and in_table_block:
                            in_table_block = False
                            is_space = True
                        else:
                            # still behaves like a space
                            is_space = True

                    # first checking blank spaces and code blocks, then directives
                    if in_code_block or in_table_block or is_space:
                        translated_lines.append(line_input + "\n")
                        is_space = False
                    elif Rules.is_directive(line_input) or \
                        Rules.is_parameter(line_input) or \
                        Rules.is_header(line_input) or \
                        Rules.is_link(line_input) or \
                            Rules.is_link_def(line_input):
                        translated_lines.append(line_input + "\n")
                    else:
                        # line is passing rules
                        model_out = model.run(line_input)
                        translated_lines.append(model_out + "\n")

                    temp_iter += 1

                rst_file.writelines(translated_lines)


if __name__ == "__main__":
    model = Translator()
    output = model.run("This is a SEDAS test")
    print(output)

#!/usr/bin/env python
import sys

import mistune
from mistune.plugins import plugin_strikethrough

import plugins
from renderer import UbbRenderer

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        input_name = sys.argv[1]
        output_name = "output.txt"
    else:
        input_name = sys.argv[1]
        output_name = sys.argv[2]


    with open(input_name, 'r', encoding='utf-8') as md_file:
        md_text = md_file.read()
        renderer = UbbRenderer(escape=False, hard_wrap=False)
        markdown = mistune.create_markdown(renderer=renderer, plugins=[plugins.plugin_table, plugin_strikethrough])
        with open(output_name, 'w', encoding='utf-8') as f:
            f.write(markdown(md_text))

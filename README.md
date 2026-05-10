# Generative Character  
  
Prototype of minimal generative AI for NPC in an open-world, non-linear game.  
  
## Instructions  
  
1. Run the `tools/download_model.py` script to import the token embedding model  
2. When making source edits, use `black` and `ruff` checks to ensure coding standards are adhered to  
3. Perform a `pip install -e .` from the CLI while in the project root folder to create the python package  
4. Boot up a local LLM server (I use llama.cpp) and load into it pre-trained weights (I use Mystral 7B instruct)  
5. Run the `generative-character` executable from the CLI  
6. Have fun!  
  
## Tips  
  
+ It works best to run `generative-character` in one terminal and the llama-cpp server in another. (Perfect use case for tmux on linux!)  

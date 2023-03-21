import torch
from diffusers import StableDiffusionPipeline

# model_id = "CompVis/stable-diffusion-v1-4"
# device = "cuda"
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# pipe = pipe.to(device)

model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]  
    
image.save("gen_image.png")

def image_generation_code(prompt):
    image = pipe(prompt).images[0]
    image.save("static/gen_image.png")
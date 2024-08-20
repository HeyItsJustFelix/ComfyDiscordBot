# To add new models, copy or change one of the existing parameters

models_config = {
    "models":{
        "Dreamshaper":{
            "name":"Dreamshaper", # This is the name the bot will use in the model selector
            "filename":"dreamshaperXL_sfwV2TurboDPMSDE.safetensors", # This is the filename of the model you want to use
            "scheduler":"karras", # Options are "normal", "karras", "exponential", "sgm_uniform", "simple", "ddim_uniform", "beta", find more info in comfyui's documentation
            "sampler":"dpmpp_sde", # Options are "euler", "euler_cfg_pp", "euler_ancestral", "euler_ancestral_cfg_pp", "heun", "heunpp2", "dpm_2", "dmp_2_ancestral", "lms", "dpm_fast", "dpm_adaptive", "dpmpp_2s_ancestral", "dpmpp_sde", "dpmpp_sde_gpu", "dpmpp_2m", "dpmpp_2m_sde", "dpmpp_2m_sde_gpu", "dpmpp_3m_sde", "dpmpp_3m_sde_gpu", "ddpm", "lcm", "ipndm", "ipndm_v", "deis", "ddim", "uni_pc", "uni_pc_bh2"
            "steps":8, # How many iterations to use on the model
            "cfg":2.0 # How "creative" the ai is with the prompt
        },
        "Yiffymix":{
            "name":"Yiffymix",
            "filename":"yiffymix_v52XL.safetensors",
            "scheduler":"normal",
            "sampler":"ddpm",
            "steps":17,
            "cfg":5.0
        }
    }
}
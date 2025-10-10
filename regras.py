def carregar_regras(teatro):
    if teatro == "Teatro dos Grandes Atores":
        return {
            "divertix_home": {
                "descricao": "Divertix Home do Site – 370 x 550 px",
                "largura": 370,
                "altura": 550,
                "formato_final": ("JPEG", "PNG"),
                "modo_cor": "RGB",
                "gabarito_img": "gabarito_divertix_home.png",
                "orientacao": "vertical"
            },
            "banner_divertix": {
                "descricao": "Banner Divertix – 255 x 240 cm",
                "largura": 15059,
                "altura": 14173,
                "resolucao_dpi": 150,
                "formato_final": ("JPEG",),
                "modo_cor": "CMYK",
                "gabarito_img": "gabarito_banner_divertix.png",
                "orientacao": "horizontal"
            },
        }
    elif teatro == "Teatro das Artes":
        return {
            "site_teatro_home": {
                "descricao": "Home do Site – 768 x 1024 px",
                "largura": 768,
                "altura": 1024,
                "formato_final": ("JPEG", "PNG"),
                "modo_cor": "RGB",
                "gabarito_img": "gabarito_site_teatro.png",
                "orientacao": "vertical"
            },
            "tv_teatro_externa": {
                "descricao": "TV Teatro Externa – 2160 x 3840 px",
                "largura": 2160,
                "altura": 3840,
                "formato_final": ("JPEG", "PNG"),
                "modo_cor": "RGB",
                "gabarito_img": "gabarito_tv_teatro.png",
                "orientacao": "vertical"
            },
        }
    return {}

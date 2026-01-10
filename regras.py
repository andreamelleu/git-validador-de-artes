from dataclasses import dataclass
from typing import Tuple, Optional, Dict, Any

# Configuração de teatros disponíveis
TEATROS_CONFIG: Dict[str, Any] = {
    "Teatro das Artes": {},
    "Teatro dos Grandes Atores": {}
}

@dataclass
class RegraValidacao:
    """Representa uma regra de validação de arte"""
    descricao: str
    largura: int
    altura: int
    formato_final: Tuple[str, ...]
    modo_cor: str
    orientacao: str
    resolucao_dpi: Optional[int] = None
    gabarito_img: str = ""
    checklist_visual: tuple = ()

    def to_dict(self) -> dict:
        return {
            "descricao": self.descricao,
            "largura": self.largura,
            "altura": self.altura,
            "formato_final": self.formato_final,
            "modo_cor": self.modo_cor,
            "gabarito_img": self.gabarito_img,
            "orientacao": self.orientacao,
            "resolucao_dpi": self.resolucao_dpi,
            "checklist_visual": self.checklist_visual,
        }


class TeatroRegras:
    """Fábricas de regras por tipo de peça"""

    # ====== PEÇAS PADRÃO (usadas pelos dois teatros) ======

    @staticmethod
    def regra_divertix_home(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix - Home do site (370x550)",
            largura=370,
            altura=550,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Logos do Teatro e Divertix no topo",
                "Informações legíveis",
                "Sem informações cortadas nas bordas"
            )
        )

    @staticmethod
    def regra_divertix_atracao(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix - Tela da Atração (740x380)",
            largura=740,
            altura=380,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=(
                "Logos do Teatro e Divertix visíveis",
                "Destaque para a atração",
                "Texto não pode cobrir rostos principais"
            )
        )

    @staticmethod
    def regra_divertix_carrossel_mobile(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix - Carrossel Mobile (375x471)",
            largura=375,
            altura=471,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Logos centralizados no topo",
                "Texto legível em telas pequenas",
                "Contraste adequado para leitura mobile"
            )
        )

    @staticmethod
    def regra_divertix_desktop(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix - Carrossel Desktop (1120x400)",
            largura=1120,
            altura=400,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=(
                "Logos visíveis",
                "Layout adaptado para formato wide",
                "Informações principais na área segura"
            )
        )

    @staticmethod
    def regra_site_teatro_home(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Teatro Site / Totem Shopping (768x1024)",
            largura=768,
            altura=1024,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Uso: Site do Teatro e Totem Digital",
                "Logos do Teatro e Divertix visíveis",
                "Informações legíveis para Web e Totem"
            )
        )

    # ====== EXTRAS (só no Grandes Atores) ======

    @staticmethod
    def regra_tv_externa(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="TV 50\" - 2160 x 3840 px",
            largura=2160,
            altura=3840,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Resolução 4K real (não apenas redimensionado)",
                "Texto grande e legível à distância",
                "Evitar fundos muito brancos (brilho excessivo)"
            )
        )
    
    # ====== NOVAS REGRAS SHOPPING DA GÁVEA (TEATRO DAS ARTES) ======

    @staticmethod
    def regra_totem_gavea(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Shopping Gávea - Totem Digital (768x1024)",
            largura=768,
            altura=1024,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Local: Entre Escadas Rolantes",
                "Texto legível à passagem",
                "Logos visíveis"
            )
        )

    @staticmethod
    def regra_videowall_1piso(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Shopping Gávea - Video Wall 1º Piso (1920x1079)",
            largura=1920,
            altura=1079,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=(
                "Local: Corredor 1º Piso (Frente Rei do Matte)",
                "Resolução específica (1079px altura)",
                "Destaque para a atração"
            )
        )

    @staticmethod
    def regra_videowall_2piso(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Shopping Gávea - Video Wall 2º Piso (1366x768)",
            largura=1366,
            altura=768,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=(
                "Local: Frente Arezzo",
                "Texto grande para leitura em movimento"
            )
        )

    @staticmethod
    def regra_videowall_3piso(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Shopping Gávea - Video Wall 3º Piso (1080x1920)",
            largura=1080,
            altura=1920,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Local: 3º Piso (Vertical)",
                "Texto legível",
                "Logos visíveis"
            )
        )

    @staticmethod
    def regra_tv_externa_gavea(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Shopping Gávea - TV Externa (2160x3840)",
            largura=2160,
            altura=3840,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Local: Ao lado da bilheteria de cadeirante",
                "Resolução 4K vertical",
                "Informações de preço e horário claras"
            )
        )

    # ====== LOTE 4 - BANNERS (TEATRO DAS ARTES) ======
    
    @staticmethod
    def regra_banner_principal_adulto(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Principal Adulto - 374x244cm",
            largura=22087,
            altura=14409,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=("CMYK 150 DPI", "Baixar PSD no site", "Sangria Ok")
        )

    @staticmethod
    def regra_banner_alternativo_rampa(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Alt. Rampa - 233,5x155cm",
            largura=13789,
            altura=9154,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=("CMYK 150 DPI", "Fundo Rampa de Acesso")
        )

    @staticmethod
    def regra_banner_principal_infantil(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Princ. Infantil - 121x209cm",
            largura=7146,
            altura=12343,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=("CMYK 150 DPI", "Entrada do Teatro")
        )

    @staticmethod
    def regra_banner_infantil_inteiro(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Inf. Porta Inteiro - 106x197cm",
            largura=6260,
            altura=11634,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=("CMYK 150 DPI", "Porta Dupla Saída")
        )

    @staticmethod
    def regra_banner_infantil_dividido(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Inf. Porta Dividido - 106x95,5cm",
            largura=6260,
            altura=5640,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
            checklist_visual=("CMYK 150 DPI", "Porta Dupla Saída (Dividido)")
        )

    @staticmethod
    def regra_banner_divertix(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Divertix - 255 x 240 cm",
            largura=15059,
            altura=14173,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Cores em CMYK obrigatório",
                "Resolução mínima de 150 DPI",
                "Margens de sangria respeitadas",
                "Preto calçado (C:40 M:40 Y:40 K:100) para fundos"
            )
        )

    @staticmethod
    def regra_banner_salas(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Salas - 290 x 240 cm",
            largura=17126,
            altura=14173,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="vertical",
            checklist_visual=(
                "Cores em CMYK obrigatório",
                "Resolução mínima de 150 DPI",
                "Elementos importantes longe das bordas (ilhós)"
            )
        )


def carregar_regras(teatro: str) -> dict:
    """
    Retorna o dicionário de regras para o teatro informado.
    Os nomes de arquivos de gabarito batem com os que existem em:
    assets/teatros/<grandes_atores|das_artes>/
    """
    import os
    from config import DIRECTORY_CONFIG
    
    # Determina o diretório base do teatro
    if teatro == "Teatro dos Grandes Atores":
        diretorio_teatro = DIRECTORY_CONFIG["GRANDES_ATORES_PATH"]
        regras_dict = {
            "divertix_home": TeatroRegras.regra_divertix_home("gabarito_divertix_home.png").to_dict(),
            "divertix_atracao": TeatroRegras.regra_divertix_atracao("gabarito_divertix_tela_atracao.png").to_dict(),
            "divertix_carrossel_mobile": TeatroRegras.regra_divertix_carrossel_mobile("gabarito_divertix_carrossel_mobile.png").to_dict(),
            "divertix_desktop": TeatroRegras.regra_divertix_desktop("gabarito_divertix_carrossel_desktop.png").to_dict(),
            "site_teatro_home": TeatroRegras.regra_site_teatro_home("gabarito_site_teatro.png").to_dict(),
            "tv_externa": TeatroRegras.regra_tv_externa("gabarito_tv_teatro.png").to_dict(),
            "banner_divertix": TeatroRegras.regra_banner_divertix("gabarito_banner_divertix.png").to_dict(),
            "banner_salas": TeatroRegras.regra_banner_salas("gabarito_banner_salas.png").to_dict(),
        }
    elif teatro == "Teatro das Artes":
        diretorio_teatro = DIRECTORY_CONFIG["DAS_ARTES_PATH"]
        regras_dict = {
            "divertix_home": TeatroRegras.regra_divertix_home("gabarito_divertix_home.png").to_dict(),
            "divertix_atracao": TeatroRegras.regra_divertix_atracao("gabarito_divertix_tela_atracao.png").to_dict(),
            "divertix_carrossel_mobile": TeatroRegras.regra_divertix_carrossel_mobile("gabarito_divertix_carrossel_mobile.png").to_dict(),
            "divertix_desktop": TeatroRegras.regra_divertix_desktop("gabarito_divertix_carrossel_desktop.png").to_dict(),
            "site_teatro_home": TeatroRegras.regra_site_teatro_home("gabarito_site_home.png").to_dict(),
            # "totem_gavea": Unificado com site_teatro_home (mesma medida)
            "videowall_1piso": TeatroRegras.regra_videowall_1piso("").to_dict(),
            "videowall_2piso": TeatroRegras.regra_videowall_2piso("").to_dict(),
            "videowall_3piso": TeatroRegras.regra_videowall_3piso("").to_dict(),
            "tv_externa_gavea": TeatroRegras.regra_tv_externa_gavea("").to_dict(),
            "banner_adulto": TeatroRegras.regra_banner_principal_adulto("").to_dict(),
            "banner_rampa": TeatroRegras.regra_banner_alternativo_rampa("").to_dict(),
            "banner_infantil_entrada": TeatroRegras.regra_banner_principal_infantil("").to_dict(),
            "banner_infantil_inteiro": TeatroRegras.regra_banner_infantil_inteiro("").to_dict(),
            "banner_infantil_dividido": TeatroRegras.regra_banner_infantil_dividido("").to_dict(),
        }
    else:
        return {}
    
    # Adiciona gabarito_path (caminho completo) para cada regra
    for regra_key, regra_data in regras_dict.items():
        gabarito_img = regra_data.get("gabarito_img", "")
        if gabarito_img:
            regra_data["gabarito_path"] = os.path.join(diretorio_teatro, gabarito_img)
    
    return regras_dict

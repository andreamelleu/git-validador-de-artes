from dataclasses import dataclass
from typing import Tuple, Optional

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
        }


class TeatroRegras:
    """Fábricas de regras por tipo de peça"""

    # ====== PEÇAS PADRÃO (usadas pelos dois teatros) ======

    @staticmethod
    def regra_divertix_home(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Home do Site – 370 x 550 px",
            largura=370,
            altura=550,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
        )

    @staticmethod
    def regra_divertix_atracao(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Tela da Atração – 740 x 380 px",
            largura=740,
            altura=380,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
        )

    @staticmethod
    def regra_divertix_carrossel_mobile(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Carrossel Mobile – 375 x 471 px",
            largura=375,
            altura=471,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
        )

    @staticmethod
    def regra_divertix_desktop(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Carrossel Desktop – 1120 x 400 px",
            largura=1120,
            altura=400,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="horizontal",
        )

    @staticmethod
    def regra_site_teatro_home(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Site do Teatro – 768 x 1024 px",
            largura=768,
            altura=1024,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
        )

    # ====== EXTRAS (só no Grandes Atores) ======

    @staticmethod
    def regra_tv_externa(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="TV 50" – 2160 x 3840 px",
            largura=2160,
            altura=3840,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img=gabarito_img,
            orientacao="vertical",
        )

    @staticmethod
    def regra_banner_divertix(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Divertix – 255 x 240 cm",
            largura=15059,
            altura=14173,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="vertical",
        )

    @staticmethod
    def regra_banner_salas(gabarito_img: str) -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Salas – 290 x 240 cm",
            largura=17126,
            altura=14173,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img=gabarito_img,
            orientacao="vertical",
        )


def carregar_regras(teatro: str) -> dict:
    """
    Retorna o dicionário de regras para o teatro informado.
    Os nomes de arquivos de gabarito batem com os que existem em:
    assets/teatros/<grandes_atores|das_artes>/
    """
    if teatro == "Teatro dos Grandes Atores":
        return {
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
        # EXATAMENTE os arquivos que você mostrou:
        return {
            "divertix_home": TeatroRegras.regra_divertix_home("gabarito_divertix_home.png").to_dict(),
            "divertix_atracao": TeatroRegras.regra_divertix_atracao("gabarito_divertix_tela_atracao.png").to_dict(),
            "divertix_carrossel_mobile": TeatroRegras.regra_divertix_carrossel_mobile("gabarito_divertix_carrossel_mobile.png").to_dict(),
            "divertix_desktop": TeatroRegras.regra_divertix_desktop("gabarito_divertix_carrossel_desktop.png").to_dict(),
            "site_teatro_home": TeatroRegras.regra_site_teatro_home("gabarito_site_home.png").to_dict(),
            # Sem TV/Banners aqui porque não existem nas suas pastas do das_artes
        }

    else:
        return {}

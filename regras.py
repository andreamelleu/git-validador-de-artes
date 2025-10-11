from dataclasses import dataclass
from typing import Tuple, Optional
from common_utils import verificar_arte


@dataclass
class RegraValidacao:
    """Classe para representar uma regra de validação de arte"""
    descricao: str
    largura: int
    altura: int
    formato_final: Tuple[str, ...]
    modo_cor: str
    gabarito_img: str
    orientacao: str
    resolucao_dpi: Optional[int] = None
    
    def to_dict(self) -> dict:
        """Converte a regra para dicionário"""
        return {
            "descricao": self.descricao,
            "largura": self.largura,
            "altura": self.altura,
            "formato_final": self.formato_final,
            "modo_cor": self.modo_cor,
            "gabarito_img": self.gabarito_img,
            "orientacao": self.orientacao,
            "resolucao_dpi": self.resolucao_dpi
        }


class TeatroRegras:
    """Classe para gerenciar regras de validação por teatro"""
    
    @staticmethod
    def criar_regra_divertix_home() -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Home do Site – 370 x 550 px",
            largura=370,
            altura=550,
            formato_final=("JPEG", "PNG"),
            modo_cor="RGB",
            gabarito_img="gabarito_divertix_home.png",
            orientacao="vertical"
        )
    
    @staticmethod
    def criar_regra_divertix_atracao() -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Tela da Atração – 740 x 380 px",
            largura=740,
            altura=380,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img="gabarito_divertix_tela_atracao.png",
            orientacao="horizontal"
        )
    
    @staticmethod
    def criar_regra_divertix_carrossel_mobile() -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Carrossel Mobile – 375 x 471 px",
            largura=375,
            altura=471,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img="gabarito_divertix_carrossel_mobile.png",
            orientacao="vertical"
        )
        
    @staticmethod
    def criar_regra_divertix_desktop() -> RegraValidacao:
        return RegraValidacao(
            descricao="Divertix Carrossel Desktop – 1120 x 400 px",
            largura=1120,
            altura=400,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img="gabarito_divertix_carrossel_desktop.png",
            orientacao="horizontal"
        )

    @staticmethod
    def criar_regra_site_teatro_home() -> RegraValidacao:
        return RegraValidacao(
            descricao="Site do Teatro – 768 x 1024 px",
            largura=768,
            altura=1024,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img="gabarito_site_teatro.png",
            orientacao="vertical"
        )
    
    @staticmethod
    def criar_regra_tv_externa() -> RegraValidacao:
        return RegraValidacao(
            descricao="TV 50” – 2160 x 3840 px",
            largura=2160,
            altura=3840,
            formato_final=("JPEG", "JPG", "PNG"),
            modo_cor="RGB",
            gabarito_img="gabarito_tv_teatro.png",
            orientacao="vertical"
        )

    @staticmethod
    def criar_regra_banner_divertix() -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Divertix – 255 x 240 cm",
            largura=15059,
            altura=14173,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img="gabarito_banner_divertix.png",
            orientacao="vertical"
        )
    
    @staticmethod
    def criar_regra_banner_salas() -> RegraValidacao:
        return RegraValidacao(
            descricao="Banner Salas – 290 x 240 cm",
            largura=17126,
            altura=14173,
            resolucao_dpi=150,
            formato_final=("JPEG", "JPG"),
            modo_cor="CMYK",
            gabarito_img="gabarito_banner_salas.png",
            orientacao="vertical"
        )

def carregar_regras(teatro: str) -> dict:
    """Carrega as regras de validação para o teatro especificado"""
    if teatro == "Teatro dos Grandes Atores":
        return {
            "divertix_home": TeatroRegras.criar_regra_divertix_home().to_dict(),
            "divertix_atracao": TeatroRegras.criar_regra_divertix_atracao().to_dict(),
            "divertix_carrossel_mobile": TeatroRegras.criar_regra_divertix_carrossel_mobile().to_dict(),
            "divertix_desktop": TeatroRegras.criar_regra_divertix_desktop().to_dict(),
            "site_teatro_home": TeatroRegras.criar_regra_site_teatro_home().to_dict(),
            "tv_externa": TeatroRegras.criar_regra_tv_externa().to_dict(),
            "banner_divertix": TeatroRegras.criar_regra_banner_divertix().to_dict(),
            "banner_salas": TeatroRegras.criar_regra_banner_salas().to_dict()
        }
    elif teatro == "Teatro das Artes":
        return {
            "site_teatro_home": TeatroRegras.criar_regra_site_teatro_home().to_dict(),
            "tv_externa": TeatroRegras.criar_regra_tv_externa().to_dict()
        }
    else:
        return {}

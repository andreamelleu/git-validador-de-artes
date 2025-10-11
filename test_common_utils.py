"""
Testes unitários para common_utils.py
"""
import pytest
import datetime
from unittest.mock import Mock, patch
from PIL import Image
from common_utils import (
    formatar_data_brasileira,
    formatar_data_timestamp,
    verificar_arte,
    processar_arquivo_com_erro,
    verificar_existencia_imagem
)


class TestFormatacaoData:
    """Testes para funções de formatação de data"""
    
    def test_formatar_data_brasileira(self):
        """Testa formatação de data brasileira"""
        data_formatada = formatar_data_brasileira()
        # Verifica se está no formato dd/mm/yyyy
        assert len(data_formatada) == 10
        assert data_formatada[2] == '/'
        assert data_formatada[5] == '/'
    
    def test_formatar_data_timestamp(self):
        """Testa formatação de timestamp"""
        timestamp = formatar_data_timestamp()
        # Verifica se está no formato yyyy-mm-dd_hh-mm-ss
        assert len(timestamp) == 19
        assert timestamp[4] == '-'
        assert timestamp[7] == '-'
        assert timestamp[10] == '_'
        assert timestamp[13] == '-'
        assert timestamp[16] == '-'


class TestVerificarArte:
    """Testes para função de verificação de arte"""
    
    def test_verificar_arte_sem_arquivo(self):
        """Testa validação sem arquivo"""
        resultado = verificar_arte(None, {})
        assert resultado[0] == False
        assert "Nenhum arquivo" in resultado[1]
    
    def test_verificar_arte_sem_regra(self):
        """Testa validação sem regra"""
        arquivo_mock = Mock()
        resultado = verificar_arte(arquivo_mock, None)
        assert resultado[0] == False
        assert "Nenhuma regra" in resultado[1]
    
    @patch('PIL.Image.open')
    def test_verificar_arte_dimensoes_incorretas(self, mock_image_open):
        """Testa validação com dimensões incorretas"""
        # Mock da imagem
        mock_img = Mock()
        mock_img.size = (100, 100)
        mock_img.format = "JPEG"
        mock_img.mode = "RGB"
        mock_img.info = {}
        mock_image_open.return_value = mock_img
        
        # Mock do arquivo
        arquivo_mock = Mock()
        arquivo_mock.read = Mock()
        arquivo_mock.seek = Mock()
        
        # Regra com dimensões diferentes
        regra = {
            'largura': 200,
            'altura': 200,
            'formato_final': ['JPEG'],
            'modo_cor': 'RGB'
        }
        
        resultado = verificar_arte(arquivo_mock, regra)
        assert resultado[0] == False
        assert "Dimensões incorretas" in resultado[1]
    
    @patch('PIL.Image.open')
    def test_verificar_arte_formato_incorreto(self, mock_image_open):
        """Testa validação com formato incorreto"""
        # Mock da imagem
        mock_img = Mock()
        mock_img.size = (200, 200)
        mock_img.format = "PNG"
        mock_img.mode = "RGB"
        mock_img.info = {}
        mock_image_open.return_value = mock_img
        
        # Mock do arquivo
        arquivo_mock = Mock()
        arquivo_mock.read = Mock()
        arquivo_mock.seek = Mock()
        
        # Regra que aceita apenas JPEG
        regra = {
            'largura': 200,
            'altura': 200,
            'formato_final': ['JPEG'],
            'modo_cor': 'RGB'
        }
        
        resultado = verificar_arte(arquivo_mock, regra)
        assert resultado[0] == False
        assert "Formato incorreto" in resultado[1]
    
    @patch('PIL.Image.open')
    def test_verificar_arte_aprovada(self, mock_image_open):
        """Testa validação aprovada"""
        # Mock da imagem
        mock_img = Mock()
        mock_img.size = (200, 200)
        mock_img.format = "JPEG"
        mock_img.mode = "RGB"
        mock_img.info = {}
        mock_image_open.return_value = mock_img
        
        # Mock do arquivo
        arquivo_mock = Mock()
        arquivo_mock.read = Mock()
        arquivo_mock.seek = Mock()
        arquivo_mock.size = 1024  # 1KB
        
        # Regra que corresponde à imagem
        regra = {
            'largura': 200,
            'altura': 200,
            'formato_final': ['JPEG'],
            'modo_cor': 'RGB'
        }
        
        resultado = verificar_arte(arquivo_mock, regra)
        assert resultado[0] == True
        assert "aprovada" in resultado[1]


class TestProcessarArquivoComErro:
    """Testes para função de processamento com erro"""
    
    def test_processar_arquivo_sucesso(self):
        """Testa processamento bem-sucedido"""
        arquivo_mock = Mock()
        arquivo_mock.name = "teste.jpg"
        
        def funcao_teste(arquivo):
            return "sucesso"
        
        resultado = processar_arquivo_com_erro(arquivo_mock, funcao_teste)
        assert resultado["arquivo"] == "teste.jpg"
        assert resultado["resultado"] == "sucesso"
    
    def test_processar_arquivo_erro(self):
        """Testa processamento com erro"""
        arquivo_mock = Mock()
        arquivo_mock.name = "teste.jpg"
        
        def funcao_teste(arquivo):
            raise Exception("Erro de teste")
        
        resultado = processar_arquivo_com_erro(arquivo_mock, funcao_teste)
        assert resultado["arquivo"] == "teste.jpg"
        assert "Erro ao processar" in resultado["resultado"]


class TestVerificarExistenciaImagem:
    """Testes para função de verificação de existência de imagem"""
    
    @patch('os.path.exists')
    def test_verificar_existencia_imagem_existe(self, mock_exists):
        """Testa quando imagem existe"""
        mock_exists.return_value = True
        
        resultado = verificar_existencia_imagem("teatro", "imagem.png")
        assert "assets/teatros/teatro/imagem.png" in resultado
    
    @patch('os.path.exists')
    def test_verificar_existencia_imagem_nao_existe(self, mock_exists):
        """Testa quando imagem não existe"""
        mock_exists.return_value = False
        
        resultado = verificar_existencia_imagem("teatro", "imagem.png")
        assert resultado == "assets/default.png"


if __name__ == "__main__":
    pytest.main([__file__])

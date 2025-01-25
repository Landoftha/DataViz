import pandas as pd 
import os

def load_data(file_path):
    """
    Carrega dados de um arquivo CSV, JSON ou Excel e retorna um DataFrame.

    Args:
        file_path (str): Caminho do arquivo a ser carregado.

    Returns:
        pd.DataFrame: DataFrame contendo os dados carregados.

    Raises:
        ValueError: Se o formato do arquivo não for suportado.
    """
    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

    # Obtém a extensão do arquivo
    file_extension = os.path.splitext(file_path)[1].lower()

    try:
        # Carregando o arquivo com base na extensão
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension == '.json':
            df = pd.read_json(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Formato de arquivo não suportado. Use CSV, JSON ou Excel.")
        
        # Remover colunas ou linhas duplicadas
        df.drop_duplicates(inplace=True)
        
        # Remover valores ausentes
        df.dropna(inplace=True)
        
        return df

    except Exception as e:
        raise RuntimeError(f"Erro ao carregar os dados: {e}")


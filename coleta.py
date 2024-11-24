import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

def extrair_dados_tabela(xpath_tabela, nome_arquivo):
    tabela = wait.until(EC.presence_of_element_located((By.XPATH, xpath_tabela)))
    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            dados = [coluna.text for coluna in colunas]
            writer.writerow(dados)

navegador.get("https://www.cepea.esalq.usp.br/br")
wait = WebDriverWait(navegador, 10)

categoria_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-wrap-content"]/div[4]/div[2]/img')))
categoria_btn.click()
proximo_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-categoria"]/div[2]/ul/li[15]/a')))
proximo_btn.click()
link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[3]/a[3]')))
link.click()
extrair_dados_tabela('//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[2]', 'dados_tabela_milho.csv')

navegador.get("https://www.cepea.esalq.usp.br/br")
categoria_avn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-wrap-content"]/div[3]/div[2]/img')))
categoria_avn.click()
categoria_bvn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-categoria"]/div[2]/ul/li[6]/a')))
categoria_bvn.click()
categoria_cvn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[3]/a[3]')))
categoria_cvn.click()
extrair_dados_tabela('//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[2]', 'dados_tabela_cafe.csv')

navegador.get("https://www.cepea.esalq.usp.br/br")
categoria_abc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-wrap-content"]/div[3]/div[2]/img')))
categoria_abc.click()
categoria_bbc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-categoria"]/div[2]/ul/li[18]/a')))
categoria_bbc.click()
categoria_cbc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[3]/a[3]')))
categoria_cbc.click()
extrair_dados_tabela('//*[@id="imagenet-content"]/div[2]/div[2]/div[1]/div[2]', 'dados_tabela_soja.csv')


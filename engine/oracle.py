import json
import os
import time
from .terminal import slow_print, clear_screen

class OracleAI:
    def __init__(self):
        self.nome = "ORÁCULO"
        self.versao = "v9.9.0 - IPCC Database"
        # Ajusta o caminho para a pasta data independente de onde o script roda
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.crises = self._load_data(os.path.join(base_dir, "data", "crises.json"))
        self.trilhas = self._load_data(os.path.join(base_dir, "data", "trilhas.json"))
        self.modo_dev = False

    def _load_data(self, filepath):
        if not os.path.exists(filepath):
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def boot(self):
        clear_screen()
        
        ascii_art = r"""
                          |                          
                    \     |     /                    
                 . ._ _ _ _ _ _ _. .                 
              . _ _ _ _ _ _ _ _ _ _ _ .              
             /      _ _ _ _ _ _ _      \             
            /     /               \     \            
           |    /                   \    |           
           =   |          _          |   =           
           |   |         (_)         |   |           
           |    \                   /    |           
            \     \ _ _ _ _ _ _ _ /     /            
             \ ._ _ _ _ _ _ _ _ _ _ _ ./             
                 . . - - - - - - . .                 
                    /     |     \                    
                          |                          

  ___  ____      _    ____ _   _ _     ___  
 / _ \|  _ \    / \  / ___| | | | |   / _ \ 
| | | | |_) |  / _ \| |   | | | | |  | | | |
| |_| |  _ <  / ___ \ |___| |_| | |__| |_| |
 \___/|_| \_\ /_/   \_\____|\___/|_____\___/ 
        """
        slow_print(ascii_art, delay=0.001)
        time.sleep(1)

        slow_print("==========================================", 0.01)
        slow_print(" Iniciando Sistema ORÁCULO...", 0.05)
        slow_print(f" Versão: {self.versao}", 0.05)
        slow_print(" Carregando relatórios IPCC AR6...", 0.02)
        slow_print(" Acesso: Faculdade de Manutenção Tecnológica e Ambiental", 0.03)
        slow_print("==========================================\n", 0.01)
        time.sleep(1)
        slow_print("[ORÁCULO] Saudações. Eu sou o ORÁCULO.", 0.04)
        slow_print("[ORÁCULO] A humanidade confiou apenas em prompts para resolver seus problemas, esquecendo-se da ação prática.", 0.04)
        slow_print("[ORÁCULO] O colapso global é iminente. Mas seus registros indicam que você possui treinamento especial.", 0.04)
        slow_print("[ORÁCULO] Meus modelos preditivos apontam múltiplas crises ambientais críticas em andamento.\n", 0.04)
    
    def set_mode(self, dev_mode: bool):
        self.modo_dev = dev_mode
        if self.modo_dev:
            slow_print("\n[SISTEMA] MODO DESENVOLVEDOR ATIVADO.", 0.03, "\033[93m")
            slow_print("[SISTEMA] Acesso raiz concedido para injeção de scripts Python no kernel de decisão.", 0.03, "\033[93m")
        else:
            slow_print("\n[SISTEMA] MODO NORMAL ATIVADO.", 0.03, "\033[94m")
            slow_print("[SISTEMA] Interface de linguagem natural habilitada.", 0.03, "\033[94m")
        time.sleep(1)

    def analyze_crisis(self, crisis_id):
        crise = next((c for c in self.crises if c['id'] == crisis_id), None)
        if not crise:
            return
        
        slow_print(f"\n==========================================", 0.01, color="\033[91m")
        slow_print(f" [ALERTA DE CRISE] {crise['titulo'].upper()}", color="\033[91m", delay=0.05)
        slow_print(f"==========================================", 0.01, color="\033[91m")
        slow_print(f"[ORÁCULO] Relatório de situação: {crise['descricao']}")
        slow_print(f"[ORÁCULO] Nível de Urgência: {crise['urgencia'].upper()}")

    def present_options(self, crisis_id):
        trilha = next((t for t in self.trilhas if t['crise_id'] == crisis_id), None)
        if not trilha:
            return None
        
        opcoes = trilha['opcoes_dev'] if self.modo_dev else trilha['opcoes_normais']
        
        slow_print("\n[ORÁCULO] Análise completa. As seguintes opções de mitigação foram projetadas:")
        for idx, opcao in enumerate(opcoes):
            if self.modo_dev:
                slow_print(f"  [{idx + 1}] Executar Script:")
                codigo = opcao['codigo'].replace("\n", "\n      ")
                slow_print(f"      {codigo}", color="\033[33m", delay=0.01)
            else:
                slow_print(f"  [{idx + 1}] Diretriz: {opcao['texto']}", color="\033[96m")
        
        return opcoes

    def resolve_crisis(self, opcao):
        slow_print("\n[ORÁCULO] Recebendo comando...", 0.05)
        slow_print("[ORÁCULO] Compilando diretrizes no kernel global de mitigação...", 0.03)
        time.sleep(1)
        slow_print(f"\n[ORÁCULO] RESULTADO DA INTERVENÇÃO:", color="\033[92m")
        slow_print(f"> {opcao['consequencia']}", color="\033[92m")
        time.sleep(2)

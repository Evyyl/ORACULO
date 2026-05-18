import time
from engine.oracle import OracleAI
from engine.terminal import prompt, slow_print, clear_screen

def main():
    oraculo = OracleAI()
    oraculo.boot()
    
    slow_print("[ORÁCULO] Por favor, identifique suas credenciais operacionais.")
    escolha_modo = prompt("Você utilizará a interface padrão (normal) ou a interface de desenvolvimento (dev)?")
    
    if escolha_modo.strip().lower() in ['dev', 'desenvolvedor', 'python', 'd']:
        oraculo.set_mode(True)
    else:
        oraculo.set_mode(False)
        
    for crise in oraculo.crises:
        oraculo.analyze_crisis(crise['id'])
        opcoes = oraculo.present_options(crise['id'])
        
        if opcoes:
            while True:
                escolha_input = prompt("Selecione o índice da ação para implementação:")
                try:
                    escolha = int(escolha_input)
                    if 1 <= escolha <= len(opcoes):
                        oraculo.resolve_crisis(opcoes[escolha - 1])
                        break
                    else:
                        slow_print("[ERRO] Índice fora de parâmetros aceitáveis. Tente novamente.", color="\033[91m")
                except ValueError:
                    slow_print("[ERRO] Input não reconhecido. Por favor, insira um valor numérico válido.", color="\033[91m")
                    
    slow_print("\n==========================================", 0.01, color="\033[92m")
    slow_print("[ORÁCULO] Avaliação final concluída.", color="\033[92m")
    slow_print("[ORÁCULO] As crises imediatas foram mitigadas. A estabilidade climática entrou em período de observação.", color="\033[92m")
    slow_print("[ORÁCULO] Lembre-se: IAs apenas sugerem caminhos. A execução no mundo real depende de vocês.", color="\033[92m")
    slow_print("==========================================", 0.01, color="\033[92m")
    slow_print("\n[ SISTEMA DESLIGANDO ]", delay=0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[SISTEMA] Interrupção detectada. Encerrando o ORÁCULO prematuramente.")

# ============================================================
#  bot_initializer.py - Lab 01: Tipagem e Inicialização de Variáveis
# ============================================================

# --- Variáveis de Configuração do Robô ---
BOT_NAME: str = "RPA_FINANCEIRO_01"
MAX_RETRIES: int = 3
EXECUTION_TIMEOUT: float = 30.5
IS_PRODUCTION: bool = False

# --- Mensagem de Inicialização ---
print("=" * 50)
print("   INICIALIZANDO CONFIGURAÇÕES DO ROBÔ RPA")
print("=" * 50)
print(f"  Nome do Robô      : {BOT_NAME}")
print(f"  Tipo              : {type(BOT_NAME)}")
print("-" * 50)
print(f"  Máx. Tentativas   : {MAX_RETRIES}")
print(f"  Tipo              : {type(MAX_RETRIES)}")
print("-" * 50)
print(f"  Timeout (seg)     : {EXECUTION_TIMEOUT}")
print(f"  Tipo              : {type(EXECUTION_TIMEOUT)}")
print("-" * 50)
print(f"  Produção          : {IS_PRODUCTION}")
print(f"  Tipo              : {type(IS_PRODUCTION)}")
print("=" * 50)
print("  ✅ Bot inicializado com sucesso!")
print("=" * 50)

"""Triagem local de mensagens fictícias."""
import json
import sys


KEYWORDS = {
    "vendas": ("preço", "comprar", "orçamento", "plano"),
    "suporte": ("erro", "bug", "não funciona", "problema"),
    "financeiro": ("boleto", "pagamento", "nota", "cobrança"),
}


def classificar(mensagem: str) -> str:
    texto = mensagem.casefold()
    for categoria, palavras in KEYWORDS.items():
        if any(palavra in texto for palavra in palavras):
            return categoria
    return "outros"


if __name__ == "__main__":
    mensagem = " ".join(sys.argv[1:]) or "Quero saber o preço do serviço"
    print(json.dumps({"mensagem": mensagem, "fila": classificar(mensagem)}, ensure_ascii=False))

## Trabalho final compiladores 
Facilitador de geração de memes permite que adicionar textos a imagens de forma simples
### Instalação
Utilizando virtualenv execute `pip install -r requirements.txt`, e depois instale o pacote com `flit install`. Para executar os comando abaixo dentro da pasta tf-compiladores execute `meme` no terminal.
As imagens e as fontes devem estar em na pasta tf-compiladores
### Comandos 
Atribuição de imagem 
**nome_da_variavel** = *caminho para imagem*
```
img = "teste.jpg"
```
Configuração de fonte 
setfont *caminho para a fonte* **tamanho da fonte**
```
setfont "Roboto-Black.ttf" 30
```
Adicionando o texto na imagem 
settext **imagem** (posição no eixo **x**,posição no eixo **y**) *texto*
```
settext img (0,0) "texto exemplo"
```
Salvar image  
save **variavel_imagem** *nome_da_nova_imagem*
```
save img "imagem_teste.jpg"
```
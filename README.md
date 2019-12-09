## Trabalho final compiladores 
Facilitador de geração de memes permite que adicionar textos a imagens de forma simples
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
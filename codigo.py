#HASZAP

# BOTÃO DE INICAR CHAT

#POPUP PARA ENTRAR NO CHAT


#QUANDO ENTRAR NO CHAT:(APARECE PRA TODO MUNDO)
    #A MENSAGEM QUE VOCÊ ENVIOU NO CHAT


    #O CAMPO E O BOTÃO DE ENVIAR A MENSAGEM


# A CADA MENSAGEM QUE VOCÊ ENVIA:(APARECE PRA TODO MUNDO)
    #NOME: TEXTO DA MENSAGEM


#HASZAP

import flet as ft

def main(pagina):
    texto = ft.Text("LETZAP")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

   

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            #ADICIONAR A MENSAGEM NO CHAT
            chat.controls.append(ft.Text(f"{usuario_mensagem} : {texto_mensagem}"))
        else:
             usuario_mensagem = mensagem["usuario"]
             chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=15, italic=True,color=ft.colors.RED_ACCENT_700))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto":campo_mensagem.value, "usuario":nome_usuario.value, "tipo" : "mensagem"})
        #LIMPAR O COMPO DE MENSAGEM
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem",on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario" : nome_usuario.value, "tipo" : "entrada"})
        #ADICIONAR O CHAT
        pagina.add(chat)
        #FECHAR POPUP   
        popup.open = False
        #REMOVER O BOTÃO INICIAR CHAT
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # CRIAR O CAMPO DE MENSAGEM DO USUÁRIO  
        pagina.add(ft.Row(
            [campo_mensagem,
             botao_enviar_mensagem]
             ))
        #CRIAR O BOTÃO DE ENVIAR MENSAGEM DO USUÁRIO
        
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title= ft.Text("Bem vindo ao LETZAP"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )

    def entrar_chat(evento):
       pagina.dialog = popup
       popup.open= True
       pagina.update()
        

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)




ft.app(target=main, view=ft.WEB_BROWSER, port=9999)
    




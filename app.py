import time
import avaimet
import gradio as gr

def getAccess(userfile):
        
    sshListo, sftpListo = avaimet.conecta()

    #Obtiene la caja donde está guardados los tokens.
    caja = avaimet.obtenCaja(userfile)

    tokens = avaimet.obtenTokens(sftpListo, caja)

    resultado_final = avaimet.aplicaReglas(sftpListo, caja, tokens)

    avaimet.cierraConexion(sshListo, sftpListo)
    
    return resultado_final

def print():

    print("Hola mundo")

    return "Hola Mundo"

iface = gr.Interface(fn=getAccess, inputs="text", outputs="text", api_name="entrar")

iface.launch()
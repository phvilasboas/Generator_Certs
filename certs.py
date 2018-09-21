#!/usr/bin/python
# coding: utf-8
import os, sys, re
#import urllib, urllib2

#nome_do_arquivo_svg_base
svgbase = "cert"
original = open(svgbase+".svg").read()
diretorio = "certificados"

def geraPDF(arquivo):
    print "    gerando certificado em pdf"
    #gerando o PNG baseado no SVG
    #comando = 'inkscape %s.svg -C -d 150 -e %s/%s.png' % (arquivo, diretorio, arquivo)
    comando = 'inkscape %s.svg -A  %s/%s.pdf' % (arquivo, diretorio, arquivo)
    os.system(comando)
    print "    removendo arquivo svg"
    #removendo o SVG
    remover = 'rm %s.svg' % (arquivo)
    os.system(remover)

def geraSVG(arquivo,nome):
    print "    copiando o arquivo svg base para " + arquivo + ".svg"
    #copiando o arquivo do svg original para ser usado de base
    comando = 'cp cert.svg %s.svg' % arquivo
    os.system(comando)
    #substituindo o nome d@ aprovad@ no arquivo svg
    novoCert = open(arquivo + ".svg",'r+')
    novoCert.write( re.sub("___NOME___",nome,original) )
    #aqui deve ser chamado o gerador de QRCode e, em seguida,
    #ele deve ser adicionado ao arquivo svg.
    novoCert.close()

def geraCertificados():
    aprovados = open("listaNomes")
    #Verificando se o diretório de certificados existe
    if not os.path.exists(diretorio):
	os.makedirs(diretorio)
    for aprovado in aprovados:
        #removendo a quebra de linha do final da variavel
        nome = aprovado.rstrip("\n")
        if (nome):
	    print "Gerando certificado de " + nome + ":"
            #removendo espaços do nome do arquivo
            arquivo = nome.replace(" ","_")
            #gerando SVG
	    geraSVG(arquivo,nome)
            #gerando PDF
            geraPDF(arquivo)
            print ""

geraCertificados()


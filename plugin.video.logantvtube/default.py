# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

versao = '1.0.0'
addonID = 'plugin.video.logantvtube'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = 'http://3.bp.blogspot.com/-ZN1-yhXrvoQ/Tcn8OJXvlQI/AAAAAAAAEWc/yAApMLKtIU4/s320/medrado.jpg'
icon2 = 'https://i.ytimg.com/vi/J5xbtSIm7cI/mqdefault.jpg'
icon3 = 'http://laerciofonseca.com/loja/image/catalog/imagens_informacoes/lala_foto.jpg'
icon4 = 'http://www.rcespiritismo.com.br/conteudo_site/imagens/foto_Wagner.bmp'
icon5 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Drauzio_Varella.jpg/200px-Drauzio_Varella.jpg'
icon6 = 'http://tvnova.tv.br/multimidia/261020159212755959_bjpyo.jpg'
icon7 = 'http://imgsapp.em.com.br/app/noticia_127983242361/2015/11/18/709303/20151118130210998337i.png'
icon8 = 'http://1.bp.blogspot.com/-97MMIK-2y9I/VgskC9dviMI/AAAAAAABL-o/fW2jkqeRzE8/s1600/9%2BFilmes%2Bde%2BSuspenses%2BPsicol%25C3%25B3gicos%2BIncr%25C3%25ADveis.png'
icon9 = 'https://yt3.ggpht.com/-0Si5qmcUhW4/AAAAAAAAAAI/AAAAAAAAAAA/NBsH0xbG-GU/s176-c-k-no/photo.jpg'
icon0 = 'https://yt3.ggpht.com/-tqsCbyWrsso/AAAAAAAAAAI/AAAAAAAAAAA/po-c8qsWGFw/s176-c-k-no/photo.jpg'

def run():
    plugintools.log("DocBrasil.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("DocBrasil ===> " + repr(params))

		plugintools.add_item(title = "José Medrado"                  , url = base + "user/cidadedaluz/"            , thumbnail = icon1, folder = True)
		plugintools.add_item(title = "Saulo Calderon"    , url = base + "channel/UC3bXRwWHoPOC2yoUzKgb6eQ/", thumbnail = icon2, folder = True)
		plugintools.add_item(title = "Prof. Laercio Fonseca"         , url = base + "channel/UCOBVZH9VYftaJmPVjtf01Ww/", thumbnail = icon3, folder = True)
		plugintools.add_item(title = "Wagner Borges"      , url = base + "channel/UC9fu3YZJFP-Gso8I-TcY3oQ/", thumbnail = icon4, folder = True)
		plugintools.add_item(title = "Dr. Drauzio Varella"     , url = base + "channel/UC9zqTTVeClpqMQ5CLuJdWtw/"                , thumbnail = icon5, folder = True)
		plugintools.add_item(title = "Materia de Capa"          , url = base + "channel/UCF-4abYiGtu9kfjq2ON5rgA/", thumbnail = icon6, folder = True)
		plugintools.add_item(title = "Mega Filmes"             , url = base + "user/XxAlemao97xX/", thumbnail = icon7, folder = True)
		plugintools.add_item(title = "O Fim Dos Tempos Chegou"           , url = base + "channel/UCD_-fbfpLkDAV_rZ6mX8lVg/", thumbnail = icon8, folder = True)
		plugintools.add_item(title = "Universo Dos Documentários"    , url = base + "channel/UCnnXcMPdZbB0lvcvBQ5KE5g/", thumbnail = icon9, folder = True)
		plugintools.add_item(title = "Visão do Mundo - Documentários", url = base + "channel/UCcPud6tzYnYAdoFWNDisu1g/", thumbnail = icon0, folder = True)

		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
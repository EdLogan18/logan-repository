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
addonID = 'plugin.video.logantubemusic'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = 'http://assets.rollingstone.com/assets/images/artists/bruce-springsteen.jpg'
icon2 = 'http://www.iconbeverages.co.uk/media/wysiwyg/Trooper_Cover.jpg'
icon3 = 'https://yt3.ggpht.com/-di1CvE2tLNQ/AAAAAAAAAAI/AAAAAAAAAAA/PycFiaklPSw/s100-c-k-no-rj-c0xffffff/photo.jpg'
icon4 = 'http://weston-cache.iwitness24.co.uk/en/photos/entertainment/2012-07-28/1662/thomas-zwijsen-at-green-baize/medium/4109-_mc16647-jpg.jpg'
icon5 = 'http://www.rock-o-rama.com.br/wp-content/uploads/2015/09/classicrock.jpg'
icon6 = 'https://lh3.googleusercontent.com/-fsBxnAIu0io/AAAAAAAAAAI/AAAAAAAAAAU/_uf5-oqscug/s265-c-k-no/photo.jpg'
icon7 = 'http://www.ecoviagem.com.br/fotos-anuncios/brasil/sao-paulo/ilhabela/atrativo-turistico/pesca-de-camarao/45746med249804-por-do-sozinho.jpg'
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

		plugintools.add_item(title = "Bruce Springsteen"                  , url = base + "user/BruceSpringsteenVEVO/"            , thumbnail = icon1, folder = True)
		plugintools.add_item(title = "Iron Maiden"    , url = base + "user/ironmaiden/", thumbnail = icon2, folder = True)
		plugintools.add_item(title = "Nacional Rock 80"         , url = base + "user/nacionalrock80/", thumbnail = icon3, folder = True)
		plugintools.add_item(title = "Thomas Zwijsen"      , url = base + "user/ThomasZwijsen2007/", thumbnail = icon4, folder = True)
		#Classic rock="user edlogan18"
		plugintools.add_item(title = "Classic Rock"     , url = base + "channel/UCstl7ql3wXzwncz-Rgd0s-Q/playlists/" , thumbnail = icon5, folder = True)
		#Albuns Completos - Bandas nacionais - "canal zorro"conta diego veiga oliveira"
		plugintools.add_item(title = "Albuns Completos - Bandas Nacionais"    , url = base + "channel/UCG5puI42yb3ogdrFml2fSFQ/playlists/", thumbnail = icon6, folder = True)
		#Artistas Solos - Nacionais - "canal giobruno18"
		plugintools.add_item(title = "Artistas Solos - Nacionais" , url = base + "channel/UClYguQ-9PhS01xH56N-rI8w/playlists/", thumbnail = icon7, folder = True)
		plugintools.add_item(title = "O Fim Dos Tempos Chegou"           , url = base + "channel/UCD_-fbfpLkDAV_rZ6mX8lVg/", thumbnail = icon8, folder = True)
		plugintools.add_item(title = "Universo Dos Documentários"    , url = base + "channel/UCnnXcMPdZbB0lvcvBQ5KE5g/", thumbnail = icon9, folder = True)
		plugintools.add_item(title = "Visão do Mundo - Documentários", url = base + "channel/UCstl7ql3wXzwncz-Rgd0s-Q/playlists/", thumbnail = icon0, folder = True)

		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
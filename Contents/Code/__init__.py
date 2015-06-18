######################################################################################
#
#	ChannelUpdater
#
######################################################################################
import common, updater

# Set global variables
TITLE = common.TITLE
PREFIX = common.PREFIX
ART = "art-default.jpg"
ICON = "icon-channelupdater.png"
ICON_PREFS = "icon-prefs.png"
ICON_UPDATE = "icon-update.png"

######################################################################################

def Start():

	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	
######################################################################################
# Menu hierarchy

@handler(PREFIX, TITLE, art=ART, thumb=ICON)
def MainMenu():

	oc = ObjectContainer(title2=TITLE)
	oc.add(DirectoryObject(key = Callback(ShowMenu, title='Menu'), title = 'Menu', thumb = R(ICON)))
	oc.add(DirectoryObject(key = Callback(updater.menu, title='Update Plugin'), title = 'Update Plugin', thumb = R(ICON_UPDATE)))
	oc.add(PrefsObject(title = 'Preferences', thumb = R(ICON_PREFS)))
	return oc

@route(PREFIX + "/showMenu")
def ShowMenu(title):
	oc = ObjectContainer(title2=title)
	oc.add(DirectoryObject(key = Callback(nothing, title='Second Menu'), title = 'Second Menu', thumb = R(ICON)))
	return oc
	
@route(PREFIX + '/nothing')
def nothing(title):
	oc = ObjectContainer(title2=title)
	oc.add(DirectoryObject(key = Callback(nothing, title='Second Menu'), title = 'Second Menu', thumb = R(ICON)))

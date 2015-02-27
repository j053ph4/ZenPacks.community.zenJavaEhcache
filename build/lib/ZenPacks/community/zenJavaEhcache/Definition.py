from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *
from ZenPacks.community.zenJavaApp.Definition import getMBeanDef, addMBeanRelations


ROOT = "ZenPacks.community"
BASE = "zenJavaEhcache"
VERSION = Version(1, 0, 0)


###################### EhcacheCacheMBean

EhcacheCacheMBeanDefinition = type('TomcatGlobalRequestProcessorDefinition', (BasicDefinition,), 
                                   getMBeanDef(VERSION, ROOT, BASE, 'EhcacheCacheMBean','Ehcache Cache', 'Ehcache Caches'))
addMBeanRelations(EhcacheCacheMBeanDefinition)


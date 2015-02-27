from Products.DataCollector.plugins.CollectorPlugin import CollectorPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.ZenUtils.Utils import prepId
from ZenPacks.community.zenJavaApp.lib.JavaAppScan import *
from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaEhcache.Definition import *

class EhcacheCacheMBeanMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(EhcacheCacheMBeanDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'net.sf.ehcache:type=CacheStatistics,CacheManager=*,name=*'

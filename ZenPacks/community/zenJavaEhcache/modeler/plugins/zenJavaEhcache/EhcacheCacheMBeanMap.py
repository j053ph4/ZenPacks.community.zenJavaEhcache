from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaEhcache.Definition import *

__doc__ = """EhcacheCacheMBeanMap

EhcacheCacheMBeanMap detects JVM EHCache Caches on a per-JVM basis.

This version adds a relation to associated ipservice and javaapp components.

"""

class EhcacheCacheMBeanMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(EhcacheCacheMBeanDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'net.sf.ehcache:type=CacheStatistics,CacheManager=*,name=*'
    
    def postprocess(self, result, om, log):
        ''''''
        om.setProductKey = MultiArgs('Ehcache', 'Terracotta')
        return om


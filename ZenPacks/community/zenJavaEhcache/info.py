from ZenPacks.community.ConstructionKit.ClassHelper import *

def EhcacheCacheMBeangetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class EhcacheCacheMBeanInfo(ClassHelper.EhcacheCacheMBeanInfo):
    ''''''



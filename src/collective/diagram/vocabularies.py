from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.component import getUtilitiesFor

from .interfaces import IDiagramProducer


def producer_vocabulary(context):
   "return a SimpleVocabulary with (utility, name, name) terms"

   terms = []
   utils = getUtilitiesFor(IDiagramProducer)
   for uname, producer in utils:
      term = SimpleTerm(value=uname, token=uname, title=producer.name)
      terms.append(term)

   return SimpleVocabulary(terms)

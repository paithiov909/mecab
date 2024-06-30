# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _MeCab
else:
    import _MeCab

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class DictionaryInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    filename = property(_MeCab.DictionaryInfo_filename_get)
    charset = property(_MeCab.DictionaryInfo_charset_get)
    size = property(_MeCab.DictionaryInfo_size_get)
    type = property(_MeCab.DictionaryInfo_type_get)
    lsize = property(_MeCab.DictionaryInfo_lsize_get)
    rsize = property(_MeCab.DictionaryInfo_rsize_get)
    version = property(_MeCab.DictionaryInfo_version_get)
    next = property(_MeCab.DictionaryInfo_next_get)

    def __init__(self):
        _MeCab.DictionaryInfo_swiginit(self, _MeCab.new_DictionaryInfo())
    __swig_destroy__ = _MeCab.delete_DictionaryInfo

# Register DictionaryInfo in _MeCab:
_MeCab.DictionaryInfo_swigregister(DictionaryInfo)
class Path(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    rnode = property(_MeCab.Path_rnode_get)
    rnext = property(_MeCab.Path_rnext_get)
    lnode = property(_MeCab.Path_lnode_get)
    lnext = property(_MeCab.Path_lnext_get)
    cost = property(_MeCab.Path_cost_get)
    prob = property(_MeCab.Path_prob_get, _MeCab.Path_prob_set)

# Register Path in _MeCab:
_MeCab.Path_swigregister(Path)
class Node(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    prev = property(_MeCab.Node_prev_get)
    next = property(_MeCab.Node_next_get)
    enext = property(_MeCab.Node_enext_get)
    bnext = property(_MeCab.Node_bnext_get)
    rpath = property(_MeCab.Node_rpath_get)
    lpath = property(_MeCab.Node_lpath_get)
    feature = property(_MeCab.Node_feature_get)
    id = property(_MeCab.Node_id_get)
    length = property(_MeCab.Node_length_get)
    rlength = property(_MeCab.Node_rlength_get)
    rcAttr = property(_MeCab.Node_rcAttr_get)
    lcAttr = property(_MeCab.Node_lcAttr_get)
    posid = property(_MeCab.Node_posid_get)
    char_type = property(_MeCab.Node_char_type_get)
    stat = property(_MeCab.Node_stat_get)
    isbest = property(_MeCab.Node_isbest_get)
    alpha = property(_MeCab.Node_alpha_get)
    beta = property(_MeCab.Node_beta_get)
    prob = property(_MeCab.Node_prob_get, _MeCab.Node_prob_set)
    wcost = property(_MeCab.Node_wcost_get)
    cost = property(_MeCab.Node_cost_get)
    surface = property(_MeCab.Node_surface_get)

# Register Node in _MeCab:
_MeCab.Node_swigregister(Node)
MECAB_NOR_NODE = _MeCab.MECAB_NOR_NODE
MECAB_UNK_NODE = _MeCab.MECAB_UNK_NODE
MECAB_BOS_NODE = _MeCab.MECAB_BOS_NODE
MECAB_EOS_NODE = _MeCab.MECAB_EOS_NODE
MECAB_EON_NODE = _MeCab.MECAB_EON_NODE
MECAB_SYS_DIC = _MeCab.MECAB_SYS_DIC
MECAB_USR_DIC = _MeCab.MECAB_USR_DIC
MECAB_UNK_DIC = _MeCab.MECAB_UNK_DIC
MECAB_ONE_BEST = _MeCab.MECAB_ONE_BEST
MECAB_NBEST = _MeCab.MECAB_NBEST
MECAB_PARTIAL = _MeCab.MECAB_PARTIAL
MECAB_MARGINAL_PROB = _MeCab.MECAB_MARGINAL_PROB
MECAB_ALTERNATIVE = _MeCab.MECAB_ALTERNATIVE
MECAB_ALL_MORPHS = _MeCab.MECAB_ALL_MORPHS
MECAB_ALLOCATE_SENTENCE = _MeCab.MECAB_ALLOCATE_SENTENCE
MECAB_ANY_BOUNDARY = _MeCab.MECAB_ANY_BOUNDARY
MECAB_TOKEN_BOUNDARY = _MeCab.MECAB_TOKEN_BOUNDARY
MECAB_INSIDE_TOKEN = _MeCab.MECAB_INSIDE_TOKEN
class Lattice(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def clear(self):
        return _MeCab.Lattice_clear(self)

    def is_available(self):
        return _MeCab.Lattice_is_available(self)

    def bos_node(self):
        return _MeCab.Lattice_bos_node(self)

    def eos_node(self):
        return _MeCab.Lattice_eos_node(self)

    def end_nodes(self, pos):
        return _MeCab.Lattice_end_nodes(self, pos)

    def begin_nodes(self, pos):
        return _MeCab.Lattice_begin_nodes(self, pos)

    def sentence(self):
        return _MeCab.Lattice_sentence(self)

    def size(self):
        return _MeCab.Lattice_size(self)

    def set_Z(self, Z):
        return _MeCab.Lattice_set_Z(self, Z)

    def Z(self):
        return _MeCab.Lattice_Z(self)

    def set_theta(self, theta):
        return _MeCab.Lattice_set_theta(self, theta)

    def theta(self):
        return _MeCab.Lattice_theta(self)

    def next(self):
        return _MeCab.Lattice_next(self)

    def request_type(self):
        return _MeCab.Lattice_request_type(self)

    def has_request_type(self, request_type):
        return _MeCab.Lattice_has_request_type(self, request_type)

    def set_request_type(self, request_type):
        return _MeCab.Lattice_set_request_type(self, request_type)

    def add_request_type(self, request_type):
        return _MeCab.Lattice_add_request_type(self, request_type)

    def remove_request_type(self, request_type):
        return _MeCab.Lattice_remove_request_type(self, request_type)

    def newNode(self):
        return _MeCab.Lattice_newNode(self)

    def toString(self, *args):
        return _MeCab.Lattice_toString(self, *args)

    def enumNBestAsString(self, N):
        return _MeCab.Lattice_enumNBestAsString(self, N)

    def has_constraint(self):
        return _MeCab.Lattice_has_constraint(self)

    def boundary_constraint(self, pos):
        return _MeCab.Lattice_boundary_constraint(self, pos)

    def feature_constraint(self, pos):
        return _MeCab.Lattice_feature_constraint(self, pos)

    def set_boundary_constraint(self, pos, boundary_constraint_type):
        return _MeCab.Lattice_set_boundary_constraint(self, pos, boundary_constraint_type)

    def set_feature_constraint(self, begin_pos, end_pos, feature):
        return _MeCab.Lattice_set_feature_constraint(self, begin_pos, end_pos, feature)

    def set_result(self, result):
        return _MeCab.Lattice_set_result(self, result)

    def what(self):
        return _MeCab.Lattice_what(self)

    def set_what(self, str):
        return _MeCab.Lattice_set_what(self, str)
    __swig_destroy__ = _MeCab.delete_Lattice

    def __init__(self):
        _MeCab.Lattice_swiginit(self, _MeCab.new_Lattice())

    def set_sentence(self, sentence):
        return _MeCab.Lattice_set_sentence(self, sentence)

# Register Lattice in _MeCab:
_MeCab.Lattice_swigregister(Lattice)
class Model(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def dictionary_info(self):
        return _MeCab.Model_dictionary_info(self)

    def transition_cost(self, rcAttr, lcAttr):
        return _MeCab.Model_transition_cost(self, rcAttr, lcAttr)

    def lookup(self, begin, end, lattice):
        return _MeCab.Model_lookup(self, begin, end, lattice)

    def createTagger(self):
        return _MeCab.Model_createTagger(self)

    def createLattice(self):
        return _MeCab.Model_createLattice(self)

    def swap(self, model):
        return _MeCab.Model_swap(self, model)

    @staticmethod
    def version():
        return _MeCab.Model_version()
    __swig_destroy__ = _MeCab.delete_Model

    def __init__(self, *args):
        _MeCab.Model_swiginit(self, _MeCab.new_Model(*args))

# Register Model in _MeCab:
_MeCab.Model_swigregister(Model)
class Tagger(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def parse(self, *args):
        return _MeCab.Tagger_parse(self, *args)

    def parseToNode(self, str):
        return _MeCab.Tagger_parseToNode(self, str)

    def parseNBest(self, N, str):
        return _MeCab.Tagger_parseNBest(self, N, str)

    def parseNBestInit(self, str):
        return _MeCab.Tagger_parseNBestInit(self, str)

    def nextNode(self):
        return _MeCab.Tagger_nextNode(self)

    def next(self):
        return _MeCab.Tagger_next(self)

    def formatNode(self, node):
        return _MeCab.Tagger_formatNode(self, node)

    def set_request_type(self, request_type):
        return _MeCab.Tagger_set_request_type(self, request_type)

    def request_type(self):
        return _MeCab.Tagger_request_type(self)

    def partial(self):
        return _MeCab.Tagger_partial(self)

    def set_partial(self, partial):
        return _MeCab.Tagger_set_partial(self, partial)

    def lattice_level(self):
        return _MeCab.Tagger_lattice_level(self)

    def set_lattice_level(self, level):
        return _MeCab.Tagger_set_lattice_level(self, level)

    def all_morphs(self):
        return _MeCab.Tagger_all_morphs(self)

    def set_all_morphs(self, all_morphs):
        return _MeCab.Tagger_set_all_morphs(self, all_morphs)

    def set_theta(self, theta):
        return _MeCab.Tagger_set_theta(self, theta)

    def theta(self):
        return _MeCab.Tagger_theta(self)

    def dictionary_info(self):
        return _MeCab.Tagger_dictionary_info(self)

    def what(self):
        return _MeCab.Tagger_what(self)
    __swig_destroy__ = _MeCab.delete_Tagger

    @staticmethod
    def version():
        return _MeCab.Tagger_version()

    def __init__(self, *args):
        _MeCab.Tagger_swiginit(self, _MeCab.new_Tagger(*args))

    def parseToString(self, str, length=0):
        return _MeCab.Tagger_parseToString(self, str, length)

# Register Tagger in _MeCab:
_MeCab.Tagger_swigregister(Tagger)
VERSION = _MeCab.VERSION

